import random
import matplotlib.pyplot as plt
from inputs import FIRST_GLUCOSE_READING, cycles, daily_insulin_units

def get_glucose_data(first_glucose_value, cycles):
    y = []

    for i in range(cycles):
        y.append(first_glucose_value)
        first_glucose_value += (random.choice((-1, 1)) * random.uniform(0, 0.5))
    return y

def get_glucose_data_delta(glucose_data, cycles):
    y = []

    for i in range(cycles):
        glucose_delta = glucose_data[i] - glucose_data[i-1]
        if glucose_delta < 0:
            glucose_delta = 0
        y.append(glucose_delta)
    return y

def get_insulin_sensitivity(daily_insulin_units):
    insulin_sensitivity = 100 / daily_insulin_units
    return insulin_sensitivity

def get_basal_data(glucose_data, cycles):
    y = []

    for i in range(cycles):
        basal = glucose_data[i] * get_insulin_sensitivity(daily_insulin_units)
        y.append(basal)
    return y