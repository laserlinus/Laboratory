import pandas as pd
import numpy as np
import datetime
import time
from bokeh.plotting import figure, output_file, show

def create_orig(tablesize):
    origcities = ['sthlm', 'copenhagen', 'oslo', 'uppsala', 'gothenburg', 'karlstad']
    origcitylist = []
    for i in range(tablesize):
        random = np.random.randint(0, 6)
        origcitylist.append(origcities[random])
    return origcitylist

def create_dest(tablesize):
    destcities = ['bangkok', 'barcelona', 'la paz', 'mumbai', 'new york', 'puebla']
    destcitylist = []
    for i in range(tablesize):
        random = np.random.randint(0, 6)
        destcitylist.append(destcities[random])
    return destcitylist

def create_frame(starttime,origcitylist,destcitylist,tablesize):
    index=pd.date_range(starttime, periods=tablesize, freq="S")
    df = pd.DataFrame(np.random.randint(10,size=tablesize), index=index,columns=['Orders'])
    df['OrigCity'] = origcitylist
    df['DestCity'] = destcitylist
    return df

def rolling_comparison(df):
    for i in range(60):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if timestamp in df.index:
            value = df.loc[timestamp]
            print (value)
        else:
            print('No data')
        time.sleep(1)

def plot(df):
    x = df.index.values
    y = df.iloc[:,0].values
    output_file("lines.html")
    p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
    p.line(x, y, legend="Temp.", line_width=2)
    show(p)

def run_script(starttime, tablesize):
    origcitylist = create_orig(tablesize)
    destcitylist = create_dest(tablesize)
    df = create_frame(starttime,origcitylist, destcitylist, tablesize)
    rolling_comparison(df)
    #plot(df)



## Heyooo ##

tablesize = 500
#starttime = '01:16:00/17/3/2017'
starttime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
run_script(starttime,tablesize)
