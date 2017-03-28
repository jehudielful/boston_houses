import matplotlib.pyplot as plt
import numpy as np #linear algebra
import pandas as pd
import matplotlib.pylab as plt
import numpy as np

train_data = pd.read_csv('C:/_WWWork/_git/boston_houses/data/train.csv')
test_data = pd.read_csv('C:/_WWWork/_git/boston_houses/data/test.csv')
all_data = pd.concat([train_data, test_data])
print(train_data.head())
#print(train_data.MSSubClass)
#train_data.pivot_table('Id', 'MSSubClass', 'SalePrice', 'count').plot(kind='bar', stacked=True)

#fig, axes = plt.subplots(ncols=2)
#train_data.pivot_table('PassengerId', ['MSSubClass'], 'Survived', 'count').plot(ax=axes[0], title='MSSubClass')
#train_data.pivot_table('PassengerId', ['SalePrice'], 'Survived', 'count').plot(ax=axes[1], title='SalePrice')

plt.figure(1)
plt.subplot(211)
plt.plot(train_data.MSSubClass,train_data.SalePrice, 'bs')

plt.subplot(212)
plt.plot(train_data.PoolArea,train_data.SalePrice, 'ro')
#plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')i
plt.subplot(231)
plt.plot(train_data.LotArea,train_data.SalePrice, 'bs')


plt.show()
#print(train_data.PassengerId[train_data.Cabin.notnull()].count())

