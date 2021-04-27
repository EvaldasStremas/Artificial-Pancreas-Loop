import random
import matplotlib.pyplot as plt
from inputs import FIRST_GLUCOSE_READING, cycles, daily_insulin_units, daily_carbs_intake
from functions import get_glucose_data, get_glucose_data_delta, get_insulin_sensitivity, get_basal_data, print_data, insulin_to_carb_ratio, total_insulin, glucose_data, get_glucose_data_delta, insulin_sensitivity, ratio, basal_data, glucose_data_delta

moment_carbs_intake = int(input("How many carbs do you eating?:  "))
insulin_needed = moment_carbs_intake / ratio
# print("You need this amount insulin:  ", insulin_needed)
eat_time = int(input("When you gonna eat?:  "))

total_insulin_data = total_insulin(basal_data, insulin_needed, eat_time)

# Print graphs
fig = plt.figure()
print_data(fig, glucose_data, "Glucose data", 221)
print_data(fig, glucose_data_delta, "Delta glucose data", 222)
print_data(fig, basal_data, "Basal insulin units", 223)
print_data(fig, total_insulin_data, "Total basal and bolus insulin units", 224)
plt.show()