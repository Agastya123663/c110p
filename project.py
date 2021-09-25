import csv
import random
import statistics
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("project.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
print('The population mean is : ',population_mean)

def random_set_of_means(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["reading_time"])
    fig.show()

def setup():
    mean_list = []
    for i in range(0, 1000):
        set_of_means = random_set_of_means(30)
        mean_list.append(set_of_means)
    sample_mean = statistics.mean(mean_list)
    print('The sample mean is :',sample_mean)
    show_fig(mean_list)


setup()