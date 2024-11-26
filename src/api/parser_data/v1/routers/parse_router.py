from fastapi import APIRouter, Depends, status
from fastapi_cache.decorator import cache

from src.api.parser_data.v1.service.parse_service import ParseFileService

router = APIRouter(prefix="/parse", tags=["Parse work"])


@router.get("/parse_file_data", status_code=status.HTTP_200_OK)
@cache(expire=3600)
async def add_parse_data_to_db(
    service: ParseFileService = Depends(ParseFileService),
) -> dict[str, int | str]:
    """
    Добавление информации из файлов в базу данных
    """
    await service.parse_file_data_to_db()
    return {
        "status": status.HTTP_200_OK,
        "detail": "Файлы обработаны и добавлены в базу данных",
    }
