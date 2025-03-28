from time import sleep
from ferris_ef import context

isin = context.params.get("ISIN")
companyname = context.params.get("companyname")
ordertype = context.params.get("ordertype")
broker = context.params.get("broker")
quota = context.params.get("quota")
price = context.params.get("price")
amount = context.params.get("amount")

print(f"Settlement for {quota} shares of {companyname} shares with ISIN {isin} is received. Total amount: {amount} CHF")
sleep(2)

context.events.send(
    "cd_settlement_confirmation_received",
    context.package.name,
    {
        "companyname": companyname,
        "ordertype": ordertype,
        "ISIN": isin,
        "broker": "Swissquotes",
        "price": price,
        "quota": 35,
        "amount": 35 * 111800
    }
)

