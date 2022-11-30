import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

df = pd.read_pickle('my_dataframe.pickle')


fig = px.pie(df, values='GRAVEDAD', names='TIPO_GRAVEDAD')
# fig.show()


# print(df.head())

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Accidentes por Tipo'),
    dcc.Graph(figure=fig)


])

if __name__ == '__main__':
    app.run_server(debug=True)
