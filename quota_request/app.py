from time import sleep
from ferris_ef import context

isin = context.params.get("ISIN")
companyname = context.params.get("companyname")
quota = context.params.get("quota")
ordertype = context.params.get("ordertype")
# brokers = context.params.get("brokers")

brokers = ['Swissquotes', 'Interactive Brokers']

dummy_prices = {
    "Swissquotes": 111800,
    "Interactive Brokers": 113900
}

selected_broker = brokers[0]

print(f"Issuing a requests for quotation for the market order purchasing of {quota} shares of {companyname} shares...")
sleep(2)

for broker in brokers:
    print(f"Received quota price from {broker}: {dummy_prices[broker]} CHF")

    if dummy_prices[broker] < dummy_prices[selected_broker]:
        selected_broker = broker

print(f"Sending issue_order event for {selected_broker} at {dummy_prices[selected_broker]} CHF...")


context.events.send(
    "cd_issue_order",
    context.package.name,
    {
        "companyname": companyname,
        "ordertype": ordertype,
        "ISIN": isin,
        "broker": selected_broker,
        "price": dummy_prices[selected_broker],
        "currency": "CHF",
        "quota": quota
    }
)


