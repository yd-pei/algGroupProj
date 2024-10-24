import matplotlib.pyplot as plt
import csv
import os
import numpy as np

def main():
    # Load the data
    with open('time_complexity_n_with_k_fixed.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Extract the data
    n_values = [int(row[0]) for row in data[1:]]
    experimental_results = [float(row[1]) for row in data[1:]]
    theoretical_results = [float(row[2]) for row in data[1:]]
    scaling_factor = np.mean(experimental_results)*1e9 / np.mean(theoretical_results)

    scaled_theoretical_results = np.array(theoretical_results) * scaling_factor
    experimental_results_nanos = np.array(experimental_results) * 1e9
    # Plot the data
    plt.figure()
    plt.title('Time Complexity (fixed value of k)')
    plt.xlabel('n')
    plt.ylabel('Time (ns)')
    plt.plot(n_values, experimental_results_nanos, label='Experimental Results')
    plt.plot(n_values, scaled_theoretical_results, label='Theoretical Results')
    plt.grid(True)
    plt.legend()
    plt.savefig('time_complexity_n_with_k_fixed.png')
    plt.show()

    # load the second batch of data
    with open('time_complexity_k_with_n_fixed.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)


    k_values = [int(row[0]) for row in data[1:]]
    experimental_results = [float(row[1]) for row in data[1:]]
    theoretical_results = [float(row[2]) for row in data[1:]]
    scaling_factor = np.mean(experimental_results)*1e9 / np.mean(theoretical_results)

    scaled_theoretical_results = np.array(theoretical_results) * scaling_factor
    experimental_results_nanos = np.array(experimental_results) * 1e9
    # Plot the data
    plt.figure()
    plt.title('Time Complexity (fixed value of n)')
    plt.xlabel('k')
    plt.ylabel('Time (ns)')
    plt.plot(k_values, experimental_results_nanos, label='Experimental Results')
    plt.plot(k_values, scaled_theoretical_results, label='Theoretical Results')
    plt.grid(True)
    plt.legend()
    plt.savefig('time_complexity_k_with_n_fixed.png')
    plt.show()

if __name__ == '__main__':
    main()