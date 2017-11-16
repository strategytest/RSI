import pandas as pd
import numpy as np


def RSI(price, length):
    rsi_lst = []
    MyRange = length
    for i in range(len(price)):
        if i < MyRange:
            rsi_lst.append(0)
        else:
            DownAmt, UpAmt = [], []
            UpSum, DownSum, UpAvg, DownAvg = 0, 0, 0, 0
            for j in range(MyRange-1):
                UpAmt.append(price[i-j] - price[i-j-1])
                if UpAmt[j] >=0:
                    DownAmt.append(0)
                else:
                    DownAmt.append(-UpAmt[j])
                    UpAmt[j] = 0
                UpSum += UpAmt[j]
                DownSum += DownAmt[j]
            UpAvg = np.array(UpSum) / MyRange
            DownAvg = np.array(DownSum) / MyRange
            if UpAvg+DownAvg != 0:
                rsi_lst.append(100*UpAvg/(UpAvg+DownAvg))
            else:
                rsi_lst.append(0)
    return rsi_lst

df = pd.read_csv('HSI.csv', na_values= 'null').fillna(method = 'ffill')
df = df[['Date', 'Adj Close']].set_index('Date')
df['RSI'] = RSI(df['Adj Close'], 10)
