from rich.console import Console
console = Console()
import os
import sys
import fileinput
import csv
import math
from os import system, name
from tabular_data import print_table
from rich.prompt import Prompt


# This section gives a comprehensive report of the products with respect to Registered Number of items, Total Costs, Total Number of sales, Total Number of Expired Items and Current Profit Gain/Loss on Total Stock. 

count = 0
product_sales_price = 0.0
product_buy_price = 0.0
count_sold_product = 0
count_expired_product = 0
product_value_loss = 0.0
to_get_files_path =         os.path.realpath(__file__)
to_create_files_directory = os.path.dirname(to_get_files_path)
to_get_directory_path =     os.path.join(to_create_files_directory, "supermarket_data")
to_get_inventory_file =     os.path.join(to_get_directory_path,     "inventory_report.csv")
to_get_expire_dates_file =  os.path.join(to_get_directory_path,     "expired_products.csv")
to_get_product_buy_file =   os.path.join(to_get_directory_path,     "bought_products.csv")
product_sales_file =        os.path.join(to_get_directory_path,     "sold_products.csv")

with fileinput.input(files=to_get_inventory_file, inplace=False, mode='r') as file:
    reader =csv.DictReader(file)
    for row in reader:
        product_buy_price = product_buy_price + float(row["Buying Price(€)"])
        count += 1                                     
        if row["Sold Price(€)"] != "0.0":
            if row["Stock Update"] == "Sold out":
                product_sales_price = product_sales_price + float(row["Sold Price(€)"])
                count_sold_product += 1
        if row["Stock Update"] == "Expired":
                count_expired_product += 1
                product_value_loss += float(row["Buying Price(€)"])

print_table(to_get_inventory_file) # A comprehensive transaction of all the items collected in inventory report.e.g. investment, revenue, profit & loss in a stipulated calender.  
console.print("\n\n\t\t\t\t\t[overline yellow]Registered Number of Products in inventory:[/]\t ",count)
console.print("\t\t\t\t\t[overline magenta]Total Number of Expired Products(today):\t[/] ",count_expired_product)
console.print("\t\t\t\t\t[overline red]Loss on Expired Products (Buying Price):\t[/]€",product_value_loss)
print("\t\t\t\t\tTotal Cost of Buying Product(investment):\t€",round((product_buy_price),2))
print(f"\t\t\t\t\tTotal Cost of Sold-out Products ({count_sold_product}):\t\t€",round((product_sales_price), 2))
console.print("\t\t\t\t\t[underline light_green]Current profit Gain/Loss on total stock:[/] \t€",(round((product_sales_price-product_buy_price-product_value_loss),2)), "\n\n\n")

# name = Prompt.ask("\t\t\t\t\t\t\t" , default="Salesperson Name")


