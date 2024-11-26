from collections.abc import Awaitable, Callable
from datetime import datetime
from typing import Annotated, Any

from sqlalchemy import DateTime, Integer, text
from sqlalchemy.orm import mapped_column

db_utc_now = text("TIMEZONE('utc', now())")
AsyncFunc = Callable[..., Awaitable[Any]]

integer_pk = Annotated[int, mapped_column(Integer, primary_key=True, index=True)]
created_at_ct = Annotated[datetime, mapped_column(DateTime, server_default=db_utc_now)]
