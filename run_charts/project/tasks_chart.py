#!/usr/bin/env python3.7
import os
from sys import exit
try:
    import numpy
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    print("Use 'pip3 install numpy; pip3 install matplotlib' first.")
    exit(1)


def read_data(file):
    try:
        with open(file, 'r') as file:
            data = []
            data.append([int(line.strip('\n').strip(' ').split(' ')[1]) for line in file])
            file.seek(0)
            data.append([line.strip('\n').strip(' ').split(' ')[0] for line in file])
            return data
    except FileNotFoundError:
        print('Where the hell is the data file? :O')
        print(f'Given file path: {file}')
        exit(1)


def get_data(data_file):
    file = os.path.join(os.path.dirname(__file__), f'{data_file}')
    data = read_data(file)
    return data


def make_calculations(data):
    mean = numpy.mean(data)
    std_dev = numpy.std(data)
    return [mean, std_dev]


def plot(data):
    tasks = data[0]
    time = [date[5:10] for date in data[1]]

    mean, std_dev = make_calculations(tasks)

    green_range = (mean - std_dev, mean + std_dev)
    red_range = (mean - 2 * std_dev, mean + 2 * std_dev)

    fig = plt.figure(1)
    ax = fig.add_subplot(111)

    ax.plot(time, tasks, '-', color='black', linewidth=1)
    ax.scatter(time, tasks, color='black', marker='o', s=5)
    ax.plot([mean for i in time], color='lightblue', linewidth=1)
    ax.plot([green_range for i in time], color='green', linewidth=1)
    ax.plot([red_range for i in time], color='red', linewidth=1)
    ax.set(title="Tasks per day", xlabel="days", ylabel="numer of tasks")
    plt.show()


def main():
    data = get_data('tasks_stat.txt')
    plot(data)


if __name__ == '__main__':
    main()

# axis x - capital numbers
