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

print(f"Payment for {quota} shares of {companyname} shares with ISIN {isin} is confirmed. Total amount: {amount} CHF")
sleep(2)

context.events.send(
    "cd_issue_settlement_confirmation",
    context.package.name,
    {
        "companyname": companyname,
        "ISIN": isin,
        "broker": "Swissquotes",
        "quota": quota,
        "amount": amount,
        "currency": "CHF",
    }
)

