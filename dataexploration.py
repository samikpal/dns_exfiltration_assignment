import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('Kafka_dataset.csv')

def plot_with_op(data, fields, width):
    for plot_no in range(len(fields)):
        plt.subplot(width, 1, plot_no)
        plt.plot(data[fields[plot_no]] )



