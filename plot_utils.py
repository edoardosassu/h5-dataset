import numpy as np
import matplotlib.pyplot as plt


def show_frame(frame: np.ndarray, title=None):
    fig = plt.figure()
    plt.imshow(frame, cmap='jet', clim=(17, 39))
    if title is not None:
        plt.title(title)
    plt.axis('off')
    plt.show()
    plt.close(fig)