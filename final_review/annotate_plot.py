"""
Author: Riley Palermo
"""

import matplotlib.pyplot as plt
import datetime as date


def annotate_plot(annotations: dict):
    for label, info in annotations.items():
        position = info['position']
        alignment = info['alignment']
        fontsize = info['fontsize']
        plt.text(position[0], position[1], label, horizontalalignment=alignment[0], verticalalignment=alignment[1],
                 fontsize=fontsize)


if __name__ == "__main__":
    # Test annotate_plot function
    plt.figure()
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    annotations = {
        ("Created by Riley Palermo", date.datetime.now()): {
            "position": (1, .5),
            "alignment": ['left', 'bottom'],
            "fontsize": 8
        }
    }
    annotate_plot(annotations)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Test Plot")
    plt.show()
