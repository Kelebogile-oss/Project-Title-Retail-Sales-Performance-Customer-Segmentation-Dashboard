import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc

# Load dataset
df = pd.read_csv('data/featured_sales_data.csv', parse_dates=['Order Date'])
df['Month'] = df['Order Date'].dt.to_period('M').astype(str)

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Live Sales Dashboard"

# Prepare charts
category_fig = px.bar(
    df.groupby('Category')['Sales'].sum().reset_index(),
    x='Category', y='Sales',
    title="Sales by Category",
    color='Category',
    template='plotly_white'
)

monthly_fig = px.line(
    df.groupby('Month')['Sales'].sum().reset_index(),
    x='Month', y='Sales',
    title="Monthly Sales Trend",
    markers=True,
    template='plotly_white'
)

customer_fig = px.bar(
    df.groupby('Customer Name')['Sales'].sum().nlargest(10).reset_index(),
    x='Sales', y='Customer Name',
    title="Top 10 Customers by Sales",
    orientation='h',
    template='plotly_white'
)

region_fig = px.bar(
    df.groupby('Region')['Profit'].sum().reset_index(),
    x='Region', y='Profit',
    title="Profit by Region",
    color='Region',
    template='plotly_white'
)

# Layout
app.layout = dbc.Container([
    html.H1("📊 Real-Time Sales Dashboard", className="text-center my-4"),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=category_fig), md=6),
        dbc.Col(dcc.Graph(figure=region_fig), md=6),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=monthly_fig), md=6),
        dbc.Col(dcc.Graph(figure=customer_fig), md=6),
    ]),
], fluid=True)

# Run app
if __name__ == '__main__':
    app.run(debug=True)

