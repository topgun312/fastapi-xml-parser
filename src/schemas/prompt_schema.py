from pydantic import BaseModel, Field

from src.schemas.response import BaseCreateResponse, BaseResponse


class PromptId(BaseModel):
    id: int


class CreatePromptRequest(BaseModel):
    name: str
    total_revenue: float
    top_product: list[str] = Field(default_factory=list)
    top_category: str


class PromptDB(PromptId, CreatePromptRequest): ...


class PromptResponse(BaseResponse):
    payload: PromptDB


class PromptListResponse(BaseResponse):
    payload: list[PromptDB]


class PromptCreateResponse(BaseCreateResponse):
    payload: PromptDB
