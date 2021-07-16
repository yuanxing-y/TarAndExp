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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    turnaround_df = pd.read_csv(f"offlineEvents-2021-07-15.csv")
    unit_map = pd.read_excel(f"iir_name_mapping.xlsx", sheet_name="IirUnit_NameMirror")
    map = unit_map[['UNIT_NAME','UnitGrpSimple']]
    dict = map.set_index("UNIT_NAME")["UnitGrpSimple"].to_dict()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
