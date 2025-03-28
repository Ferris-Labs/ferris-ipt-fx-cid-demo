# Ferris IPT Demo Day - CID Example

## Background

The following minimal demo example fakes an Equity Order flow along the following steps:

1. Specify some (fake) details about the share order and exchanges selected
1. Attempt to get the best price from the two brokers selected
1. Issue the order with the "best price" exchange
1. Fake partial fill across three separate tranches

To illustrate the different executor capabilities with minimum code we did not include the actual API calls and response resolvers.


## Explainer

1. Illustrate minimum required elements for a project / flow
1. Explain the main components of each service / step in the flow
    - manifest.json
    - parameters.json (optional)
    - config.json (optional)
    - app.py (main service / step processing logic)
1. Explain the difference in explicit state elements and implied state elements


## Steps to Play


