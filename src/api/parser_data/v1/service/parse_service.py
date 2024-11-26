import asyncio
import copy
import pathlib
from datetime import datetime

import aiofiles
from aiohttp import ClientSession
from bs4 import BeautifulSoup as bs
from loguru import logger

from src.config import SITE_URL, directory
from src.utils.service import BaseService
from src.utils.unit_of_work import transaction_mode


class GetFileService:

    def __init__(self):
        self.create_dir = self.create_files_dir()

    @staticmethod
    def create_files_dir() -> None:
        """
        Метод для создания папки xml_files
        """
        dir = pathlib.Path.cwd() / "xml_files"
        if not dir.exists() and not dir.is_dir():
            dir.mkdir(exist_ok=True)
            logger.info("Директория xml_files создана!")
        else:
            logger.info("Директория xml_files инициализирована!")

    async def get_page_count(self) -> None:
        """
        Метод для получения количества страниц в пагинаторе
        """
        print("ssssssssssssssssssssssssssssssssss")
        tasks = []
        async with ClientSession() as session:
            response = await session.get(url=SITE_URL)
            soup = bs(await response.text(), "lxml")
            page_count = int(
                soup.find("div", class_="pagination_class")
                .find_all("span")[0]
                .get_text()
            )
            for page in range(1, page_count):
                task = await self.get_links_and_date_files(session, page)
                if not task:
                    break
                tasks.append(task)
            await asyncio.gather(*tasks)

    async def get_links_and_date_files(self, session: ClientSession, page: int) -> None:
        """
        Метод для получения ссылок и дат загрузки файлов
        """
        dates = []
        links = []
        page_url = SITE_URL + f"?page=page-{page}"
        async with session.get(url=page_url) as response:
            soup = bs(await response.text(), "lxml")
            docs_on_page = soup.find_all("div", class_="class_name")
            for item in docs_on_page:
                doc_date = (
                    item.find("div", class_="date_class_name").find("span").get_text()
                )
                doc_date = (
                    datetime.strptime(doc_date, "%d.%m.%Y").date().strftime("%Y-%m-%d")
                )
                dates.append(doc_date)
                link = item.find("a", class_="link_class_name").get("href")

                links.append(link)
        dict_result = dict(zip(dates, links))
        if len(dict_result) > 0:
            await self.download_files_on_repository(dict_result, session)

    async def download_files_on_repository(
        self, dict_result: dict, session: ClientSession
    ) -> None:
        """
        Метод для создания файлов
        """
        for date, link in dict_result.items():
            filename = f"xml_files/{date}.xml"
            async with session.get(url=link) as response:
                data = await response.read()
                async with aiofiles.open(filename, "wb") as file:
                    await file.write(data)


class ParseFileService(BaseService):
    base_repository = "parse"

    @transaction_mode
    async def parse_file_data_to_db(self) -> None:
        """
        Метод сервиса для добавления информации из файлов в базу данных
        """
        data_dict = dict()
        data_list = []

        for file in directory.iterdir():
            if file.is_file():
                with open(str(directory) + "/" + file.name, "r") as f:
                    xml_file = f.read()
                    soup = bs(xml_file, "lxml")
                    for tag in soup.find_all("product"):
                        data_dict = copy.deepcopy(data_dict)
                        data_dict["sale_date"] = soup.find("sales_data").get("date")
                        data_dict["product_id"] = int(tag.find("id").text)
                        data_dict["name"] = tag.find("name").text
                        data_dict["quantity"] = int(tag.find("quantity").text)
                        data_dict["price"] = float(tag.find("price").text)
                        data_dict["category"] = tag.find("category").text
                        data_list.append(data_dict)
                        sort_list = sorted(
                            data_list, key=lambda x: (x["sale_date"], x["product_id"])
                        )
        for i in directory.iterdir():
            date = i.name.split(".")[0]
            s = await self.uow.sale.get_exists_obj(sale_date=date)
            if s:
                sort_list = list(
                    filter(lambda x: x["sale_date"] != s[0].sale_date, sort_list)
                )
        if len(sort_list) > 0:
            await self.uow.sale.add_many_obj(sort_list)
        logger.info("Данные из файлов .xml в базу данных загружены")
