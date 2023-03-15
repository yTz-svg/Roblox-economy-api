import requests

cookie = '  '

gamepass_id = int(input('gamepass id: '))

res = requests.get(f'https://apis.roblox.com/game-passes/v1/game-passes/{gamepass_id}/product-info').json()
product_id = res['ProductId']
seller_id = res['Creator']['Id']
price = res['PriceInRobux']


req = requests.post(
    f'https://economy.roblox.com/v1/purchases/products/{product_id}',

    headers={
    'cookie': f'.ROBLOSECURITY={cookie}'
    },
    json={
    "expectedCurrency":1,
    "expectedPrice":price,
    "expectedSellerId":seller_id
    })

print(req.json())