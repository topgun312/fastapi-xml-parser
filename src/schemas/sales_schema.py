from pydantic import BaseModel, Field

from src.schemas.response import BaseCreateResponse, BaseResponse


class SaleId(BaseModel):
    id: int


class SaleAnswer(BaseModel):
    name: str = Field(max_length=50)
    quantity: int
    price: float
    category: str


class CreateSaleRequest(SaleAnswer):
    product_id: int
    sale_date: str


class SaleDB(SaleId, CreateSaleRequest): ...


class SaleResponse(BaseResponse):
    payload: SaleDB


class ProductListResponse(BaseResponse):
    payload: list[SaleDB]


class ProductCreateResponse(BaseCreateResponse):
    payload: SaleDB
