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

Head over to home.sb.ferris.ai to start and register for a new user. 

1. Clone the repo to your own machine, directory & account
1. Change and extend after your own creative likings & commit / push your changes 
1. Create your "own" project on the FX sandbox
1. Add your "own" version / repo to the project
1. Add the synch / deploy key to your remote repo (use the SSH notation link)
1. Synchronize the project with your remote repo
1. Test and debug at your will on   

Of course feel free to completely leave the example behind and try for some more complex cases involving "real" API calls or other ideas you may have.
