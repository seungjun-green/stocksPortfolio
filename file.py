from yahoo_fin import stock_info as si
from pretty_tables import PrettyTables


tickers = []
shares = []
marketValue = []
temp = []
rows = []
totalValue = 0

stocks = 0
percentage = []
headers = ["Ticker", "Shares", "Market Value".  , "Percentage"]
stocks = int(input("How many ticker symbols? : "))
valueInDollar = ''
errorHappend = True

for i in range(0, stocks):

    # Ticker Symbol
    while errorHappend == True:
        new = input("Ticker Symbol: ")
        try:
            si.get_live_price(new)
            errorHappend = False
        except:
            print("The Ticker Symbol", new, "Does not exist")
            print("Please input valid Ticker Symbol :)")
            errorHappend = True
            print()

    errorHappend = True


    if new in tickers:
        while new in tickers:
            print(new,"is already in the portfolio, try other Ticker Symbol plz: ")
            new = input("other ticker symbol: ")

    tickers.append(new)
    temp.append(new)

    # Shares

    s = float(input("%s | Number of Shares: " %tickers[i]))
    if s <= 0:
        while s <= 0:
            print("number of shares should be bigger than 0")
            s = float(input("%s | Number of Shares: " % tickers[i]))
    s = round(s, 2)
    shares.append(s)
    temp.append(s)

    # Market Value
    value = si.get_live_price(tickers[i]) * shares[i]
    totalValue += value
    marketValue.append(value)
    valueInDollar = '$'+str(round(value,2))
    temp.append(valueInDollar)

    temp.append(0)

    rows.append(temp)
    temp = []


for i in range(stocks):
    rows[i][3] = str(round(((marketValue[i]/totalValue)*100), 2)) + "%"

print("total Value: ", totalValue)
table = PrettyTables.generate_table(
    headers=headers,
    rows=rows,
    empty_cell_placeholder='No data'
)

print(table)






print("testing")
