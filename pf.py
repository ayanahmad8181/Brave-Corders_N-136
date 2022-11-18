from pandas_profiling import ProfileReport
import pandas as pd


def generate_report(df):
    pro = ProfileReport(df)
    pro.to_file("output.html")


# generate_report()
