import pytest
from faker import Faker
from fastapi import (
    FastAPI,
    status,
)
from fastapi.testclient import TestClient
from httpx import Response


@pytest.mark.asyncio
async def test_get_random_art_success(
    app: FastAPI,
    client: TestClient,
    faker: Faker,
):
    url = app.url_path_for("get_random_art_handler")
    art_direction = "modern"
    response: Response = client.post(url=url, json={"art_direction": art_direction})

    assert response.is_success
    json_data = response.json()

    assert json_data["result"][0]["art_direction"]["value"] == art_direction


@pytest.mark.asyncio
async def test_get_random_art_is_valid(
    app: FastAPI,
    client: TestClient,
    faker: Faker,
):
    url = app.url_path_for("get_random_art_handler")
    art_direction = "modern" * 50
    response: Response = client.post(url=url, json={"art_direction": art_direction})

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    json_data = response.json()

    assert json_data["detail"]["error"]
