from typing import Any

from fastapi import APIRouter, Depends, status
from fastapi_cache.decorator import cache

from src.api.parser_data.v1.service.prompt_service import PromptService

router = APIRouter(prefix="/prompt", tags=["Prompt work"])


@router.post("/get_prompt/{date}", status_code=status.HTTP_200_OK)
@cache(expire=3600)
async def get_prompt_and_add_to_db(
    date: str, service: PromptService = Depends(PromptService)
) -> Any:
    """
    Анализ данных для формирования промпта с выводами
    """
    result = await service.to_form_prompt_and_save_db(date=date)
    return result
