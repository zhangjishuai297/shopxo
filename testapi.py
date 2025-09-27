import requests
# 测试git用户名,添加了用户名
session = requests.Session()

def test_register_user():
    url = "http://vless.shuai-shuai.top:8888/?s=user/reg"
    payload = {
        "accounts": "10000000001",
        "pwd": "123456",
        # "verify": 2456,
        "type": "username"
    }
    response = requests.post(url, json=payload)
    print(response.text)

def test_login_user():
    url = "http://vless.shuai-shuai.top:8888/?s=user/login"
    payload = {
        "accounts": "10000000001",
        "pwd": "123456",
        "type": "username"
    }
    response = session.post(url, json=payload)
    print(response.text)

# 测试获取首页
def test_get_index():
    url = "http://vless.shuai-shuai.top:8888/?s=index/index"
    response = session.get(url)
    # print(response.text)

# 测试搜索
def test_search():
    url = "http://vless.shuai-shuai.top:8888/?s=search/index"
    payload = {
        "wd": "苹果",
        "page": 1
    }
    response = session.post(url, json=payload)
    print(response.text)

# 测试加入购物车
def test_add_cart():
    url = "http://vless.shuai-shuai.top:8888/?s=cart/save"
    payload = {
    "goods_id": "2",
        "spec": [
            {
                "type": "套餐",
                "value": "套餐二"
            },
            {
                "type": "颜色",
                "value": "银色"
            },
            {
                "type": "容量",
                "value": "64G"
            }
        ],
        "stock": 2
    }

    response = session.post(url, json=payload)
    print(response.text)

# test_register_user()
test_login_user()

