import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("output.csv")

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["sales"] = pd.to_numeric(df["sales"], errors="coerce")
df = df.dropna()
df = df.sort_values("date")

# Regions list
regions = ["all", "north", "south", "east", "west"]

# Dash app
app = Dash(__name__)

app.layout = html.Div(style={"fontFamily": "Arial", "padding": "20px"}, children=[

    html.H1(
        "Soul Foods Sales Visualiser",
        style={"textAlign": "center", "color": "#2c3e50"}
    ),

    html.Div([
        html.Label("Select Region:", style={"fontWeight": "bold"}),

        dcc.RadioItems(
            id="region-filter",
            options=[{"label": r.title(), "value": r} for r in regions],
            value="all",
            inline=True,
            style={"marginBottom": "20px"}
        )
    ]),

    dcc.Graph(id="sales-chart")
])

# Callback for filtering
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    filtered_df = df.copy()

    if selected_region != "all":
        filtered_df = filtered_df[filtered_df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales Over Time ({selected_region.title()})"
    )

    fig.add_vline(
        x="2021-01-15",
        line_width=3,
        line_dash="dash",
        line_color="red"
    )

    fig.add_annotation(
        x="2021-01-15",
        y=filtered_df["sales"].max() if not filtered_df.empty else 0,
        text="Price Increase",
        showarrow=True,
        arrowhead=1
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)