import pandas as pd
import csv
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
# Read dataset
champion = pd.read_csv('Champ.Challenge.csv')
# Transpose of dataset
match_mid = champion.T
# Remove default index
match_mid.columns = match_mid.iloc[0]
match = match_mid[1:]
# Fill 0 with NaN values
match = match.fillna(0)
# Replace YES wit 1
match = match.replace('YES',1)
print match.head()
# Retrieve part of the values
Kmeans_values = match.iloc[:,1:66].values
print Kmeans_values
print match.values
# Convert numpy.array to list
a = match.values.tolist()
print a
print type(a)

# look for number of clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    kmeans.fit(Kmeans_values)
    wcss.append(kmeans.inertia_)
print wcss
plt.plot(range(1, 11), wcss)
plt.title('The elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS') #within cluster sum of squares
plt.show()

# Build Model
kmeans = KMeans(n_clusters=3, init='k-means++',max_iter=100, n_init=10, random_state=0)
y_kmeans = kmeans.fit_predict(Kmeans_values)
print y_kmeans

