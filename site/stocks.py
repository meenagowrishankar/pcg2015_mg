#GIVEN THE FOLLOWING LIST OF LIST
test_data = [
    ["2014-06-01", "APPL", 100.11],
    ["2014-06-02", "APPL", 110.61],
    ["2014-06-03", "APPL", 120.22],
    ["2014-06-04", "APPL", 100.54],
        ["2014-06-01", "MSFT", 20.46],
    ["2014-06-02", "MSFT", 21.25],
    ["2014-06-03", "MSFT", 32.53],
    ["2014-06-04", "MSFT", 40.71],
    ["2014-06-04", "ABCD", 40.71]
]

#CREATE TWO NEW LISTS ONE FOR EACH STOCK TICKER SYMBOL e.g. APPL and MSFT

appl = []

msft = []

stocks = {}

# for a in test_data:
# 	if a[1] == "APPL":
# 		appl.append(a[0])
# 		appl.append(a[2])
# 		stocks[a[1]] = appl
# for a in test_data:
# 	if a[1] == "MSFT":
# 		msft.append(a[0])
# 		msft.append(a[2])
# 		stocks[a[1]] = msft

# print appl
# print msft


# x = str(stocks)
# print x
# print stocks.keys()
for a in test_data:
	if a[1] not in stocks:
		stocks[a[1]] = [a[0], a[2]]
		
for a in test_data:
	if a[1] == stocks.keys:
		stocks[a[1]] = [a[0], a[2]]



print stocks
print stocks['APPL']

#ONCE THAT WORKS THEN what would need to change to copy with an unknown number of stock ticker symbols?



