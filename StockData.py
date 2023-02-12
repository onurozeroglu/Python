import os
from urllib.request import urlopen

tickers = ['GOOG', 'IBM', 'MSFT']

local_folder = 'x'

output_folder = 'x'

for ticker in tickers:
    url = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1=1587042293&period2=1618578293&interval=1d&events=history&includeAdjustedClose=true'
    local_path = os.path.join(local_folder, f'{ticker}.csv')
    with urlopen(url) as image, open(local_path, 'wb') as f:
        f.write(image.read())

for ticker in tickers:
    local_path = os.path.join(local_folder, f'{ticker}.csv')
    output_path = os.path.join(output_folder, f'{ticker}_change.csv')

    with open(local_path, 'r') as f:
        lines = f.readlines()

    with open(output_path, 'w') as f:
        for line in lines:

            columns = line.strip().split(',')

            try:
                open_price = float(columns[1])
                close_price = float(columns[4])
                change = (close_price - open_price) / open_price
            except ValueError:

                f.write(line)
                continue

            f.write(f'{line.strip()},{change}\n')