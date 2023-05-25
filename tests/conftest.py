from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.main import app
from app.config import settings
from app.database import get_db
from app.database import Base
from app.oauth2 import create_access_token
from app import models
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:radmilo123@localhost:5432/fastapi_test"
SQLALCHEMY_DATABASE_URL =f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}_test'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)


@pytest.fixture()
def session():
     print("my session fixture ran")
     Base.metadata.drop_all(bind=engine)
     Base.metadata.create_all(bind=engine)
     db = TestingSessionLocal()
     try:
        yield db
     finally:
        db.close()

@pytest.fixture()
def client(session):
     def override_get_db():
        try:
            yield session
        finally:
            session.close()
     app.dependency_overrides[get_db] = override_get_db
     yield TestClient(app)



@pytest.fixture
def test_user(client):
    user_data = {"email" : "radmilo@yahoo.com", "password" : "radmilo123"}

    res = client.post("/users/",json= user_data)

    assert res.status_code == 201
    print(res.json())
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user

@pytest.fixture
def test_user2(client):
    user_data = {"email" : "raki@yahoo.com", "password" : "raki123"}

    res = client.post("/users/",json= user_data)

    assert res.status_code == 201
    print(res.json())
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user

@pytest.fixture
def token(test_user):
    return create_access_token({"user_id" : test_user['id']})

@pytest.fixture
def authorized_client(client,token):
    client.headers = {
        **client.headers,
        "Authorization" :f"Bearer {token}"
    }
    return client

@pytest.fixture
def test_posts(test_user,session,test_user2):
    posts_data = [{"title" : "first", "content": "first content","owner_id" : test_user['id']},
                  {"title" : "second", "content": "second content","owner_id" : test_user['id']},
                  {"title" : "third", "content": "third content","owner_id" : test_user['id']},
                  {"title" : "fir", "content": "fir content","owner_id" : test_user2['id']},]
    
    session.add_all([models.Post(title='first title', content='first content',user_id = test_user['id']),
                     models.Post(title='second title', content='second content',user_id = test_user['id']),
                      models.Post(title='third title', content='third content',user_id = test_user['id']),
                      models.Post(title='fourth', content='third content',user_id = test_user2['id'])])
    session.commit()
    posts = session.query(models.Post).all()
    return posts


