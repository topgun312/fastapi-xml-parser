from src.models import Prompt
from src.utils.repository import SQLAlchemyRepository


class PromptRepository(SQLAlchemyRepository):
    model = Prompt
