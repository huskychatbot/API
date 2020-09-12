ExchangeRate API url: https://api.exchangeratesapi.io/latest?base=USD;

In package.json, dependencies add "axios": "^0.20.0"

In indes.js, add function mutipleHandler, parse the url and get the rate.
Note: in line 23, must to be a return clause to add the return value to the agent

