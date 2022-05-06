import csv
import os
from os import system, name
from rich.console import Console
console = Console()

# To present a data for visualization a table format is selected. In this form different style color of text is selected from a rich library.

to_get_files_path =         os.path.realpath(__file__)
to_create_files_directory = os.path.dirname(to_get_files_path)
to_get_directory_path =     os.path.join(to_create_files_directory, "supermarket_data")
to_get_inventory_file =     os.path.join(to_get_directory_path,     "inventory_report.csv")
to_get_expire_dates_file =  os.path.join(to_get_directory_path,     "expired_products.csv")

def to_get_column_width(col, max_width):
    return col.ljust(max_width)

def print_table(print_file):  # Exhibit print_file in a table format
    print()
    with open(print_file) as csvfile:
        reader = csv.reader(csvfile)
        to_get_all_table_rows = []
        for row in reader:
            to_get_all_table_rows.append(row)

    max_column_width = [0] * len(to_get_all_table_rows[0])
    for row in to_get_all_table_rows:
        for product_id_x, col in enumerate(row):
            max_column_width[product_id_x] = max(len(col), max_column_width[product_id_x])
    table_count_row = 0
    table_empty_row = 0
    for row in to_get_all_table_rows:
        if table_count_row <= 1:                                  
            to_print = " "
            for product_id_x, col in enumerate(row):
                to_print += to_get_column_width(col, max_column_width[product_id_x]) + " | "
            console.print("-"*(len(to_print)-1),style="blue on white")
            console.print(to_print, style="yellow on black")
        else:
            if table_empty_row == 4:
                print()
                table_empty_row = 2
            else:
                table_empty_row += 6
            to_print = " "                                  
            for product_id_x, col in enumerate(row):
                to_print += to_get_column_width(col, max_column_width[product_id_x]) + " | "
            
            console.print(to_print, style="light_green")
        table_count_row += 1
    console.print("="*(len(to_print)-1), style="blue on bright_white")


