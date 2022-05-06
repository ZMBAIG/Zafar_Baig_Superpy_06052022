from rich.console import Console
console = Console()
import os
import sys
import fileinput
import csv
import math
from datetime import date, timedelta, datetime
from tkinter.ttk import Style


to_get_files_path =         os.path.realpath(__file__)
to_create_files_directory = os.path.dirname(to_get_files_path)
to_get_directory_path =     os.path.join(to_create_files_directory, "supermarket_data")
to_get_inventory_file =     os.path.join(to_get_directory_path,     "inventory_report.csv")
to_get_expire_dates_file =  os.path.join(to_get_directory_path,     "expired_products.csv")

# To get a schedule of different dates for certain events like expire, a function is defined that helps to add or subtract number of days with respect to current date(today).

def to_acquire_expired_report_today(current_date, number_of_days):             
    report = []
    number_of_days = number_of_days                                   
    table_headers = ["Product ID",
                    "Product Name",
                    "Count",
                    "Expiration Date",
                    "Stock Update"]
    report.append(table_headers)
    os.remove(os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)),
     "supermarket_data"), 
     "expired_products.csv"))

    with fileinput.input(files=to_get_inventory_file, inplace=True, mode='r') as file:     
        reader = csv.DictReader(file)
        print(",".join(reader.fieldnames))                                          
        for row in reader:
            check_expire_date =     row["Expiration Date"]
            product_expire_date =   date.fromisoformat(check_expire_date)
            stock_status =          row["Stock Update"]
            if stock_status !=      "Expired" and stock_status != "Sold out":
                if current_date > product_expire_date:
                    row["Stock Update"] = "Expired"
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
                    report.append([
                     row["Product ID"],
                     row["Product Name"],
                     row["Count"],
                     row["Expiration Date"],"Expired"])
                else:
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
            else:
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

    file = open(to_get_expire_dates_file, 'w+', newline="")                                      
    with file:
        write = csv.writer(file)
        write.writerows(report)
    return report

def to_get_expire_report_processed(process_date, number_of_days):             
    if process_date == "None":
        process_date = str(date.today())
    report = []
    buy_lost = 0.0
    os.remove(os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), "supermarket_data"), 
    "expired_products.csv"))
    process_date = date.fromisoformat(str(process_date))
    maximum_date = process_date + timedelta(days=number_of_days)
    table_headers = [
        "Product ID",
        "Product Name",
        "Count",
        "Buying Price(€)",
        "Expiration Date",
        "Stock Update"]
    report.append(table_headers)
    console.print(f"\n [bold white on green]Transaction Scheduled Till[/] [blink]{maximum_date}\n")
    with fileinput.input(files=to_get_inventory_file, inplace=False, mode='r') as file: 
        reader = csv.DictReader(file)

        for row in reader:
            check_expire_date =     row["Expiration Date"]
            product_sold_date =     row["Sold Date"]
            stock_status =          row["Stock Update"]
            buy_date =              row["Buying Date"]
            product_buy_date =      date.fromisoformat(buy_date)
            product_expire_date =   date.fromisoformat(check_expire_date)
            if product_sold_date == "0":
                product_sold_date = date.fromisoformat("4999-01-01")
            else:
                product_sold_date = date.fromisoformat(product_sold_date)


            if product_sold_date <= maximum_date:
                console.print (f"Product ID: {row['Product ID']}\t({row['Product Name']})\t\tis\t[bright_blue]SOLD OUT[/].")

            else:
                if product_buy_date >= maximum_date:
                    print (f"Product ID: {row['Product ID']}\t({row['Product Name']})\t\tis\t.")
                else:
                    if maximum_date > product_expire_date:
                        row["Stock Update"] = "Product Expired"
                        report.append([
                        row["Product ID"], 
                        row["Product Name"], 
                        row["Count"], 
                        row["Buying Price(€)"], 
                        row["Expiration Date"],
                        row["Stock Update"]])
                        expiration_date = row["Expiration Date"]
                        buy_lost += float(row["Buying Price(€)"])
                        console.print(f"Product ID: {row['Product ID']}\t([underline red]{row['Product Name']}[/])\tis\t[red]EXPIRED...[/]")
                    else:
                        console.print(f"Product ID: {row['Product ID']}\t({row['Product Name']})\t\tis\t[light_green]VALID UNTIL\:[/][red]({product_expire_date})[/]")


    file = open(to_get_expire_dates_file, 'w+', newline="")     
    with file:
        write = csv.writer(file)
        write.writerows(report)
    
    from tabular_data import print_table
    print_table(to_get_expire_dates_file)            
    console.print(f"\n [red]Loss on Expired Products (Buying Price):[/] €{buy_lost}")
    
    return report



