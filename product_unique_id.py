
from datetime import date

# By creating a random unique item-ids in the following categary; date(today), Number of items, Date of Expiration and Date of buy Items. Since products might have the same name, but could have a different unique-id, these products should be separated from each other in the inventory file.This makes a clear and meaning full property due to lack of copying same products.

def unique_id(amount_round, expiration_date, buy_date): 
    
    import random
    today =                 str(date.today())
    today_replace =         today.replace("-", "")
    amount =                str(amount_round)
    expiration_date =       expiration_date
    expiration_replace =    expiration_date.replace("-", "")
    buy_date =              buy_date
    buy_replace =           buy_date.replace("-", "")
    change_product_id =     int(today_replace+amount+expiration_replace+buy_replace)
    random =                random.random()
    change_product_id =     int((change_product_id * random)/(2e+17))

    
    return change_product_id

