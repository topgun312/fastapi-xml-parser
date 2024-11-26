from typing import Any

import pytest
from httpx import AsyncClient

from tests import fixtures
from tests.utils import prepare_payload


class TestParseRouter:
    @staticmethod
    @pytest.mark.parametrize(
        ("url", "expected_status_code", "expected_payload", "expectation"),
        fixtures.test_cases.PARAMS_TEST_PARSE_ROUTE_GET,
    )
    async def test_add_parse_data_to_db(
        url: str,
        expected_status_code: int,
        expected_payload: dict,
        expectation: Any,
        async_client: AsyncClient,
        clean_data,
    ) -> None:
        with expectation:
            await clean_data()
            response = await async_client.get(url)
            assert response.status_code == expected_status_code
            assert prepare_payload(response) == expected_payload
