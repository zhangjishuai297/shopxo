import pytest
import requests

# 测试购物车

# 登录账号
session = requests.Session()
login_url = "http://vless.shuai-shuai.top:8888/?s=user/login"
    
login_payload = {
        "accounts": '10000000001',
        "pwd": '123456',
        "type": 'username'
    }
response = session.post(login_url, json=login_payload)
print(response.text)

@pytest.mark.parametrize("goods_id,spec, stock, code, desc", [
    ("2", [{"value": "套餐二"},{"value": "银色"},{"value": "64G"}],
           1, 0, '添加购物车成功'),   # 添加购物车成功
    # ('9999', [], 1, -2, '商品不存在'),    # 商品不存在
    # ('2', [], 1, -1, '商品规格不存在'),  # 商品规格不存在
    # ('2', [{"value": "套餐二"},{"value": "银色"},{"value": "64G"}], 0, -1, '商品数量不能小于1'), # 商品数量不能小于1
    # ('2', [{"value": "套餐二"},{"value": "银色"},{"value": "64G"}], 99999999999, -1, '库存不足'), # 库存不足
        
])
def test_add_cart(goods_id, spec, stock, code, desc):

    url = "http://vless.shuai-shuai.top:8888/?s=cart/save"
        
    # payload = {
    #     "goods_id": goods_id,
    #     "spec": spec,
    #     "num": num
    # }
    payload = {
        "goods_id": goods_id,
        "spec": spec,
          "stock": stock
        }

    response = session.post(url, json=payload)
    print(response.text)
    assert response.json().get("code") == code

# 删除购物车商品
@pytest.mark.parametrize("id, code, desc", [
    # ("6", 1, '删除成功'),   # 删除成功
    ('string', -100, '删除失败'),    # 删除失败
])
def test_del_cart(id, code, desc):

    url = "http://vless.shuai-shuai.top:8888/?s=cart/delete"
        
    payload = {
        "id": id,
        }

    response = session.post(url, json=payload)
    print(response.text)
    assert response.json().get("code") == code