#bg_to_goty_regression


from organizing_bg_data import data_set
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# setting general figure size to fit the screen better
plt.rcParams['figure.figsize'] = (10,5)

# setting x and y values
X = data_set[0]
Y = data_set[1]

# average of x and y sets from data collected 
x_mean = np.mean(X)
y_mean = np.mean(Y)

#length of y, because y is slightly smaller, and causes out of range error
n = len(Y)

#find the denomenator and numerator for the regression sum
num, den = 0, 0
for i in range(n):
    num += (X[i] - x_mean) * (Y[i] - y_mean)
    den += (X[i] - x_mean) ** 2

#finding the coefficients
b1 = num/den
b0 = y_mean - (b1 * x_mean)

print(b1, b0)

#setting maximum and minimum values for the graph
x_max = np.max(X)
x_min = np.min(X)

#finding the line eqn of the model 
x = np.linspace(x_min, x_max, 1000)
y = b0 + b1 * x

t = 0
r = 0
for i in range(n):
    y_pred = b0 + b1 * X[i]
    t += (Y[i] - y_mean) ** 2
    r += (Y[i] - y_pred) ** 2
r2 = 1 - (r/t)

r_squared = round(r2, 4)

print(f"The resulting r squared is: {r_squared}")


#plotting the line of the model and the data X and Y in one graph
plt.scatter(X, Y, color='blue', label='scatter plot')
plt.plot(x, y, color='red', label='regression line')
plt.title('Relationship Between Keywords and the Amount of Times They are Mentioned In a Period of a Month')
plt.xlabel('Baldurs gate 3 mentioned')
plt.ylabel('Game of the year mentioned')
plt.legend()
plt.text(0.05, 14, f"R^2 value is: {r_squared}")
#plt.savefig('final_graph_of_correlation.jpg')
plt.show()


