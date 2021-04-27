import random
import matplotlib.pyplot as plt
from inputs import FIRST_GLUCOSE_READING, cycles, daily_insulin_units
from functions import get_glucose_data, get_glucose_data_delta, get_insulin_sensitivity, get_basal_data

glucose_data = get_glucose_data(FIRST_GLUCOSE_READING, cycles)
# print(glucose_data)

glucose_data_delta = get_glucose_data_delta(glucose_data, cycles)
# print(glucose_data_delta)

insulin_sensitivity = get_insulin_sensitivity(daily_insulin_units)
# print(insulin_sensitivity)

basal_data = get_basal_data(glucose_data_delta, cycles)
# print(basal_data)


def print_glucose(first_glucose_value):
    x = range(0, len(glucose_data))
    y = glucose_data

    ax1 = fig.add_subplot(221)
    ax1.plot(x, y)
    ax1.set_title('Glucose data')


def print_glucose_delta(glucose_data):
    x = range(0, len(glucose_data))
    y = glucose_data

    ax2 = fig.add_subplot(222)
    ax2.plot(x, y)
    ax2.set_title('Delta glucose data')


def print_basal(glucose_data):
    x = range(0, len(glucose_data))
    y = glucose_data

    ax3 = fig.add_subplot(223)
    ax3.plot(x, y)
    ax3.set_title('Basal insulin units')


# Print graphs
fig = plt.figure()
print_glucose(glucose_data)
print_glucose_delta(glucose_data_delta)
print_basal(basal_data)
plt.show()