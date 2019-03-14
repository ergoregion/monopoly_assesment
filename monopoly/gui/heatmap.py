import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def heatmap_matrix(model):
    fig, ax = plt.subplots()
    im = ax.imshow(model.transmission_matrix, cmap="hot")

    # We want to show all ticks...
    ax.set_xticks(np.arange(model.dof))
    ax.set_yticks(np.arange(model.dof))
    # ... and label them with the respective list entries
    ax.set_xticklabels(model.states)
    ax.set_yticklabels(model.states)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    #for i in range(model.dof):
    #    for j in range(model.dof):
    #        text = ax.text(j, i, model.transmission_matrix[i, j],
    #                   ha="center", va="center", color="w")

    ax.set_title("Complete transmission matrix")
    fig.tight_layout()
    plt.show()
