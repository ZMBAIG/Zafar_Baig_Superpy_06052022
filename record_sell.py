
from rich.console import Console
console = Console()
import os
from os import system
import sys
import fileinput
import csv
import argparse
from datetime import date
from tabular_data import print_table


# Declaring a number of variables for different files that are finally stored in a directory of "supermarket_data" with file extension of csv. As a new product with  purchase or sold registered in the inventory, these files are updated with relvent information. 

to_get_full_path_directory =   os.path.realpath(__file__)
to_create_files_directory =    os.path.dirname(to_get_full_path_directory)
to_get_directory_path =        os.path.join(to_create_files_directory, "supermarket_data")
to_get_inventory_file =        os.path.join(to_get_directory_path,     "inventory_report.csv")
to_get_expire_dates_file =     os.path.join(to_get_directory_path,     "expired_products.csv")
to_get_product_buy_file =      os.path.join(to_get_directory_path,     "bought_products.csv")
product_sales_file =           os.path.join(to_get_directory_path,     "sold_products.csv")


get_argparser = argparse.ArgumentParser()
def sell(product_id, product_sold_date, product_sold_price):
    if product_sold_date == "None":
        product_sold_date = str(date.today())
    console.print("\n [bold italic blue on light_green]Product Specification[/]\n")
    print(f" Product ID: \t{product_id}")
    print(f" Sold Date: \t{product_sold_date}")
    print(f" Sold Price: \t€{product_sold_price}")
    sold_message = ""
    total_sales = 0.0

    with fileinput.input(files=to_get_inventory_file, inplace=True, mode='r') as file:
        reader =csv.DictReader(file)
        print(",".join(reader.fieldnames))  
        for row in reader:
            if row["Product ID"] ==     product_id and row["Stock Update"] == "NA":
                row["Sold Date"] =      product_sold_date
                row["Sold Price(€)"]=   product_sold_price
                row["Stock Update"] =   "Sold out"
                sold_message =          "has been sold.."
                product =               row["Product Name"]
                buy_date =              row["Buying Date"]
                buy_quantity =          row["Count"]
                product_buy_price =     row["Buying Price(€)"]
                product_id2 =           product_id
                product_sold_date2 =    product_sold_date
                product_sold_price2 =   product_sold_price
                stock_status2 =         "Sold out"
                product2 =              product
                buy_date2 =             buy_date
                buy_quantity2 =         buy_quantity
                product_buy_price2 =    product_buy_price
                stock_status =          "Sold out"
            else:
                pass
            print(",".join([
                row["Product ID"], 
                row["Product Name"],
                row["Buying Date"], 
                row["Count"],
                row["Buying Price(€)"],
                row["Expiration Date"],
                row["Sold Date"],
                row["Sold Price(€)"],
                row["Stock Update"]]))

    if sold_message == "has been sold..":
        with fileinput.input(files=product_sales_file, inplace=True, mode='r') as file:
            reader = csv.DictReader(file)
            print(",".join(reader.fieldnames))  
            print(",".join([product_id2, 
                product2, 
                buy_date2, 
                buy_quantity2, 
                product_buy_price2, 
                product_sold_date2, 
                product_sold_price2, 
                stock_status2])) 
            total_sales += float(product_sold_price2)
            for row in reader:
                print(",".join([row["Product ID"], 
                row["Product Name"], 
                row["Buying Date"], 
                row["Count"],
                row["Buying Price(€)"],
                row["Sold Date"], 
                row["Sold Price(€)"], 
                row["Stock Update"]]))
                total_sales += float(row["Sold Price(€)"])
    else:
        pass

    if sold_message == "has been sold..":
        print(f"\nAn item with ID {product_id} {sold_message}", file=sys.stdout)
        total_sales = round(total_sales, 3)
        print(f'\nNow Total Price of Sold items: \t€{total_sales}', file=sys.stdout)
        console.print("\n\t\t\t\t [bold red on white]Summary of Sold Products:[/]")
        print_table(product_sales_file)
    else:
        print(f'\nNo Transaction for suggested ID {product_id}.(For verification! Please check "Stock Update" in inventory report).\n\n', file=sys.stdout)
    return

