
from rich.console import Console
console = Console()
import os
import sys
import fileinput
import csv
from product_unique_id import unique_id
from tabular_data import print_table

# This section belongs to a number of questions asked for the registration of buying a product. It makes sure the right product is going to be entering manually, with relevant attributes e.g. Product Name, Buying Date, Price, Expiration Date etc .etc. In this way the command line tool helps and enhance to store all the attributes of inventory item.

to_get_files_path =         os.path.realpath(__file__)
to_create_files_directory = os.path.dirname(to_get_files_path)
to_get_directory_path =     os.path.join(to_create_files_directory, "supermarket_data")
to_get_inventory_file =     os.path.join(to_get_directory_path,     "inventory_report.csv")
to_get_expire_dates_file =  os.path.join(to_get_directory_path,     "expired_products.csv")
to_get_product_buy_file =   os.path.join(to_get_directory_path,     "bought_products.csv")

def to_get_buy_items_input():# To buy or register a product an input data questions.
    input_tag_message = "no"
    while input_tag_message != "yes":
        product = input("Please Enter Product\'s Name: (e.g. Banana) ")
        input_tag_message = console.input(f"Is Product\'s Name '{product}' [magenta] perfect[/] (yes/no/quit):")
        if input_tag_message == "quit":
            return
    console.print (f"[green]Ok[/] This is {product}.\n[yellow]==============================================================[/]")
    input_tag_message = "no"
    while input_tag_message != "yes":
        buy_date = str(input("Enter Date of Buying: (e.g. 2022-01-01) "))
        input_tag_message = console.input(f"Is Date of Buying '{buy_date}' [magenta] perfect[/] (yes/no/quit):")
        if input_tag_message == "quit":
            return
    console.print (f"[green]Ok[/] This is {buy_date}.\n[yellow]==============================================================[/]")

    input_tag_message = "no"
    while input_tag_message != "yes":
        buy_quantity = str(input("Enter Product Amount: (Please a number, e.g. 12) "))
        input_tag_message = console.input(f"Is Quantity of Product '{buy_quantity}' [magenta] perfect[/] (yes/no/quit):")
        if input_tag_message == "quit":
            return
    console.print (f"[green]Ok[/] This is {buy_quantity}.\n[yellow]==============================================================[/]")

    input_tag_message = "no"
    while input_tag_message != "yes":
        product_buy_price = str(input("Enter Buying Price: (Please a number, e.g. 3.99) "))
        input_tag_message = console.input(f"Is Product Price '{product_buy_price}' [magenta] perfect[/] (yes/no/quit):")
        if input_tag_message == "quit":
            return
    console.print (f"[green]Ok[/] This is {product_buy_price}.\n[yellow]==============================================================[/]")

    input_tag_message = "na"
    while input_tag_message != "yes":
        expiration_date = input("Enter Expiration Date: (e.g. 2022-01-01) ")
        input_tag_message = console.input(f"Is Expiration Date'{expiration_date}' [magenta] perfect[/] (yes/no/quit):")
        if input_tag_message == "quit":
            return
    console.print (f"[green]Ok[/] This is {expiration_date}.\n[yellow]==============================================================[/]")

    product_id = str(unique_id(buy_quantity, expiration_date, buy_date))
    product_sold_date = "0"
    product_sold_price = "0.0"
    stock_status = "NA" # This means the product status is Not Available(NA).
    full_input_buy = (product_id, 
                    product,
                    buy_date,
                    buy_quantity,
                    product_buy_price,
                    expiration_date,
                    product_sold_date,
                    product_sold_price,
                    stock_status)
    return full_input_buy

console.print("\nPlease register the required items with respect to their Product Name, Buying Date, Amount, Price and Expiration Date.\n",style="bold white on blue3")

get_schedule = console.input("\n[bold magenta]Would you like to execute this program?(yes/no):[/] ")
if get_schedule == "yes":
    buy = to_get_buy_items_input()
else:
    buy = ("3652", 'Soap', '2022-01-02', '25.0', '2.50', '2022-12-30', 'n', '0', '0.0', 'NA')            

table_headers = ("Product ID",
                "Product Name",
                "Buying Date",
                "Count",
                "Buying Price(€)",
                "Expiration Date",
                "Sold Date",
                "Sold Price(€)",
                "Stock Update")

with fileinput.input(files=to_get_product_buy_file, inplace=True, mode='r') as file:
    reader= csv.DictReader(file)
    print(",".join(reader.fieldnames)) 
    print(",".join(buy))
    for row in reader:
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

with fileinput.input(files=to_get_inventory_file, inplace=True, mode='r') as file:
    reader= csv.DictReader(file)
    print(",".join(reader.fieldnames))  
    print(",".join(buy))
    for row in reader:
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

get_buy_expire_data = list(buy)
get_buy_expire_data.remove(get_buy_expire_data[7])    # It will remove the index value of product_sold_price.
get_buy_expire_data.remove(get_buy_expire_data[6])    # It will remove the index value of product_sold_date.
get_buy_expire_data.remove(get_buy_expire_data[3])    # It will remove index value of buy_quantity.

get_buy_expire_data = tuple(get_buy_expire_data)

with fileinput.input(files=to_get_expire_dates_file, inplace=True, mode='r') as file:
    reader= csv.DictReader(file)
    print(",".join(reader.fieldnames))  
    print(",".join(get_buy_expire_data))
    for row in reader:
        print(",".join([
            row["Product ID"], 
            row["Product Name"],
            row["Count"],
            row["Expiration Date"],
            row["Stock Update"]]))

console.print(f"These are Updated Directory Folders:\n\n"
      f"{to_get_product_buy_file}\n"
      f"{to_get_inventory_file}\n"
      f"{to_get_expire_dates_file}\n\n"
      f"[blink white on red bold]Registration Ended. Please Enter a New Product[/]")

print_table(to_get_product_buy_file) 
