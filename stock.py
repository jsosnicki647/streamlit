import yfinance
import streamlit
import pandas
from datetime import date

streamlit.write("""
# Simple Stock Price App

Search for a Ticker Symbol below.

"""
)

today = date.today()
month = date.today().month
day = date.today().day
startYear = date.today().year - 10

tickerSymbol = streamlit.text_input("Ticker Symbol:","GOOGL")
tickerData = yfinance.Ticker(tickerSymbol)
tickerDF = tickerData.history(period='id', start=str(startYear)+'-'+str(month)+'-'+str(day), end=today)

streamlit.write("Close")
streamlit.line_chart(tickerDF.Close)
streamlit.write("Volume")
streamlit.line_chart(tickerDF.Volume)