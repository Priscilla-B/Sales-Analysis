import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash_table as dt
import numpy as np
import pandas as pd
import json

def trend(df):
    trend_fig = make_subplots(specs=[[{"secondary_y": True}]])
    trend_fig.add_trace(
        go.Bar(
            x=df["Order Date"], y=df["Revenue"],
            name = "Revenue"
        ),
        secondary_y = False
    )
    trend_fig.add_trace(
        go.Bar(
            x=df["Order Date"], y=df["Cost"],
            name = "Cost"
        ),
        secondary_y = False
    )
    trend_fig.add_trace(
        go.Bar(
            x=df["Order Date"], y=df["Profit"],
            name = "Profit"
        ),
        secondary_y = False
    )

    trend_fig.add_trace(
        go.Scatter(
            x=df["Order Date"], y=df["Profit Margin"],
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
            x=0.1,
            font= dict(size = 9)
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"

    )
    return trend_fig

# def matrix(df):

    # matrix_fig = go.Figure(data = [go.Table(
    #     columnwidth=[120, 60, 60, 80],
    #     header = dict(values=list(df.columns),
    #                 fill_color="gray",
    #                 line_color="gray",
    #                 font = dict(color="white", size=10),
    #                 height=22,
    #                 align="left"),
    #     cells =  dict(values=df.T, 
    #                 fill_color="white",
    #                 line = dict(color="gray", width=None),
    #                 font = dict(color="black", size=8),
    #                 height = 16,
    #                 align="left")
    # )])

    # matrix_fig.update_layout(
    #     autosize=True,
    #     margin=dict(
    #         l=10,
    #         r=50,
    #         b=10,
    #         t=10,
    #         pad=4
    #     )
    # )
    # return matrix_fig

def create_map(df):
    ghana_geo = json.load(open("ghana_regions.json","r"))
    for feature in ghana_geo["features"]:
        feature["id"] = feature["properties"]["NAME_1"]

    map_fig = go.Figure()
    labels = df["Profit"].apply(lambda x: "{:,.1f}k".format((x/1000)))
    colors = np.where(df["Profit"]>300000,"rgb(3, 127, 62)", np.where(
        df["Profit"]>100000,"rgb(53, 103, 157)", "rgb(214, 12, 12)"))

    map_fig.add_trace(go.Choropleth(
        geojson = ghana_geo,
        locations = df["Region"],
        featureidkey = "id",
        locationmode = "geojson-id",
        z = df["Profit"],
        autocolorscale = False,
        colorscale = [[0,'rgb(255, 255, 255)'],[1,'rgb(255, 255, 255)']],
        showscale = False
    ))

    map_fig.add_trace(go.Scattergeo(
        geojson = ghana_geo,
        locations =df["Region"],
        featureidkey = "id",
        locationmode = "geojson-id",
        mode = "markers+text",
        text = labels,
        marker = dict(
                    size = df["Profit"]/10000,
                    line_width = 0,
                    color = colors
                )
    ))

    map_fig.update_layout(
        autosize=False,
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=0,
            autoexpand = True
        ),
        width = 400,
        height = 450,
        geo = go.layout.Geo(
            fitbounds = "geojson",
            visible = False,
            projection = dict(
                type = "gnomonic"
                # "stereographic" "gnomonic"
            )
        )
    )
    

    return map_fig

