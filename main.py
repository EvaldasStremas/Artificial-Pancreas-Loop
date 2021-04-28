import random
import matplotlib.pyplot as plt
from inputs import *
from functions import *
# from user_input import *

moment_carbs_intake = int(input("How many carbs do you eating?:  "))
eat_time = int(input("When you gonna eat?:  "))

# user_input()

# Print graphs
if __name__ == '__main__':
    fig = plt.figure()
    print_data(fig, glucose_data(), "Glucose data", 221)
    print_data(fig, glucose_data_delta(glucose_data()), "Delta glucose data", 222)
    print_data(fig, basal_data(glucose_data_delta(glucose_data())), "Basal insulin units", 223)
    print_data(fig, total_insulin_data(moment_carbs_intake, eat_time), "Total basal and bolus insulin units", 224)
    plt.show()