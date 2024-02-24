import pandas as pd
import plotly.express as px
import dash
from dash import html
from dash import dcc

# Данные https://github.com/rssh/dou_pl_questionare/tree/master
def load_data(year):
    file_path = f'year_{year}.csv'
    data = pd.read_csv(file_path).head(10)
    return data

# Создание Dash приложения
app = dash.Dash(__name__)

# Опции для выбора года
year_options = [{'label': str(year), 'value': year} for year in range(2022, 2025)]

# Создание фигуры Plotly
def create_figure(data, year):
    fig = px.bar(x=data['language'], y=data['freq'], labels={'x': 'Язык программирования', 'y': 'Процент использования'},
                 title=f'Топ-10 самых популярных языков программирования на {year}')
    return fig

# Отображение графика и поля выбора года в Dash
app.layout = html.Div([
    dcc.Dropdown(
        id='year-dropdown',
        options=year_options,
        value=2022
    ),
    dcc.Graph(id='bar-chart')
])

@app.callback(
    dash.dependencies.Output('bar-chart', 'figure'),
    [dash.dependencies.Input('year-dropdown', 'value')]
)
def update_figure(selected_year):
    data = load_data(selected_year)
    fig = create_figure(data, selected_year)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
