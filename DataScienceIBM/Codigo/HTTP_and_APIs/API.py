# %%
!pip install pycoingecko

# %%
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

# %%
bitcoin_data =cg.get_coin_market_chart_by_id(id = 'bitcoin',vs_currency = 'usd',days = 30)

# %%
print(bitcoin_data)

bitcoin_data.keys()

#%%
import pandas as pd

data = pd.DataFrame(bitcoin_data['prices'],columns=['TimeStamp','Price'])

data['Date'] = pd.to_datetime(data['TimeStamp'], unit = 'ms')


# %%






# %% 
import matplotlib.pyplot as plt

fechas = data['Date'].to_numpy()
precios = data['Price'].to_numpy()

plt.plot(fechas, precios)
plt.xticks(rotation=90)

# %%
# # Find minimous max first and last price at day
# candlestick_data = data.groupby(data.Date.dt.date).agg({'Price': ['min','max','first','last']})


# import plotly.graph_objects as go
# import plotlyfig  = go.Figure(data= [go.Candlestick(x = candlestick_data.index, open = candlestick_data['Price']['first'], high = candlestick_data['Price']['max'], low = candlestick_data['Price']['min'], close = candlestick_data['Price']['last'])])

# fig.update_layout(xaxis_rangelider_visible = False, xaxis_title = 'Date', yaxis_title = 'Price (USD $)', title  = 'Bitcoin Candlestick Chart Over Past 30 Days')




import plotly.graph_objects as go

# Group data by date and get min, max, first, and last prices
candlestick_data = data.groupby(data.Date.dt.date).agg({'Price': ['min', 'max', 'first', 'last']})

# Create candlestick figure
fig = go.Figure(data=[go.Candlestick(
    x=candlestick_data.index,
    open=candlestick_data[('Price', 'first')],
    high=candlestick_data[('Price', 'max')],
    low=candlestick_data[('Price', 'min')],
    close=candlestick_data[('Price', 'last')]
)])

# Update layout
fig.update_layout(
    xaxis_rangeslider_visible=False,
    xaxis_title='Date',
    yaxis_title='Price (USD $)',
    title='Bitcoin Candlestick Chart Over Past 30 Days'
)

fig.show()