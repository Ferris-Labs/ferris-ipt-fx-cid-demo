from time import sleep
from ferris_ef import context

isin = context.params.get("ISIN")
companyname = context.params.get("companyname")
numofshares = context.params.get("isin")
ordertype = context.params.get("ordertype")
broker = context.params.get("broker")
quota = context.params.get("quota")
price = context.params.get("price")
amount = context.params.get("amount")

print(f"Processing payment for {quota} shares of {companyname} shares with ISIN {isin} at price {price}. Total amount: {amount} CHF")
sleep(2)
print("Payment completed")

context.events.send(
    "cd_payment_confirmed",
    context.package.name,
    {
        "companyname": companyname,
        "ISIN": isin,
        "broker": broker,
        "amount": amount,
        "quota": quota,
        "price": price,
        "currency": "CHF"
    }
)

