from collections.abc import Sequence

from sqlalchemy import Result, desc, func, insert, select

from src.models import Sale
from src.utils.repository import SQLAlchemyRepository


class SaleRepository(SQLAlchemyRepository):
    model = Sale

    async def add_many_obj(self, *args) -> None:
        query = insert(self.model).values(*args)
        await self.session.execute(query)

    async def get_sum_price_or_none(self, **kwargs) -> type(model) | None:
        query = select(func.sum(self.model.price)).filter_by(**kwargs)
        res: Result = await self.session.execute(query)
        return res.unique().scalar_one_or_none()

    async def get_top_three_product_by_count(self, **kwargs) -> Sequence:
        query = (
            select(self.model)
            .filter_by(**kwargs)
            .order_by(desc(self.model.quantity))
            .limit(3)
        )
        res: Result = await self.session.execute(query)
        return res.scalars().all()

    async def get_products_distribution_by_category(self, **kwargs) -> Sequence:
        query = (
            select(self.model.category, func.count(self.model.category))
            .filter_by(**kwargs)
            .order_by(desc(self.model.category))
            .group_by(self.model.category)
        )
        res: Result = await self.session.execute(query)
        result = [f"{i[0]} - {i[1]}" for i in res.all()]
        return result
