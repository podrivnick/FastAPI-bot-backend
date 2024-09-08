import pytest
from faker import Faker
from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx import Response


@pytest.mark.asyncio
async def test_get_random_flower_success(
    app: FastAPI,
    client: TestClient,
    faker: Faker,
):
    url = app.url_path_for("get_random_flower_handler")
    get_random_flower_photo = True
    response: Response = client.get(
        url=url,
        params={"get_random_flower_photo": get_random_flower_photo},
    )

    assert response.is_success
    json_data = response.json()

    assert len(json_data["result"][0]["flower_name"]["value"]) > 0
