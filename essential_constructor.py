
from os import system, name
import os
from stock_establish import StockEstablish
from expiry_schedule import to_acquire_expired_report_today
from datetime import date, datetime

_ = system('cls') 
# This function use to clear screen.                                           
to_get_stock_data =         StockEstablish()
to_get_current_date =       date.today()
to_get_todays_expire =      to_acquire_expired_report_today(to_get_current_date, 0)        
to_get_files_path =         os.path.realpath(__file__)
to_create_files_directory = os.path.dirname(to_get_files_path)
to_get_directory_path =     os.path.join(to_create_files_directory, "supermarket_data")
to_get_inventory_file =     os.path.join(to_get_directory_path,     "inventory_report.csv")
to_get_expire_dates_file =  os.path.join(to_get_directory_path,     "expired_products.csv")

import report_inventory
