from collections.abc import Sequence
from datetime import datetime

from fastapi import HTTPException, status

from src.models import Sale
from src.schemas.sales_schema import SaleAnswer
from src.utils.service import BaseService
from src.utils.unit_of_work import transaction_mode


def is_valid_date(date_string):
    """
    Функция для валидации даты
    """
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


class PromptService(BaseService):
    base_repository = "prompt"

    @transaction_mode
    async def to_form_prompt_and_save_db(
        self, date: str
    ) -> dict[str, list[SaleAnswer] | str | Sequence]:
        """
        Метод сервиса для анализа данных, формирования промпта и формирования вывода с сохранением в базу данных
        """
        valid_date = is_valid_date(date)
        if not valid_date:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Введите корректную дату (формат: 2024-01-02)!",
            )

        sale_by_date = await self.uow.sale.get_exists_obj(sale_date=date)
        if not sale_by_date:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Продаж с датой {date} не найдено!",
            )

        sum_price = await self.uow.sale.get_sum_price_or_none(sale_date=date)
        top_products = await self.uow.sale.get_top_three_product_by_count(
            sale_date=date
        )
        top_categories = await self.uow.sale.get_products_distribution_by_category(
            sale_date=date
        )

        prompt_by_date = await self.uow.prompt.get_exists_obj(name=f"Промпт_{date}")
        if not prompt_by_date:
            await self.uow.prompt.add_one(
                name=f"Промпт_{date}",
                total_revenue=sum_price,
                top_product=",".join([prod.name for prod in top_products]),
                top_category=top_categories[0],
            )

        return {
            "Данные о продажах за: ": date,
            "Общая выручка: ": sum_price,
            "Топ-3 товара по продажам: ": [
                self.correct_sale_schema_answer(sale=prod) for prod in top_products
            ],
            "Распределение по категориям: ": top_categories,
            "Краткий аналитический отчет с выводами и рекомендациями: ": f"Лучший товар по продажам: {top_products[0].name}, продан в количестве: {top_products[0].quantity}. Самая востребованная категория {top_categories[0]}",
        }

    def correct_sale_schema_answer(self, sale: Sale) -> SaleAnswer:
        return SaleAnswer(
            name=sale.name,
            quantity=sale.quantity,
            price=sale.price,
            category=sale.category,
        )
