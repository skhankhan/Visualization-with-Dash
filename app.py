# dash for app
import dash
# dash_core_components is used for graph
import dash_core_components as dcc
# dash_html_components library has all the html tags as its own compenents
import dash_html_components as html

# external_stylesheets used from the following link
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app layout is defined here with dash_html_components
app.layout = html.Div(children=[
    
    html.H1(children='Hello World'),

    html.Div(
        html.P(children='Simple visualization using Dash python framework')
    ),

    dcc.Graph(
        id='example-bar-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [1, 1, 3], 'type': 'bar', 'name': 'Bar 1'},
                {'x': [1, 2, 3], 'y': [0.3, 0.2, 2], 'type': 'bar', 'name': 'Bar 2'},
                {'x': [1, 2, 3], 'y': [0, 4, 1], 'type': 'bar', 'name': 'Bar 3'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])
# running app on server
if __name__ == '__main__':
    app.run_server(debug=True)