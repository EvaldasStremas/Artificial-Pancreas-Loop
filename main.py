import random
import matplotlib.pyplot as plt
from inputs import FIRST_GLUCOSE_READING, cycles, daily_insulin_units, daily_carbs_intake
from functions import get_glucose_data, get_glucose_data_delta, get_insulin_sensitivity, get_basal_data, print_data, insulin_to_carb_ratio

def total_insulin(data, time, basal_data, insulin_needed, cycles):
    for i in range(cycles):
        if time == i:
            total_insulin_amount = basal_data[i] + insulin_needed
    return total_insulin_amount

glucose_data = get_glucose_data(FIRST_GLUCOSE_READING, cycles)
# print(glucose_data)

glucose_data_delta = get_glucose_data_delta(glucose_data, cycles)
# print(glucose_data_delta)

insulin_sensitivity = get_insulin_sensitivity(daily_insulin_units)
# print(insulin_sensitivity)

basal_data = get_basal_data(glucose_data_delta, cycles)
# print(basal_data)

# ratio = insulin_to_carb_ratio(daily_insulin_units, daily_carbs_intake)

# moment_carbs_intake = int(input("How many carbs do you eating?:  "))
# insulin_needed = moment_carbs_intake / ratio
# print("You need this amount insulin:  ", insulin_needed)
# time = int(input("When you gonna eat?:  "))
# print(time)

# ti = total_insulin(basal_data, time, basal_data, insulin_needed, cycles)
# print(ti)
# print(basal_data)

# Print graphs
fig = plt.figure()
print_data(fig, glucose_data, "Glucose data", 221)
print_data(fig, glucose_data_delta, "Delta glucose data", 222)
print_data(fig, basal_data, "Basal insulin units", 223)
plt.show()