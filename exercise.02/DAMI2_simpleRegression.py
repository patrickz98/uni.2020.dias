import numpy as np
from numpy import *
import matplotlib.pyplot as plt

data = genfromtxt('scores.csv', delimiter=',')

# Extract the data needed to perform a regression
x = array(data[:, 0])
y = array(data[:, 1])


def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)

    # HERE: Get the mean of x and y vector (hint: use built-in functions)
    x_mean = x.mean()
    y_mean = y.mean()

    # calculating cross-deviation and deviation about x
    nominal = 0
    for idx in range(n):
        nominal += (x[idx] - x_mean) * (y[idx] - y_mean)

    counter = 0
    for idx in range(n):
        counter += (x[idx] - x_mean) ** 2

    # HERE: Calculate the regression coefficients
    beta_1 = nominal / counter
    beta_0 = y_mean - beta_1 * x_mean

    return beta_0, beta_1


def plot_regression_line(x, y, b):
    # HERE: plot the actual points as scatter plot

    # HERE: compute the predicted response vector
    y_pred = [b[0] + b[1] * val for val in x]

    # plotting the regression line
    plt.plot(x, y_pred, color="k")

    # putting labels
    plt.scatter(x, y)
    plt.xlabel('Hours of study')
    plt.ylabel('Test scores')

    # function to show plot
    plt.savefig("exercise.02.04.result.png", dpi=600)


# DATASET INPUT
def main():
    # estimating coefficients
    b = estimate_coef(x, y)
    print('The estimated coefficients are', repr(b[0]), 'and', repr(b[1]))

    # plotting regression line
    plt.figure(2)
    plot_regression_line(x, y, b)


if __name__ == "__main__":
    main()
