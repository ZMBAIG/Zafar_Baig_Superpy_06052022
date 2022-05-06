import os
from shutil import copyfile
from os import path, makedirs
from csv import DictWriter
import shutil
from rich.console import Console
console = Console()


# To run this function, a number of different files with csv data are made and stored in "supermarket_data" directory with respect to their products attributes. These are derived from the original stock.csv data with requested fields and records. These folder directories are updated when main.py is first time executed.

def make_directory_folder(directory_name):  
    to_get_files_path =         os.path.realpath(__file__)
    to_create_files_directory = os.path.dirname(to_get_files_path)
    to_get_directory_path =     os.path.join(to_create_files_directory, directory_name)

    if not os.path.isdir(to_get_directory_path):
        os.makedirs(to_get_directory_path)

        console.print(f"\n A Directory as [overline]{directory_name} is created in {to_create_files_directory}[/]")# This will create a directory folder for all the csv data.                 

    shutil.copy("stock.csv", to_get_directory_path)


    stock_file = os.path.join(to_get_directory_path, "stock.csv")

    if not os.path.isfile("inventory_report.csv"):
        to_get_inventory_file = os.path.join(to_get_directory_path, "inventory_report.csv")

    if not os.path.isfile("expired_products.csv"):
        to_get_expire_dates_file = os.path.join(to_get_directory_path, "expired_products.csv")

    if not os.path.isfile("bought_products.csv"):
        to_get_product_buy_file = os.path.join(to_get_directory_path, "bought_products.csv")

    if not os.path.isfile("sold_products.csv"):
        product_sales_file = os.path.join(to_get_directory_path, "sold_products.csv")
    return to_get_directory_path



