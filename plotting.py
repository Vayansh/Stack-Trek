import matplotlib.pyplot as plt
import pandas as pd
import csv
path='table_output1.csv'
data=pd.read_csv(path)
serial=data.serial
time=data.Time
plt.plot(serial,time+1)
plt.savefig('savedgraph.png')
plt.show()

