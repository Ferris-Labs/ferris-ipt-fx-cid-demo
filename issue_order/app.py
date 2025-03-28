import random
import math
from time import sleep
from ferris_ef import context

isin = context.params.get("ISIN")
companyname = context.params.get("companyname")
ordertype = context.params.get("ordertype")
broker = context.params.get("broker")
quota = int(context.params.get("quota"))
price = context.params.get("price")

p1 = random.randint(math.ceil(quota*0.3), math.ceil(quota*0.5))
p2 = random.randint(math.ceil(quota*0.3), math.ceil(quota*0.5))
dummy_percentages = [p1, p2, quota-p1-p2]
dummy_prices = [price, math.ceil(price*1.002), math.ceil(price*1.005)]

print(f"Issuing an order request for {quota} shares of {companyname} shares with ISIN {isin}...")
sleep(2)
print("Received 3 partial fills for the order:")

for idx, perc in enumerate(dummy_percentages):
    cur_price = dummy_prices[idx]
    print(f"1. {perc} shares @ {cur_price} ")

    context.events.send(
        "cd_issue_payment",
        context.package.name,
        {
            "companyname": companyname,
            "ordertype": ordertype,
            "ISIN": isin,
            "broker": broker,
            "price": cur_price,
            "currency": "CHF",
            "quota": perc,
            "amount": perc * cur_price
        }
    )
    sleep(1)

print("Payment events sent")
