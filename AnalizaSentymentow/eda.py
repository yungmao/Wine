import matplotlib.pyplot as plt # Library to plot graphics
import seaborn as sns # to build modern graphics
from AnalizaSentymentow.dataService import dataframe

df = dataframe()
plt.figure(figsize=(16,5))
sns.countplot(x='points', data=df)
#plt.show()
plt.savefig('plots/rozklad.png',bbox_inches = "tight")
