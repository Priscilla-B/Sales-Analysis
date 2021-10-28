from calendar import month_name
from dash.dcc import ConfirmDialogProvider
from dash.html.Legend import Legend
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

import numpy as np
from statistics import mean
from pivot_tables import *

app = Dash(__name__)
#themes: CYBORG, SLATE, SOLAR, SUPERHERO, FLATLY
server = app.server

df = create_data("data\denormalized-data.xlsx")
trends_df = trend_pivot(df)
regions_df = region_pivot(df)
sub_category_df = sub_category_pivot(df)
date_df = date_table()


cards = html.Div(
    className="cards",
    children=[
        html.Div(
            className="card-item",
            children=[
                html.P("REVENUE", className="chart-title"),
                html.Hr(),
                html.P(className="card-value", id="revenue")
            ]
                    ),
        html.Div(
            className="card-item",
            children=[
                html.P("COST", className="chart-title"),
                html.Hr(),
                html.P(className="card-value", id="cost")
            ]
        ),
        html.Div(
            className="card-item",
            children=[
                html.P("PROFIT", className="chart-title"),
                html.Hr(),
                html.P(className="card-value", id="profit")
                ]
            ),
        html.Div(
            className="card-item",
            children=[
                html.P("PROFIT MARGIN", className="chart-title"),
                html.Hr(),
                html.P(className="card-value", id="p-margin")
                ]
            )
        ]
    )

trend_matrix = html.Div(
    className="trend-matrix",
    children=[
        html.Div(
            className="trend",
            children=[
                html.P(
                    className="chart-title",
                    children=["TREND"]
                ),
                html.Hr(),
                dcc.Graph(
                    id="trend-line")
            ]
        ),
        html.Div(
            className="matrix",
            children=[
                html.P(
                    className="chart-title",
                    children=["PRODUCT SUB-CATEGORY"]
                ),
                html.Hr(),
                dcc.Graph(id="matrix-chart")
                # dash_table.DataTable(
                #     id="matrix-chart",
                #     columns = [{"name":i, "id":i} for i in sub_category_df.columns],
                #     data = sub_category_df.to_dict("records")
                # )
            ]
        )
    ]
)


slicers = html.Div(
    className="slicers",
    children=[
        
    ]
)

timeline = html.Div(
    id="timeline",
    children=[
        html.Div(
            className="time-selectors",
            children=[
            dcc.Dropdown(
                id="year-picker",
                options=[
                    {"label":2018, "value":2018},
                    {"label":2019, "value":2019}
                ],
                value=[2018,2019],
                multi=True
            ),
            dcc.Dropdown(
                id="period-picker",
                options=[
                    {"label":"Days", "value":"Days"},
                    {"label":"Months", "value":"Months"},
                    {"label":"Quarters", "value":"Quarters"}
                ],
                value="Months"
            )
            ]),
        html.Div(
            id="time-slider-container",
            children=[
                dcc.RangeSlider(id="time-slider")
            ]
        )
    ])
    
app.layout = html.Div(
    children=[
        dcc.Store(
            id="card-data",
            storage_type="session",
            data=None),
        html.Div(
            className="title",
            children=[
                html.H1("Sales Analytics Dashboard | Finex Skills Hub"),
            ]
        ),
        html.Div(
            className="charts",
            children=[
                html.Div(
                    className="column-one",
                    children=[
                        cards,
                        trend_matrix,
                        timeline  
                ]
            ),
                html.Div(
                    className="column-two",
                    children=[
                        dcc.Graph(id="map")
                ]
            )
                
            ]
        ),
        slicers
        
    ]
)


@app.callback(
    Output(component_id="card-data", component_property="data"),
    [Input(component_id="year-picker", component_property="value"),
    Input(component_id="period-picker", component_property="value"),
    Input(component_id="time-slider", component_property="value")]
)

def create_card_data(year, period, time):
    df = create_data("data\denormalized-data.xlsx")
    if not (year or period or time):
        return df.to_dict("series")
    time = [i for i in range(min(time), max(time)+1)]
    period = "".join(period)
    df = df[df["Years"].isin(year)]
    df = df[df[period].isin(time)]
    return df.to_dict("series")


@app.callback(
    [Output(component_id="time-slider", component_property="min"),
    Output(component_id="time-slider", component_property="max"),
    Output(component_id="time-slider", component_property="marks"),
    Output(component_id="time-slider", component_property="value")],
    [Input(component_id="year-picker", component_property="value"),
    Input(component_id="period-picker", component_property="value")]
)

def populate_time_slider(year, period):
    date_df_f = date_df.copy()
    date_df_f = date_df_f[date_df_f["Years"].isin(year)]

    period = "".join(period)
    date_df_f = date_df_f[period]

    # if period == ["Months"]:
    #     date_df_f = date_df_f.apply(lambda x: calendar.month_abbr[x])
    
    min_ = int(np.asarray(date_df_f.min()))
    max_ = int(np.asarray(date_df_f.max()))
    marks = {period:str(period) for period in date_df_f}
    value = [min_, max_]
    return min_, max_, marks, value

@app.callback(
    [Output(component_id="revenue", component_property="children"),
    Output(component_id="cost", component_property="children"),
    Output(component_id="profit", component_property="children"),
    Output(component_id="p-margin", component_property="children")],
    Input(component_id="card-data", component_property="data")
    
)

def create_card_values(data):
    df = data

    revenue = df["Revenue"]
    cost = df["Cost"]
    profit = df["Profit"]
    p_margin = sum(profit)/sum(revenue)

    revenue = "{:,}".format(sum(revenue))
    cost = "{:,}".format(sum(cost))
    profit = "{:,}".format(sum(profit))
    p_margin = "{:.2%}".format(p_margin)
    
    return revenue, cost, profit, p_margin
    



if __name__ == '__main__':
    app.run_server(debug=True)