from app import schema
from jose import jwt
from app.config import settings
import pytest

    # def test_root(client):
    #     res = client.get("/")
    #     assert res.json().get("message") == "Hello World"
    #     assert res.status_code == 200



def test_create_user(client):
    res = client.post("/users",json={"email": "rajko@yahoo.com","password" : "rajko123"})
    new_user = schema.UserOut(**res.json())
    assert new_user.email == 'rajko@yahoo.com'
    assert res.status_code == 201

def test_login_user(client,test_user):
    res = client.post("/login",data={"username": test_user['email'],"password" : test_user['password']})
    login_res = schema.Token(**res.json())
    payload = jwt.decode(login_res.access_token,settings.secret_key,algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == 'bearer'
    assert res.status_code == 200

@pytest.mark.parametrize("email,password,status_code",[
    ('wrongemail@gmail.com',"rajko123",403),
    ("rajko@yahoo.com",'wrongpasswrd',403),
    ("wrong@yahoo.com","hou123",403),
    (None, "rajko123",422),
    ("rajko@yahoo.com",None,422),
])
def test_incorrect_login(client,email,password,status_code):
    res = client.post("/login", data={"username" : email, "password" : password})
    assert res.status_code == status_code


