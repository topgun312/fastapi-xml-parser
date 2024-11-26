from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from src.models.base_model import BaseModel
from src.models.mixins.custom_types import created_at_ct, integer_pk
from src.schemas.prompt_schema import PromptDB


class Prompt(BaseModel):
    __tablename__ = "prompt_table"

    id: Mapped[integer_pk]
    name: Mapped[str] = mapped_column(default=f"{datetime.now()}")
    total_revenue: Mapped[float] = mapped_column(nullable=True)
    top_product: Mapped[str] = mapped_column(nullable=True)
    top_category: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[created_at_ct]

    def to_pydantic_schema(self) -> PromptDB:
        return PromptDB(**self.__dict__)
