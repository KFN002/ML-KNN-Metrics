import numpy as np
import math


def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def mean_absolute_error(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))


def root_mean_squared_error(y_true, y_pred):
    return math.sqrt(mean_squared_error(y_true, y_pred))


def r_squared(y_true, y_pred):
    mean_true = np.mean(y_true)
    ss_total = np.sum((y_true - mean_true) ** 2)
    ss_res = np.sum((y_true - y_pred) ** 2)
    r2 = 1 - (ss_res / ss_total)
    return r2


true_values = np.array(list(map(float, input().split())))
predicted_values = np.array(list(map(float, input().split())))

mse = mean_squared_error(true_values, predicted_values)
mae = mean_absolute_error(true_values, predicted_values)
rmse = root_mean_squared_error(true_values, predicted_values)

r2 = r_squared(true_values, predicted_values)

print(f"R2: {r2:.2f}")
