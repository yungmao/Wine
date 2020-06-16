import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from Red_or_White.dataService import dataframe
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier


classifications = 2 #Białe i czerwone
df = dataframe()
df['Gatunek'] = np.where(df['Gatunek'] == 'Czerwone wino', 1, df['Gatunek'])
df['Gatunek'] = np.where(df['Gatunek'] == 'Białe wino', 0, df['Gatunek'])

X = df[df.columns[:-1]]
X=X.astype('float')
Y = df['Gatunek']
Y=Y.astype('int')
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.7, random_state=23)

n3 = KNeighborsClassifier(n_neighbors = 3)
n3.fit(x_train, y_train)
pred_n3 = n3.predict(x_test)
print(classification_report(y_test, pred_n3))

rf = RandomForestClassifier()
rf.fit(x_train, y_train)
pred_rf = rf.predict(x_test)
print(classification_report(y_test, pred_rf))

dt = DecisionTreeClassifier()
dt.fit(x_train, y_train)
pred_dt = dt.predict(x_test)
print(classification_report(y_test, pred_dt))

sgd = SGDClassifier()
sgd.fit(x_train, y_train)
pred_sgd = sgd.predict(x_test)
print(classification_report(y_test, pred_sgd))

NN = MLPClassifier(solver='adam', alpha=0.0001,
                   hidden_layer_sizes=(1, 50),
                   random_state=6, max_iter=2000, verbose=1).fit(x_train, y_train)
pred_MLPC = NN.predict(x_test)
print(classification_report(y_test,pred_MLPC))


feat_importances = pd.Series(rf.feature_importances_, index=['Kwas winowy','Kwas octowy','Kwas cytyrynowy',
                                                             'Cukier','Chlorki','Dwutlenek siarki',
                                                             'Wolny dwutlenek siarki', 'Gęstość','pH','Siarczany','Alkohol'])
feat_importances.nlargest(11).plot(kind='barh')
plt.xlabel("Wpływ cech na ocenę dla lasów losowych")
#plt.show()
plt.savefig('plots/lasy.png',bbox_inches = "tight")


feat_importances = pd.Series(dt.feature_importances_, index=['Kwas winowy','Kwas octowy','Kwas cytyrynowy',
                                                             'Cukier','Chlorki','Dwutlenek siarki',
                                                             'Wolny dwutlenek siarki', 'Gęstość','pH','Siarczany','Alkohol'])
feat_importances.nlargest(11).plot(kind='barh')
plt.xlabel("Wpływ cech na ocenę dla drzewa decyzyjnego")
#plt.show()
plt.savefig('plots/drzewp.png',bbox_inches = "tight")




