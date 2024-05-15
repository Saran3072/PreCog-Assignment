import matplotlib.pyplot as plt

class Plotter:
    """
    Plots various graph properties over time.
    """

    @staticmethod
    def plot_properties(properties):
        """
        Plots the given properties over time.

        Args:
            properties (dict): The properties to plot, keyed by property name.
        """
        plt.figure(figsize=(10, 8))
        for key in properties:
            if key != 'dates':
                plt.plot(properties['dates'], properties[key], label=key)
        plt.legend()
        plt.xlabel('Time')
        plt.ylabel('Graph Properties')
        plt.title('Graph Properties Over Time')
        plt.show()
