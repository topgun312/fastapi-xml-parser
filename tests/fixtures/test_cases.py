from contextlib import nullcontext as does_not_raise

# url, date, expected_status_code, expected_payload, expectation
PARAMS_TEST_PROMPT_ROUTE_GET = [
    # positive case
    (
        "api/prompt/get_prompt/2024-01-01",
        "2024-01-01",
        200,
        {
            "Данные о продажах за: ": "2024-01-01",
            "Общая выручка: ": 7620.0,
            "Топ-3 товара по продажам: ": [
                {
                    "name": "Product B",
                    "quantity": 200,
                    "price": 2500.0,
                    "category": "Electronics",
                },
                {
                    "name": "Product D",
                    "quantity": 200,
                    "price": 10.0,
                    "category": "Household products",
                },
                {
                    "name": "Product C",
                    "quantity": 150,
                    "price": 110.0,
                    "category": "Household products",
                },
            ],
            "Распределение по категориям: ": [
                "Household products - 2",
                "Electronics - 3",
            ],
            "Краткий аналитический отчет с выводами и рекомендациями: ": "Лучший товар по продажам: Product B, продан в количестве: 200. Самая востребованная категория Household products - 2",
        },
        does_not_raise(),
    ),
    # not valid request body
    (
        "api/prompt/get_prompt/2024-99-99",
        "2024-99-99",
        400,
        {"detail": "Введите корректную дату (формат: 2024-01-02)!"},
        does_not_raise(),
    ),
    # not found date
    (
        "api/prompt/get_prompt/2024-01-02",
        "2024-01-02",
        404,
        {"detail": "Продаж с датой 2024-01-02 не найдено!"},
        does_not_raise(),
    ),
]


# url,  expected_status_code, expected_payload, expectation
PARAMS_TEST_PARSE_ROUTE_GET = [
    # positive case
    (
        "api/parse/parse_file_data",
        200,
        {"status": 200, "detail": "Файлы обработаны и добавлены в базу данных"},
        does_not_raise(),
    ),
]
