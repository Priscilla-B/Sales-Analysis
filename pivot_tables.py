import pandas as pd
import openpyxl
import calendar

def create_data(path):
    df = pd.read_excel(path)
    df["Revenue"] = df["Quantity"] * df["Selling price"]

    df["Cost"] = df["Quantity"] * df["Unit cost"]
    df["Profit"] = df["Revenue"] - df["Cost"]
    df["Profit Margin"] = df["Profit"]/df["Revenue"]

    return df


def trend_pivot(df):
    months = df["Order Date"].dt.month
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
    regions_df = df.groupby('Region')["Profit"].sum().sort_values(ascending=False)
    regions_df = regions_df.reset_index()
    return regions_df

def sub_category_pivot(df):
    sub_category_df = df.groupby('Sub-Category')[["Revenue", "Cost", "Profit"]].sum().sort_values(by="Revenue",ascending=False)
    sub_category_df = sub_category_df.reset_index()
    sub_category_df["Profit Margin"] = sub_category_df["Profit"]/sub_category_df["Revenue"]
    sub_category_df.drop("Profit",axis=1, inplace=True)
    return sub_category_df
