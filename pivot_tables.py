import numpy as np
import pandas as pd
import openpyxl
import calendar

def create_data(path):
    df = pd.read_excel(path)
    df["Revenue"] = df["Quantity"] * df["Selling price"]

    df["Cost"] = df["Quantity"] * df["Unit cost"]
    df["Profit"] = df["Revenue"] - df["Cost"]
    df["Profit Margin"] = df["Profit"]/df["Revenue"]

    df["Years"] = df["Delivery Date"].dt.year
    df["Months"] = df["Delivery Date"].dt.month
    df["Quarters"] = df["Delivery Date"].dt.quarter
    df["Days"] = df["Delivery Date"].dt.day
    df["Selector"] = np.where(df["Discount"]>0, "Discount", "No Discount")

    return df


def trend_pivot(df):
    df = pd.DataFrame(df)
    months = pd.to_datetime(df["Order Date"]).dt.month
    try:
        months = months.apply(lambda x: calendar.month_abbr[x])
    except(TypeError):
        months = months

    order = calendar.month_abbr
    trend_df = df.groupby([months])[["Revenue", "Cost", "Profit"]].sum()
    trend_df["Profit Margin"] = trend_df["Profit"]/trend_df["Revenue"]
    trend_df = trend_df.reindex(order, axis=0)
    trend_df.dropna(inplace=True)
    trend_df = trend_df.reset_index()
    return trend_df

def region_pivot(df):
    df = pd.DataFrame(df)
    regions_df = df.groupby('Region')["Profit"].sum().sort_values(ascending=False)
    regions_df = regions_df.reset_index()
    regions_df["Region"] = regions_df["Region"].str.replace("Brong-Ahafo", "Brong Ahafo")
    return regions_df

def sub_category_pivot(df):
    df = pd.DataFrame(df)
    sub_category_df = df.groupby('Sub-Category')[["Revenue", "Cost", "Profit"]].sum().sort_values(by="Revenue",ascending=False)
    sub_category_df["PM Tracker"] = sub_category_df["Profit"]/sub_category_df["Revenue"]
    sub_category_df.drop("Profit",axis=1, inplace=True)

    sub_category_df.loc['Grand Total'] = sub_category_df[["Revenue", "Cost"]].sum()
    sub_category_df["PM Tracker"].loc['Grand Total'] = sub_category_df["PM Tracker"].mean()
    sub_category_df = sub_category_df.reset_index()

    # sub_category_df["Revenue"] = sub_category_df["Revenue"].apply(lambda x: "{:,.1f}k".format((x/1000)))
    # sub_category_df["Cost"] = sub_category_df["Cost"].apply(lambda x: "{:,.1f}k".format((x/1000)))

    sub_category_df["PM Tracker"] = sub_category_df["PM Tracker"].apply(lambda x: '⭐' if x<0.2
        else '⭐⭐' if x<0.25
        else '⭐⭐⭐')

    return sub_category_df


def date_table(start='2018-01-01', end='2019-12-31'):
    date_df = pd.DataFrame({"Date": pd.date_range(start, end)})
    date_df["Days"] = date_df.Date.dt.day
    date_df["Months"] = date_df.Date.dt.month
    date_df["Quarters"] = date_df.Date.dt.quarter
    date_df["Years"] = date_df.Date.dt.year
    return date_df

