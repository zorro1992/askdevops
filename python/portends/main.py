from pytrends.request import TrendReq
import pytrends
pytrends = TrendReq(hl='en-US', tz=360)
pytrends.build_payload(kw_list=['bitcoin'])
df = pytrends.interest_over_time()
df["bitcoin"].plot(figsize=(20,7),color='purple',linewidth=7)
