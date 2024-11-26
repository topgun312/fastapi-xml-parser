from typing import Any

import pytest
from httpx import AsyncClient

from tests import fixtures
from tests.utils import prepare_payload


class TestPromptRouter:
    @staticmethod
    @pytest.mark.parametrize(
        ("url", "json", "expected_status_code", "expected_payload", "expectation"),
        fixtures.test_cases.PARAMS_TEST_PROMPT_ROUTE_GET,
    )
    async def test_get_prompt_and_add_to_db(
        url: str,
        json: dict,
        expected_status_code: int,
        expected_payload: dict,
        expectation: Any,
        async_client: AsyncClient,
        add_sales,
        clean_data,
    ) -> None:
        with expectation:
            await clean_data()
            await add_sales()
            response = await async_client.post(url, json=json)
            assert response.status_code == expected_status_code
            assert prepare_payload(response) == expected_payload
