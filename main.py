import pandas as pd
import xlrd
import numpy as np
import matplotlib.pyplot as plt


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def clean_df(df):
    return df.dropna(how='all', axis=1)  # Drop Column Only if All the Values are Null


def get_dict(map_df):
    simple_dict = map_df.set_index("UNIT_NAME")["UnitGrpSimple"].to_dict()
    return simple_dict


def processed_df(turnaround_df, simple_dict):  # add additional three column
    # df = clean_df(turnaround_df)
    df = turnaround_df.copy()
    df['UnitGrpSimple'] = df['UNIT_NAME'].map(simple_dict)
    df['SMN'] = pd.to_datetime(df['START_DATE']).dt.strftime('%Y%m')
    df['EMN'] = pd.to_datetime(df['END_DATE']).dt.strftime('%Y%m')
    return df


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
    turnaround_df = pd.read_csv(f"offlineEvents-2021-07-15.csv")
    unit_map = pd.read_excel(f"iir_name_mapping.xlsx", sheet_name="IirUnit_NameMirror")
    simple_dict = get_dict(unit_map)
    df = processed_df(turnaround_df, simple_dict)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
