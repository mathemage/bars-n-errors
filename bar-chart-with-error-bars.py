"""
========
Barchart
========

A bar plot with error bars and height labels on individual bars
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use('ggplot')


def bar_n_errors_plot(number_of_variants=2):
    latency_jama = (705.364, 691.045)
    errors_jama = (50.947, 60.670)
    latency_mtj = (140.828, 156.375)
    errors_mtj = (96.366, 112.684)

    fig, ax = plt.subplots()
    ax.set_title('PCA performance - JIRA dataset')
    ind = np.arange(number_of_variants)  # the x locations for the groups
    width = 0.35  # the width of the bars

    rects1 = ax.bar(ind, latency_jama, width, color='b', yerr=errors_jama)
    rects2 = ax.bar(ind + width, latency_mtj, width, color='r', yerr=errors_mtj)
    ax.set_ylabel('Throughput [ms/op]')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels((
        'WideData - Training 5',
        'WideData - Training 6',
    ), rotation='45')
    ax.legend((rects1[0], rects2[0]), ('Jama', 'netlib-java'))
    plt.show()


bar_n_errors_plot()
