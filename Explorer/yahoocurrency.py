from yahoo_finance import Currency
import time
import datetime
import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show

def data_extraction(interval, length):
    x = []
    y = []
    eur_sek = Currency('EURSEK')
    for i in range (length):
        eur_sek.refresh()
        timestamp = datetime.datetime.now()
        rate = eur_sek.get_bid()
        print('Time: ',timestamp)
        print ('EUR-SEK: ',rate)
        print ('')
        x.append(timestamp)
        y.append(rate)
        time.sleep(interval)
    data = pd.DataFrame(x, columns=['Date'])
    data['Rate'] = y
    return data

def plot(data):
    x = data.iloc[:,0].values
    y = data.iloc[:,1].values
    #mean = np.mean(y)
    output_file("currency.html")
    p = figure(title="SEK to Euro", x_axis_type='datetime', x_axis_label='Date', y_axis_label='Rate',y_range=(9.45, 9.6))
    p.line(x, y, legend="Temp.", line_width=5)
    show(p)

interval = 1
length = 10
data = data_extraction(interval, length)
plot(data)
data.to_csv('data1.csv')