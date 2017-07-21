"""
========
Barchart
========

A bar plot with errorbars and height labels on individual bars
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')


def plot1():
    N = 12
    latency_jama = (0.658, 2.310, 0.748, 1.009, 0.564, 0.552, 1.260, 1.003, 5.077, 7.640, 6.764, 7.304)
    errors_jama = (0.429, 1.111, 1.056, 1.172, 0.705, 0.779, 0.787, 0.716, 2.474, 6.329, 7.270, 4.105)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, latency_jama, width, color='b', yerr=errors_jama)
    latency_mtj = (0.781, 2.479, 2.066, 0.492, 0.568, 1.206, 2.338, 0.670, 4.111, 6.223, 5.835, 7.771)
    errors_mtj = (0.646, 1.466, 7.888, 0.667, 0.708, 2.768, 6.228, 0.487, 1.610, 4.150, 3.349, 4.570)
    rects2 = ax.bar(ind + width, latency_mtj, width, color='r', yerr=errors_mtj)
    # add some text for labels, title and axes ticks
    ax.set_ylabel('Latency [ms/op]')
    ax.set_title('Latency of benchmarks')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels((
        'Impute Missing - Scoring',
        'Impute Missing - Training',
        'WideData - Scoring 1',
        'WideData - Scoring 2',
        'WideData - Scoring 3',
        'WideData - Scoring 4',
        'WideData - Scoring 5',
        'WideData - Scoring 6',
        'WideData - Training 1',
        'WideData - Training 2',
        'WideData - Training 3',
        'WideData - Training 4',
    ), rotation='45')
    ax.legend((rects1[0], rects2[0]), ('Jama', 'netlib-java'))
    plt.show()


def plot2():
    N = 2
    latency_jama = (705.364, 691.045)
    errors_jama = (50.947, 60.670)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, latency_jama, width, color='b', yerr=errors_jama)
    latency_mtj = (140.828, 156.375)
    errors_mtj = (96.366, 112.684)
    rects2 = ax.bar(ind + width, latency_mtj, width, color='r', yerr=errors_mtj)
    # add some text for labels, title and axes ticks
    ax.set_ylabel('Latency [ms/op]')
    ax.set_title('Latency of benchmarks')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels((
        'WideData - Training 5',
        'WideData - Training 6',
    ), rotation='45')
    ax.legend((rects1[0], rects2[0]), ('Jama', 'netlib-java'))
    plt.show()


plot1()
plot2()
