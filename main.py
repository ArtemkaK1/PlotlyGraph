import pandas as pd
import plotly.express as px
import dash
from dash import html
from dash import dcc

# Данные из https://github.com/rssh/dou_pl_questionare/blob/master/2024_01/FinalTable.csv
data = pd.read_csv('FinalTable.csv').head(10)

# Создание фигуры Plotly
fig = px.bar(x=data['language'], y=data['freq'], labels={'x': 'Язык программирования', 'y': 'Процент использования'},
             title='Топ-10 самых популярных языков программирования на 2024')

# Создание Dash приложения
app = dash.Dash(__name__)

# Отображение графика в Dash
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
