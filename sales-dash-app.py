from dash.html.Legend import Legend
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc


from pivot_tables import *

app = Dash(__name__)
#themes: CYBORG, SLATE, SOLAR, SUPERHERO, FLATLY
server = app.server

df = create_data("data\denormalized-data.xlsx")
trends_df = trend_pivot(df)
regions_df = region_pivot(df)
sub_category_df = sub_category_pivot(df)

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
                html.P("{:,}".format(df['Revenue'].sum()), className="card-value")
            ]
                    ),
        html.Div(
            className="card-item",
            children=[
                html.P("COST", className="chart-title"),
                html.Hr(),
                html.P("{:,}".format(df['Cost'].sum()), className="card-value")
            ]
        ),
        html.Div(
            className="card-item",
            children=[
                html.P("PROFIT", className="chart-title"),
                html.Hr(),
                html.P("{:,}".format(df['Profit'].sum()), className="card-value")
                ]
            ),
        html.Div(
            className="card-item",
            children=[
                html.P("PROFIT MARGIN", className="chart-title"),
                html.Hr(),
                html.P("{:.2%}".format(df['Profit Margin'].mean()), className="card-value")
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
                        html.Div(
                            className="timeline",
                            children=[]
                        )
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








if __name__ == '__main__':
    app.run_server(debug=True)