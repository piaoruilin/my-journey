import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
a=[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
b=[1,2,4,5,8,11,23,26,30,37]
regr = linear_model.LinearRegression()
mdl = regr.fit(a,b)
y_predict = regr.predict(a)
plt.scatter(a,b,alpha=0.4)
plt.plot(a,y_predict)
plt.show()
