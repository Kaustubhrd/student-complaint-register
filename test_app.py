from app import app, complaints


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_add_complaint():
    client = app.test_client()

    complaints.clear()

    response = client.post(
        "/add",
        data={
            "name": "Test Student",
            "complaint": "Fan is not working",
            "category": "Academic"
        }
    )

    assert response.status_code == 302
    assert len(complaints) == 1
    assert complaints[0]["name"] == "Test Student"
    assert complaints[0]["status"] == "Pending"


def test_invalid_complaint():
    client = app.test_client()

    response = client.post(
        "/add",
        data={
            "name": "",
            "complaint": "",
            "category": "Academic"
        }
    )

    assert response.status_code == 400


def test_api_complaints():
    client = app.test_client()

    complaints.clear()

    complaints.append({
        "name": "API Student",
        "complaint": "Library book issue",
        "category": "Library",
        "status": "Pending"
    })

    response = client.get("/api/complaints")

    assert response.status_code == 200
    assert response.json[0]["name"] == "API Student"
    assert response.json[0]["category"] == "Library"
