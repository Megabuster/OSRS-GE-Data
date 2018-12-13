import matplotlib.pyplot as plt
import pandas as pd

class Visualization:

    def display(self, list_to_show, **kwargs):
        df = pd.DataFrame(list_to_show)
        df.plot(kind='bar', x=kwargs['x'], y=kwargs['y'], color='green')
        plt.tight_layout()
        plt.savefig('plot.png')
