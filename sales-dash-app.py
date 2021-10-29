from calendar import month_name
from dash.dcc import ConfirmDialogProvider
from dash.html.Legend import Legend
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

import numpy as np
from pivot_tables import *
from plots import *

app = Dash(__name__)
#themes: CYBORG, SLATE, SOLAR, SUPERHERO, FLATLY
server = app.server

date_df = date_table()
df = create_data("data\denormalized-data.xlsx")

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
        html.Div(
            className = "checklist",
            children=[
                html.P("Delivery Mode"),
                dcc.Checklist(
                    id="delivery-mode",
                    options=[{"label":mode, "value":mode} for mode in df["Delivery Mode"].unique()],
                    labelStyle={"display":"block"}
                )
            ]
        ),
        html.Div(
            className = "checklist",
            children=[
                html.P("Segment"),
                dcc.Checklist(
                    id="cust-segment",
                    options=[{"label":segment, "value":segment} for segment in df["Customer Segment"].unique()],
                    labelStyle={"display":"block"}
                )
            ] 
        ),
        html.Div(
            className = "checklist",
            children=[
                html.P("Region"),
                dcc.Checklist(
                    id="region",
                    options=[{"label":region, "value":region} for region in df["Region"].unique()],
                    labelStyle={"display":"block"}
                )
            ] 
        ),
        html.Div(
            className = "checklist",
            children=[
                html.P("Category"),
                dcc.Checklist(
                    id="prod-category",
                    options=[{"label":category, "value":category} for category in df["Product Category"].unique()],
                    labelStyle={"display":"block"}
                )
            ] 
        ),
        html.Div(
            className = "checklist",
            children=[
                html.P("Sub-Category"),
                dcc.Checklist(
                    id="sub-category",
                    options=[{"label":sub, "value":sub} for sub in df["Sub-Category"].unique()],
                    labelStyle={"display":"block"}
                )
            ] 
        ),
        html.Div(
            className = "checklist",
            children=[
                html.P("Selector"),
                dcc.Checklist(
                    id="selector",
                    options=[{"label":option, "value":option} for option in df["Selector"].unique()],
                    labelStyle={"display":"block"}
                )
            ] 
        )
    ]
)

timeline = html.Div(
    id="timeline",
    children=[
        html.P("Select Date"),
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
            id="data-store",
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
    Output(component_id="data-store", component_property="data"),
    [Input(component_id="year-picker", component_property="value"),
    Input(component_id="period-picker", component_property="value"),
    Input(component_id="time-slider", component_property="value"),
    Input(component_id="delivery-mode", component_property="value"),
    Input(component_id="cust-segment", component_property="value"),
    Input(component_id="region", component_property="value"),
    Input(component_id="prod-category", component_property="value"),
    Input(component_id="sub-category", component_property="value"),
    Input(component_id="selector", component_property="value")
    ]
)

def create_filtered_data(year, period, time, delivery, segment, region, category, subcategory, selector):
    df = create_data("data\denormalized-data.xlsx")
    
    time = [i for i in range(min(time), max(time)+1)]
    period = "".join(period)
    df = df[df["Years"].isin(year)]
    df = df[df[period].isin(time)]

    if delivery:
        df = df[df["Delivery Mode"].isin(delivery)]
    elif segment:
        df = df[df["Customer Segment"].isin(segment)]
    elif region:
        df = df[df["Region"].isin(region)]
    elif category:
        df = df[df["Product Category"].isin(category)]
    elif subcategory:
        df = df[df["Sub-Category"].isin(subcategory)]
    elif selector:
        df = df[df["Selector"].isin(selector)]
    
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
    Output(component_id="p-margin", component_property="children"),
    Output(component_id="trend-line", component_property="figure"),
    Output(component_id="matrix-chart", component_property="figure")],
    Input(component_id="data-store", component_property="data")
    
)

def create_charts(data):
    df = data

    revenue = df["Revenue"]
    cost = df["Cost"]
    profit = df["Profit"]
    p_margin = sum(profit)/sum(revenue)

    revenue = "{:,}".format(sum(revenue))
    cost = "{:,}".format(sum(cost))
    profit = "{:,}".format(sum(profit))
    p_margin = "{:.2%}".format(p_margin)

    trends_df = trend_pivot(df)
    trend_fig = trend(trends_df)

    sub_category_df = sub_category_pivot(df)
    matrix_chart = matrix(sub_category_df)

    #regions_df = region_pivot(df)
    
    return revenue, cost, profit, p_margin, trend_fig, matrix_chart
    



if __name__ == '__main__':
    app.run_server(debug=True)