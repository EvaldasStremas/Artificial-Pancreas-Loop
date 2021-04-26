import random
import numpy as np
import matplotlib.pyplot as plt

# Inputs
first_glucose_reading = 9
cycles = 10
daily_insulin_units = 66


def print_glucose_data(first_glucose_value, cycles):
    x = range(cycles)
    y = []

    for i in range(cycles):
        y.append(first_glucose_value)
        first_glucose_value += (random.choice((-1, 1)) * random.uniform(0, 0.2))

    plt.plot(x, y)
    plt.show()


def get_glucose_data(first_glucose_value, cycles):
    x = range(cycles)
    y = []

    for i in range(cycles):
        y.append(first_glucose_value)
        first_glucose_value += (random.choice((-1, 1)) * random.uniform(0, 0.2))
    return y


def get_insulin_sensitivity(daily_insulin_units):
    insulin_sensitivity = 100 / daily_insulin_units
    return insulin_sensitivity


def get_glucose_data_delta(glucose_data, cycles):
    x = range(cycles)
    y = []

    for i in range(cycles):
        glucose_delta = glucose_data[i] - glucose_data[i - 1]
        y.append(glucose_delta)
    return y


def print_glucose_data_delta(glucose_data, cycles):
    x = range(cycles)
    y = []

    for i in range(cycles):
        glucose_delta = glucose_data[i] - glucose_data[i - 1]
        y.append(glucose_delta)
    plt.plot(x, y)
    plt.show()


glucose_data = get_glucose_data(first_glucose_reading, cycles)
print(glucose_data)

glucose_data_delta = get_glucose_data_delta(glucose_data, cycles)
print(glucose_data_delta)

insulin_sensitivity = get_insulin_sensitivity(daily_insulin_units)
print(insulin_sensitivity)

print_glucose_data_delta(glucose_data, cycles)