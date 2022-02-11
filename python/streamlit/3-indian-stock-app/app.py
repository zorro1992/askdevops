import streamlit as st
from bsedata.bse import BSE
b = BSE()
print(b)
# Output:
# Driver Class for Bombay Stock Exchange (BSE)

# to execute "updateScripCodes" on instantiation
b = BSE(update_codes=True)

tg = b.topGainers()
print(tg)
st.title("Top 10 Losers")
for x in range(len(tg)):
    # print(tg[x]['securityID'])
    st.text(tg[x]['securityID'])
