import matplotlib.pyplot as plt
import numpy as np


# Fixing random state for reproducibility
np.random.seed(19680801)

def read_data():
    """Generate fake data"""
    x = np.random.random(1000)
    y = np.random.random(1000)

    return x, y


def process_data(x, y):
    # pretend to do something with it
    return x, y


def plot_data(x: list, y: list, fname: str):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(x, y, 'o')
    #plt.show()
    fig.savefig(f'plots/{fname}.png')
    plt.close(fig)


for alpha in range(50):
    x, y = read_data()
    x, y = process_data(x, y)
    plot_data(x, y, str(alpha))