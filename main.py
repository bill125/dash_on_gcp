# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import numpy as np

app = Dash(__name__)
server = app.server

# assume you have a "long-form" data frame

# flights = pd.read_csv("flights.csv.gz")
# airports = pd.read_csv("airports.csv")
# weather = pd.read_csv('weather.csv.gz')
# flights_weather = flights.merge(weather, on=['year','month','day','hour'], how='left')
# for colname in ['dewp', 'humid', 'wind_speed', 'wind_dir']:
#     flights_weather[colname] = flights_weather.apply(lambda row: row[''.join([colname, '_', row['origin']])] \
#                                      if row['origin'] in ['EWR', 'JFK', 'LGA'] else np.NAN, axis=1)
# for airport in ['EWR', 'JFK', 'LGA']:
#     flights_weather.drop(['dewp_{}'.format(airport), 'humid_{}'.format(airport), 'wind_dir_{}'.format(airport), 'wind_speed_{}'.format(airport)], inplace=True, axis=1)
flights_weather = pd.read_csv('flights_weather.csv.gz')
df = flights_weather[flights_weather['dep_delay'] > 60]
humid_bins = np.arange(df['humid'].min(),df['humid'].max(),2)
wind_speed_bins = np.arange(df.wind_speed.min(),df.wind_speed.max(),2)
groups = df.groupby([pd.cut(df.wind_speed, wind_speed_bins), pd.cut(df.humid, humid_bins)]).size().unstack()
fig = px.imshow(groups.to_numpy(),
                labels=dict(x="humid", y="wind speed", color="departure delay flights count"),
                x=humid_bins[1:],
                y=wind_speed_bins[1:])
fig.update_yaxes(autorange=True)    


df2 = flights_weather
fig2 = px.histogram(df2, x="dep_delay", range_x=[-100,400])


app.layout = html.Div(children = [
    html.H1(children = "depature delay distribution",
            style={
                'textAlign': 'center',
            }),
    dcc.Graph(id="delay",
              figure=fig2),
    html.H4(children = "This is a histogram graph showing the distribution of depature delay. A flight is considered delay if it depatures 60 minutes behind the schedule. \
            It shows that most of the flights depature on time or a little bit earlier, while there are still some flights delay. \
                The longer the delay, the fewer the number of flights. This inspires me to dig deeper into the factor that affects flight delay"),
    html.H1(children = 'Depature delay related to humid and wind speed',
            style={
                'textAlign': 'center',
            }),
    dcc.Graph(id="graph",
              figure=fig),
    html.H4(children = "This is a heatmap showing the factors that affect flight delay. Two factors, humid and wind speed, were taken into consideration. \
            From the heat map, we find that most of the flight delay happen when the humid is high. \
            This indicate that humid may be the cause of flight delay, while wind speed is not.")
])

if __name__ == '__main__':
    app.run_server(debug=True, port=9527)
