# pip install tabula
# pip install camelot  or  conda install -c conda-forge camelot-py

import openpyxl
import tabula
import camelot
import pandas
import sys

def export_table():
    # dfs = tabula.read_pdf('C:\\RPA\\TEST\\정보공개서\\정보공개서_꼬마숲어린이집.pdf', pages="35", stream=True)
    # print(f"Data Type :{type(dfs)}")
    # print(f"Data Length: {len(dfs)}")
    # for index, table in enumerate(dfs):
    #   print(f"\nData Index: {index}")
    #   print(type(table))
    #   print(table.head())
    # tabula.convert_into('C:\\RPA\\TEST\\정보공개서\\정보공개서_꼬마숲어린이집.pdf', 'C:\\RPA\\TEST\\정보공개서\\output.csv', output_format="csv", pages='35')

    tables = camelot.read_pdf('C:\\RPA\\TEST\\정보공개서\\정보공개서_꼬마숲어린이집.pdf', pages='35')
    print(tables)
    # for tabs in tables:
    #     print(tabs.df, "\n=================================\n")

if __name__ == '__main__':
    # asset_id_from_wd = sys.argv[1]
    # save_img_path_from_wd = sys.argv[2]
    export_table()