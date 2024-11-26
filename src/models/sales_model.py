from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base_model import BaseModel
from src.models.mixins.custom_types import created_at_ct, integer_pk
from src.schemas.sales_schema import SaleDB


class Sale(BaseModel):
    __tablename__ = "sale_table"

    id: Mapped[integer_pk]
    sale_date: Mapped[str]
    product_id: Mapped[int]
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    created_at: Mapped[created_at_ct]

    def to_pydantic_schema(self) -> SaleDB:
        return SaleDB(**self.__dict__)
