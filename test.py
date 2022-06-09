import plotly_express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
app.layout = html.Div(
	[
	dcc.Input(id="input1", type="text", placeholder="", style={'marginRight':'10px'}, value=""),
	html.Div(id="output", children=[]),
	]
	)

@app.callback(Output("output", "children"), Input("input1", "value"))
def update(input):
	if input is None:
		dash.no_update()
	return str(input)

app.run_server(debug=True)
