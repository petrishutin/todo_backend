from beanie import PydanticObjectId


def test_create_user_200(client, fake):  # noqa
    response = client.post(
        "/api/v1/user",
        json={"email": f"{fake.email()}", "password1": "test", "password2": "test"},
    )
    assert response.status_code == 201, response.json()
    assert PydanticObjectId(response.json())


def test_create_user_400(client, create_user_data):  # noqa
    user = create_user_data()
    client.post("/api/v1/user", json=user)
    response = client.post("/api/v1/user", json=user)
    assert response.status_code == 400, response.json()


def test_get_user_200(client, auth_header):  # noqa
    response = client.get("/api/v1/user", headers=auth_header)
    assert response.status_code == 200, response.json()
    for key in ("email", "hashed_password"):
        assert key in response.json(), response.json()


def test_get_user_404(client):  # noqa
    response = client.get(f"/api/v1/user/{str(PydanticObjectId())}")
    assert response.status_code == 404, response.json()
