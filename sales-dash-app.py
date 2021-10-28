from calendar import month_name
from dash.html.Legend import Legend
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

import numpy as np
from pivot_tables import *

app = Dash(__name__)
#themes: CYBORG, SLATE, SOLAR, SUPERHERO, FLATLY
server = app.server

df = create_data("data\denormalized-data.xlsx")
trends_df = trend_pivot(df)
regions_df = region_pivot(df)
sub_category_df = sub_category_pivot(df)
date_df = date_table()
#trend_fig = px.line(trends_df, x="Order Date", y="Profit Margin")
#trend_fig.add_bar(x=trends_df["Order Date"], y=trends_df["Revenue"])
#trend_fig = go.Figure()
trend_fig = make_subplots(specs=[[{"secondary_y": True}]])
trend_fig.add_trace(
    go.Bar(
        x=trends_df["Order Date"], y=trends_df["Revenue"],
        name = "Revenue"
    ),
    secondary_y = False
)

trend_fig.add_trace(
    go.Bar(
        x=trends_df["Order Date"], y=trends_df["Cost"],
        name = "Cost"
    ),
    secondary_y = False
)
trend_fig.add_trace(
    go.Bar(
        x=trends_df["Order Date"], y=trends_df["Profit"],
        name = "Profit"
    ),
    secondary_y = False
)

trend_fig.add_trace(
    go.Scatter(
        x=trends_df["Order Date"], y=trends_df["Profit Margin"],
        name = "Profit Margin",
    ),
    secondary_y = True
)
trend_fig.update_layout(
    autosize=True,
    margin=dict(
        l=10,
        r=50,
        b=10,
        t=10,
        pad=4
    ),
    legend=dict(
        yanchor="bottom",
        xanchor="left",
        orientation='h',
        y=1.02,
        x=0.1
    ),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"

)

matrix_fig = go.Figure(data = [go.Table(
    columnwidth=[120, 60, 60, 60],
    header = dict(values=list(sub_category_df.columns),
                fill_color="gray",
                line_color="gray",
                font = dict(color="white", size=12),
                height=25,
                align="left"),
    cells =  dict(values=sub_category_df.T, 
                fill_color="white",
                line = dict(color="gray", width=None),
                font = dict(color="black", size=10),
                height = 19,
                align="left")
)])

matrix_fig.update_layout(
    autosize=True,
    margin=dict(
        l=10,
        r=50,
        b=10,
        t=10,
        pad=4
    )
)



ghana_geo = pd.read_json("data/ghana_regions.json")


cards = html.Div(
    className="cards",
    children=[
        html.Div(
            className="card-item",
            children=[
                html.P("REVENUE", className="chart-title"),
                html.Hr(),
                html.P("{:,}".format(df['Revenue'].sum()), className="card-value", id="revenue")
            ]
                    ),
        html.Div(
            className="card-item",
            children=[
                html.P("COST", className="chart-title"),
                html.Hr(),
                html.P("{:,}".format(df['Cost'].sum()), className="card-value", id="cost")
            ]
        ),
        html.Div(
            className="card-item",
            children=[
                html.P("PROFIT", className="chart-title"),
                html.Hr(),
                html.P("{:,}".format(df['Profit'].sum()), className="card-value", id="profit")
                ]
            ),
        html.Div(
            className="card-item",
            children=[
                html.P("PROFIT MARGIN", className="chart-title"),
                html.Hr(),
                html.P("{:.2%}".format(df['Profit Margin'].mean()), className="card-value", id="p-margin")
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
                    id="trend-line",
                    figure=trend_fig)
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
                dcc.Graph(id="matrix-chart", figure = matrix_fig)
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
    Output(component_id="profit", component_property="children"),
    [Input(component_id="year-picker", component_property="value"),
    Input(component_id="period-picker", component_property="value"),
    Input(component_id="time-slider", component_property="value")]
    
)



def create_profit_value(year, period, time):
    df = create_data("data\denormalized-data.xlsx")
    df["Years"] = df["Delivery Date"].dt.year
    df["Months"] = df["Delivery Date"].dt.month
    df["Quarters"] = df["Delivery Date"].dt.quarter
    df["Days"] = df["Delivery Date"].dt.day

    time = [i for i in range(min(time), max(time)+1)]
    period = "".join(period)
    df = df[df["Years"].isin(year)]
    df = df[df[period].isin(time)]

    profit = df["Profit"]
    profit = "{:,}".format(profit.sum())
    
    return profit
    



if __name__ == '__main__':
    app.run_server(debug=True)