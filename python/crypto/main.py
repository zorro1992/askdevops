from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

print(cg)

data1 = cg.get_price(ids='bitcoin', vs_currencies='usd')
print(data1)

data2 = cg.get_price(ids='bitcoin,litecoin,ethereum', vs_currencies='usd')
print(data2)

data3 = cg.get_price(ids='bitcoin,litecoin,ethereum', vs_currencies='usd,eur')
print(data3)
