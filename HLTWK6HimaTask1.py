from re import X
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model._glm.glm import _y_pred_deviance_derivative
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

s_data = pd.read_csv('student_scores.csv')
print(s_data)



# s_data.shape
# s_data.head()
# #s_data.describe(include=[np.number])


s_data.plot(x='Hours', y='Scores', style='o')
plt.title('Hours vs Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.show()

X = s_data.iloc[:, :-1].values
y = s_data.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0)
regressor = LinearRegression()
regressor.fit(X_train, y_train)

print(regressor.intercept_)

print(regressor.coef_)

#y_pred = regressor.predict(X_test)

#df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
#df

# df = pd.DataFrame({ 'col-1': ['Petrol_tax', 'Average_income', 'Paved_Highways', 'opulation_Driver_licence(%)', 'Petrol_Consumption'],
#                     'col-2': [9,3571,1976,0.525,541]
# })
# #print(df)
# df.describe(include=['object'])
# df.plot(x='col-1', y='col-2', style='o')
# plt.title('Petrol use vs Calculation')
# plt.xlabel('Petrol use in')
# plt.ylabel('Calculation Info')
# plt.show()

