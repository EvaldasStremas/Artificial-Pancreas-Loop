import random
import matplotlib.pyplot as plt
from inputs import *

class Glucose: 

    def get_glucose_data(first_glucose_value, cycles):
        y = []

        for _ in range(cycles):
            y.append(first_glucose_value)
            first_glucose_value += (random.choice((-1, 1)) * random.uniform(0, 0.5))
        return y

    def get_glucose_data_delta(glucose_data):
        y = []

        for i in range(len(glucose_data)):
            glucose_delta = glucose_data[i] - glucose_data[i-1]
            if glucose_delta < 0:
                glucose_delta = 0
            y.append(glucose_delta)
        return y

    def get_insulin_sensitivity(daily_insulin_units):
        insulin_sensitivity = 100 / daily_insulin_units
        return insulin_sensitivity

    def get_basal_data(glucose_data_delta, insulin_sensitivity):
        y = []

        for i in range(len(glucose_data_delta)):
            basal = glucose_data_delta[i] * insulin_sensitivity
            y.append(basal)
        return y

    def get_insulin_to_carb_ratio(daily_insulin_units, daily_carbs_intake):
        y = daily_carbs_intake / daily_insulin_units
        return y

    def get_total_insulin(basal_data, insulin_needed, eat_time):
        bolus_and_basal_insulin_data = basal_data[eat_time] + insulin_needed
        return bolus_and_basal_insulin_data

    def print_data(figure, data, graph_title, graph_position):
        x = range(0, len(data))
        y = data

        ax1 = figure.add_subplot(graph_position)
        ax1.plot(x, y)
        ax1.set_title(graph_title)