from yahoo_finance import Share
from yahoo_finance import Currency
from pprint import pprint
# Get shares data

yahoo = Share('YHOO')
print (yahoo.get_open())
print (yahoo.get_price())
print (yahoo.get_trade_datetime())

# Refresh data
yahoo.refresh()
print (yahoo.get_price())

# Historical data
print (yahoo.get_historical('2014-04-25', '2014-04-29'))
pprint(yahoo.get_historical('2014-04-25', '2014-04-29'))
pprint(yahoo.get_info())

## Currency
eur_pln = Currency('EURPLN')
print (eur_pln.get_bid())
print (eur_pln.get_ask())
print (eur_pln.get_rate())
print (eur_pln.get_trade_datetime())
