from collections.abc import Callable
from copy import deepcopy
from pathlib import Path

import pytest
from sqlalchemy import delete, insert

from src.models import Sale
from tests.fixtures.postgres import SALES


@pytest.fixture(scope="function")
def sales():
    return deepcopy(SALES)


@pytest.fixture(scope="function")
def add_sales(async_session_maker, sales) -> Callable:
    async def _add_results():
        async with async_session_maker() as session:
            for sale in sales:
                await session.execute(
                    insert(Sale).values(**sale),
                )
                await session.commit()

    return _add_results


@pytest.fixture(scope="session")
def clean_data(async_session_maker) -> Callable:
    async def _clear_data():
        async with async_session_maker() as session:
            await session.execute(delete(Sale))
            await session.commit()

    return _clear_data
