import pandas as pd
import numpy as np
from mlxtend.preprocessing import OnehotTransactions
from mlxtend.frequent_patterns import apriori
import matplotlib.pyplot as plt

challenges = pd.read_csv('CHALLENGE.csv')
challenge = challenges.set_index('STARTUP')
challenge = challenge.replace('Please Select', np.nan)
challenge.drop(challenge.columns[len(challenge.columns)-1], axis=1, inplace=True)

count = challenge.apply(pd.Series.value_counts)
count['Frequency'] = count['FIRST CHOICE'] + count['SECOND CHOICE'] + count['THIRD CHOICE']
count.drop(count.columns[0:3], axis=1, inplace=True)
count = count.dropna()
Frequency = count.sort_values(['Frequency'])
print Frequency.shape

Frequency.to_csv('Frequency.csv', sep=',')

count.plot.barh(fontsize=7)
plt.xlabel('Frequency'12
plt.ylabel('Challenge')

plt.show()

dataset = challenge.values.tolist()
print dataset

oht = OnehotTransactions()
oht_ary = oht.fit(dataset).transform(dataset)
df = pd.DataFrame(oht_ary, columns=oht.columns_)
print df

results = apriori(df, min_support=0.005,use_colnames=True)
results.itemsets = results.itemsets.apply(lambda x: tuple(x))
results = results.sort_values(['itemsets','support'],ascending=[True, False])

results.to_csv('Results.csv', sep=',')


