import csv
from typing import get_origin
import pandas as pd
import plotly.figure_factory as ff
import statistics as st
import random
import plotly.graph_objects as go

dfc = pd.read_csv("project.csv") 
data = dfc["reading_time"].tolist()
mean_list = []
dataSet = []


population_mean = st.mean(data)
population_std = st.stdev(data)


def show_graph(mean):
    fig = ff.create_distplot([data], ["reading_time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean], y=[0,1],  mode="lines", name="Mean"))
    fig.show()


def randomMean(counter):
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataSet.append(value)

    mean_for_dataSet = st.mean(dataSet)
    print("{} is the sample of the data".format(mean_for_dataSet))  
    
    return mean_for_dataSet


def setUp():
    for i in range(0,100):
        setOfMean = randomMean(30)
        mean_list.append(setOfMean)

    show_graph(mean_list)



# def call ----

setUp()

# def call xxxx



# print state -----

print("{} is the mean of the data".format(population_mean))
print("{} is the standard deviation of the data".format(population_std))

# print state xxxx

