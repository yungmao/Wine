from Red_or_White.dataService import dataframe
import seaborn as sns
import matplotlib.pyplot as plt

df = dataframe()

fig = plt.figure(figsize = (4,3))
#sns.barplot(x = 'Gatunek', y = 'fixed acidity', data = df)
sns.violinplot(x = 'Gatunek', y = 'fixed acidity', data = df)
plt.ylabel('Kwas winowy')
#plt.show()
plt.savefig('plots/fixed_acidity.png',bbox_inches = "tight")

fig = plt.figure(figsize = (4,3))
#sns.barplot(x = 'Gatunek', y = 'volatile acidity', data = df)
sns.violinplot(x = 'Gatunek', y = 'volatile acidity', data = df)
plt.ylabel('Kwas octowy')
#plt.show()
plt.savefig('plots/volatile_acidity.png',bbox_inches = "tight")

fig = plt.figure(figsize = (4,3))
#sns.barplot(x = 'Gatunek', y = 'citric acid', data = df)
sns.violinplot(x = 'Gatunek', y = 'citric acid', data = df)
plt.ylabel('Kwas cytyrynowy')
#plt.show()
plt.savefig('plots/citric_acid.png',bbox_inches = "tight")

fig = plt.figure(figsize = (4,3))
#sns.barplot(x = 'Gatunek', y = 'residual sugar', data = df)
sns.violinplot(x = 'Gatunek', y = 'residual sugar', data = df)
plt.ylabel('Cukier')
#plt.show()
plt.savefig('plots/sugar.png',bbox_inches = "tight")

fig = plt.figure(figsize = (4,3))
#sns.barplot(x = 'Gatunek', y = 'chlorides', data = df)
sns.violinplot(x = 'Gatunek', y = 'chlorides', data = df)
plt.ylabel('Chlorki')
#plt.show()
plt.savefig('plots/chlorides.png',bbox_inches = "tight")

fig = plt.figure(figsize = (4,3))
#sns.barplot(x = 'Gatunek', y = 'free sulfur dioxide', data = df)
sns.violinplot(x = 'Gatunek', y = 'free sulfur dioxide', data = df)
plt.ylabel('Wolny dwutlenek siarki')
#plt.show()
plt.savefig('plots/freeso2.png',bbox_inches = "tight")

fig = plt.figure(figsize = (4,3))
#sns.barplot(x = 'Gatunek', y = "total sulfur dioxide", data = df)
sns.violinplot(x = 'Gatunek', y = "total sulfur dioxide", data = df)
plt.ylabel('Dwutlenek siarki')
#plt.show()
plt.savefig('plots/tso2.png',bbox_inches = "tight")

fig = plt.figure(figsize = (4,3))
#sns.barplot(x = 'Gatunek', y = 'density', data = df)
sns.violinplot(x = 'Gatunek', y = 'density', data = df)
plt.ylabel('Gęstość')
#plt.show()
plt.savefig('plots/density.png',bbox_inches = "tight")

fig = plt.figure(figsize = (4,3))
#sns.barplot(x = 'Gatunek', y = 'pH', data = df)
sns.violinplot(x = 'Gatunek', y = 'pH', data = df)
plt.ylabel('pH')
#plt.show()
plt.savefig('plots/ph.png',bbox_inches = "tight")

fig = plt.figure(figsize = (4,3))
#sns.barplot(x = 'Gatunek', y = 'sulphates', data = df)
sns.violinplot(x = 'Gatunek', y = 'sulphates', data = df)
plt.ylabel('Siarczany')
#plt.show()
plt.savefig('plots/sulphates.png',bbox_inches = "tight")

fig = plt.figure(figsize = (4,3))
#sns.barplot(x = 'Gatunek', y = 'alcohol', data = df)
sns.violinplot(x = 'Gatunek', y = 'alcohol', data = df)
plt.ylabel('Alkohol')
#plt.show()
plt.savefig('plots/alcohol.png',bbox_inches = "tight")







