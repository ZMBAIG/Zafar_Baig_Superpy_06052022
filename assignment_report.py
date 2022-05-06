
# import os.path
# from os import path


report_superpy = """Assignment: SuperPy
        
        Here, I am going to evaluate three necessary elements.
        1.CSV File Reading and Writing. To access a well-structured and user friendly command-line interface with clear descriptions and information, CSV file is the backbone of our supermarket database management. A detail inventory transaction is only possible with the application of csv files. These files are derived from pre-defined 'stock.csv' and can be easily read and write in most of the operating system. When certain command line tools are conducted with exporting a report, buy or sell a product and expire certain items all of these files are updated. These identified items with unique code are essential to keep up-to-date record of inventory. Since products might have the same name, but could have a different unique-id, these products should be separated from each other in the inventory file.

        2.Basic date and time types; a set up of schedule for number of days; (today, tomorrow and yesterday) for the products transaction is introduced. This helps to enumerate different period of dates to examine status of items stored in inventory. The procedure is very convenient to run, to keep a check and balance for all the tracks that a supermarket requires to store or exit a product in inventory. Moreover, expiration date of a certain product, revenue generated and buying loss are the alarming tools for a transaction period.

        3.Parser for command-line options, arguments and subcommands. The argparse module makes it easy to write user-friendly command-line interfaces. This defines what arguments it requires, and will figure out how to parse those out of sys.argv. It also automatically generates help and usage messages and issues errors when users give the program invalid arguments. So here we use argparse command line tools for supermarket inventory, like --product_id, --soldprice, etc.
        """

with open ('assignment_report.txt', 'w') as file:
            file.write(report_superpy)
