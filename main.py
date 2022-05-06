# Imports
from os import system, name
import os.path
from os import path
from rich.console import Console
console = Console()
from rich import print
from rich.panel import Panel
import argparse
from record_sell import sell
from datetime import datetime
from expiry_schedule import to_get_expire_report_processed
from assignment_report import report_superpy


# Do not change these lines.
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'

# Your code below this line.
#------------------------------------------------------------------------------

# current_date = datetime.datetime.today().strftime('%Y-%m-%d')
# yesterday = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

#------------------------------------------------------------------------------

to_get_exists_directory = path.exists("supermarket_data")  
if to_get_exists_directory:
    console.print(Panel.fit("Welcome to the [blink bold dark_red underline2]:apple::apple::apple:Supermarket SuperPy.:apple::apple::apple:[/] This App is build on a [overline]Command-Line Tool[/] that the Supermarket SuperPy will use to keep track of their all the daily activities stock in inventory.", style="bold blue on #d7ffff"))
else:
    import essential_constructor

# The argparse module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments. So here we use argparse command line tools for supermarket inventory, like --product_id, --soldprice, --solddate etc etc.


def main(command_line = None):
    parser = argparse.ArgumentParser("Supermarket SuperPy")
    subparsers = parser.add_subparsers(dest="command")


    report = subparsers.add_parser("report", help ="It exhibits a comprehensive Stock Inventory. e.g. python3 main.py report")

    buyproduct = subparsers.add_parser("buyproduct", help ="Enter (buyproduct) and buy a product for Supermarket. e.g. python3 main.py buyproduct")

    sellproduct = subparsers.add_parser("sellproduct", help ="Sold Items Information with respect to price and date", description ="inventory items transaction")
    sellproduct.add_argument("-id", "--product_id", help ="Sold Items unique-id ", required = True)
    sellproduct.add_argument("-sp", "--soldprice", help="Sold Items Price", required=True)
    sellproduct.add_argument("-sd", "--solddate", help="Sold Items Date. Default = today", required = False)

    expire = subparsers.add_parser("expire", help="Product expiration date, represented with Number of Days counted. Default 0 = Today, negative number(days)with current date = yesterday, positive number(days) = tomorrow")
    expire.add_argument("-ed", "--expiredate", help="Processed Date Start. Default = today", required=False)
    expire.add_argument("-nd", "--numdays", help="Adds or subtract number of days in current date or Number of Processed Days", required=True)

    # The following code is a Python program that takes a list of products and produces either the report or the items in inventory. The Python code above is saved into a file called main.py, it can be run at the command line and provides useful help messages and diffrent derived files from stock.csv.

    args = parser.parse_args(command_line)

    if args.command == "report":
        import report_inventory

    elif args.command == "buyproduct":
        import buyproduct_input

    elif args.command == "sellproduct":
        product_id =            str(args.product_id)
        product_sold_date =     str(args.solddate)
        product_sold_price =    str(args.soldprice)
        # product_sold_date =     str(args.solddate)
        sell(product_id, product_sold_price, product_sold_date)
        # sell(product_id, product_sold_date, product_sold_price)


    elif args.command == "expire":
        get_process_date =      str(args.expiredate)
        number_of_days =        int(args.numdays)
        to_get_expire_report_processed(get_process_date, number_of_days)

    else:
        console.print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<:apple:>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
            "\n\n\t\t\t\t\t\t:apple::apple::apple:[green]Supermarket SuperPy[/]:apple::apple::apple:"
            "\n\n\t\t\t To access well-structured and user friendly command-line interface with clear descriptions\n\t\t\t of each argument in the --help section, please, explore from the HELP file.\n\t\t\t"
               " Moreover, the optional commands are described in [underline light_green]report[/], [underline light_green]buyproduct[/], [underline light_green]sellproduct[/] or [underline light_green]expire[/]."
               "\n\n\t\t\t\t Type 'python3 main.py -h' for additional information.\n")
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<:apple:>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

if __name__ == '__main__':
        main()
