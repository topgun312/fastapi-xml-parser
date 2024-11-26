from loguru import logger

from src.api.parser_data.v1.service.parse_service import GetFileService
from src.tasks.celery_app import celery

service = GetFileService()


@celery.task(name="get_file_from_site")
def get_file_from_site() -> None:
    """
    Парсинг xml файлов с сайта и сохранение в папку xml_files ежедневно в 10:00
    """

    async def add_task():
        await service.get_page_count()
        return add_task

    logger.info(
        "Запущена задача для парсинга xml файлов с сайта и сохранение в папку xml_files ежедневно в 10:00"
    )
