import yfinance as yf
import pandas as pd
import streamlit as st
import pilotly.express as pt
st.title("ilk cloud streamlit projem")


btc=yf.download("BTC-USD","2008-01-01", "2023-09-12")

st.table(btc)
