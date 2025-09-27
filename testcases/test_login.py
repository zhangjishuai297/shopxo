import pytest
import requests

# 登录类型type（账号 username ，手机 sms，邮箱 email）
# 登录接口用例
@pytest.mark.parametrize("accounts,pwd,type,code, desc", [
    ("10000000001", "123456", "username", 0, "用户名正确密码正确"),
    ("10000000001", "000000", "username", -4, "密码错误"),
    ("19999999999", "123456", "username", -3, "帐号不存在"),
    ("", "123456", "username", -1, "用户名为空"),
    ("10000000001", "11111", "username", -1, "密码格式小于6位"),
    ("10000000001", "1234561234561234561", "username", -1, "密码格式大于18位"),
    ("10000000001", "123456", "1", -1, "type格式错误")
])
def test_login(accounts, pwd, type, code, desc):
    url = "http://vless.shuai-shuai.top:8888/?s=user/login"
    
    payload = {
            "accounts": accounts,
            "pwd": pwd,
            "type": type
        }
    response = requests.post(url, json=payload)
    print(response.text)
    assert response.json().get("code") == code