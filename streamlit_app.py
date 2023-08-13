import yfinance as yf
import pandas as pd
import streamlit as st
st.title("ilk cloud streamlit projem")


btc=yf.dowload("BTC-USD","2008-01-01", "2023-09-12")

st.table(btc)
