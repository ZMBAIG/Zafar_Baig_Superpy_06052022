
# In this section a pre-defined stock.csv generates the following files; inventry.csv, bought_products.csv, expired_products.csv and sold_products.csv in a structured folder of "supermarket_data". Every record in these files consist of a unique_id that describes the required reporting.

import os
import csv
from make_directory import make_directory_folder
from decimal import Decimal
import math
from product_unique_id import unique_id
# defining a class
class StockEstablish():
    def __init__(self):
        dir_path = make_directory_folder("supermarket_data")                                 
        product_id = 0
        self.dir_path =             dir_path
        stock_file =                os.path.join(dir_path, "stock.csv")                               
        superpy_inventory_file =    os.path.join(dir_path, "inventory_report.csv")
        to_get_expire_dates_file =  os.path.join(dir_path, "expired_products.csv")
        to_get_product_buy_file =   os.path.join(dir_path, "bought_products.csv")
        product_sales_file =        os.path.join(dir_path, "sold_products.csv")

        if os.path.isfile(stock_file):
            with open(stock_file, newline='') as csvfile:
                reader =                    csv.DictReader(csvfile)
                for row in reader:
                    product_id =            row['product_id']
                    product =               row['product']
                    buy_date =              row["buy_date"]
                    amount =                float(row['buy_quantity'])
                    amount_round =          round(amount,0)
                    amount_round =          math.ceil(amount_round)
                    product_buy_price =     float(row["product_buy_price"])
                    expiration_date =       row["expiration_date"]
                    product_sold_date =     row["sold_date"]
                    product_sold_price =    float(row["sold_price"])
                    exit_status =           row["stock_status"]
                    product_id =            unique_id(amount_round, expiration_date, buy_date)        
                    if os.path.isfile(superpy_inventory_file):
                        with open(superpy_inventory_file, 'a', newline='') as csvfile:
                            table_headers = (
                                "Product ID",
                                "Product Name",
                                "Buying Date",
                                "Count",
                                "Buying Price(€)",
                                "Expiration Date",
                                "Sold Date",
                                "Sold Price(€)",
                                "Stock Update")
                            writer = csv.DictWriter(csvfile, fieldnames=table_headers)
                            writer.writerow({
                                "Product ID":       product_id,
                                "Product Name":     product,
                                "Buying Date":      buy_date,
                                "Count":            amount,
                                "Buying Price(€)":  product_buy_price,
                                "Expiration Date":  expiration_date,
                                "Sold Date":        product_sold_date,
                                "Sold Price(€)":    product_sold_price, 
                                "Stock Update":     exit_status})
                    else:
                        with open(superpy_inventory_file, 'w', newline='') as csvfile:
                            table_headers = (
                                "Product ID",
                                "Product Name",
                                "Buying Date",
                                "Count",
                                "Buying Price(€)",
                                "Expiration Date",
                                "Sold Date",
                                "Sold Price(€)",
                                "Stock Update")
                            writer = csv.DictWriter(csvfile, fieldnames=table_headers)
                            writer.writeheader()
                            writer.writerow({
                                "Product ID":       product_id,
                                "Product Name":     product,
                                "Buying Date":      buy_date,
                                "Count":            amount,
                                "Buying Price(€)":  product_buy_price,
                                "Expiration Date":  expiration_date, 
                                "Sold Date":        product_sold_date,
                                "Sold Price(€)":    product_sold_price,
                                "Stock Update":     exit_status})

                    if os.path.isfile(product_sales_file):      
                        with open(product_sales_file, 'a', newline='') as csvfile:
                            table_headers = [
                                "Product ID",
                                "Product Name",
                                "Buying Date",
                                "Count",
                                "Buying Price(€)",
                                "Sold Date",
                                "Sold Price(€)",
                                "Stock Update"]
                            writer = csv.DictWriter(csvfile, fieldnames=table_headers)
                            if row["stock_status"] == "Sold out":        
                                
                                writer.writerow({
                                 "Product ID":      product_id,
                                 "Product Name":    product,
                                 "Buying Date":     buy_date,
                                 "Count":           amount,
                                 "Buying Price(€)": product_buy_price,
                                 "Sold Date":       product_sold_date,
                                 "Sold Price(€)":   product_sold_price,
                                 "Stock Update":    exit_status})
                    else :                             
                        with open(product_sales_file, 'w', newline='') as csvfile:
                            table_headers = [
                                "Product ID",
                                "Product Name",
                                "Buying Date",
                                "Count",
                                "Buying Price(€)",
                                "Sold Date",
                                "Sold Price(€)",
                                "Stock Update"]
                            writer = csv.DictWriter(csvfile, fieldnames=table_headers)
                            writer.writeheader()
                            if row["stock_status"] == "Sold out":       
                                
                                writer.writerow({
                                 "Product ID":      product_id,
                                 "Product Name":    product,
                                 "Buying Date":     buy_date,
                                 "Count":           amount,
                                 "Buying Price(€)": product_buy_price,
                                 "Sold Date":       product_sold_date,
                                 "Sold Price(€)":   product_sold_price,
                                 "Stock Update":    exit_status})

                    if os.path.isfile(to_get_product_buy_file):
                        with open(to_get_product_buy_file, 'a', newline='') as csvfile:
                            table_headers = (
                                "Product ID",
                                "Product Name",
                                "Buying Date",
                                "Count",
                                "Buying Price(€)",
                                "Expiration Date",
                                "Sold Date",
                                "Sold Price(€)",
                                "Stock Update")
                            writer = csv.DictWriter(csvfile, fieldnames=table_headers)
                            writer.writerow({
                                "Product ID":       product_id,
                                "Product Name":     product,
                                "Buying Date":      buy_date,
                                "Count":            amount,
                                "Buying Price(€)":  product_buy_price,
                                "Expiration Date":  expiration_date, 
                                "Sold Date":        product_sold_date,
                                "Sold Price(€)":    product_sold_price,
                                "Stock Update":     exit_status})
                    else:
                        with open(to_get_product_buy_file, 'w', newline='') as csvfile:
                            table_headers = (
                                "Product ID",
                                "Product Name",
                                "Buying Date",
                                "Count",
                                "Buying Price(€)",
                                "Expiration Date",
                                "Sold Date",
                                "Sold Price(€)",
                                "Stock Update")
                            writer = csv.DictWriter(csvfile, fieldnames=table_headers)
                            writer.writeheader()
                            writer.writerow({
                                "Product ID":       product_id,
                                "Product Name":     product,
                                "Buying Date":      buy_date,
                                "Count":            amount,
                                "Buying Price(€)":  product_buy_price,
                                "Expiration Date":  expiration_date,
                                "Sold Date":        product_sold_date,
                                "Sold Price(€)":    product_sold_price,
                                "Stock Update":     exit_status})

                    if os.path.isfile(to_get_expire_dates_file):
                        pass
                    else:
                        with open(to_get_expire_dates_file, 'w', newline='') as csvfile:
                            table_headers = (
                                "Product ID",
                                "Product Name",
                                "Buying Date",
                                "Buying Price(€)",
                                "Expiration Date",
                                "Stock Update")
                            writer = csv.DictWriter(csvfile, fieldnames=table_headers)
                            writer.writeheader()

