import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load data
df = pd.read_csv("output.csv")

# Convert and clean data
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["sales"] = pd.to_numeric(df["sales"], errors="coerce")

df = df.dropna()
df = df.sort_values("date")

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time"
)

# Add vertical line for price change date
fig.add_vline(
    x="2021-01-15",
    line_width=3,
    line_dash="dash",
    line_color="red"
)

# Optional annotation (makes your submission stronger)
fig.add_annotation(
    x="2021-01-15",
    y=df["sales"].max(),
    text="Price Increase (15 Jan 2021)",
    showarrow=True,
    arrowhead=1
)

# Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Sales Visualiser"),
    dcc.Graph(figure=fig)
])

# Run server
if __name__ == "__main__":
    app.run(debug=True)