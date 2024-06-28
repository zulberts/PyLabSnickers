from matplotlib import pyplot as plt


def pie_plotter(values):
    keys = ["completed todos", "not completed todos"]
    plt.title("done tasks")
    plt.pie(values, labels=keys)
    plt.legend()
    plt.show()


def bar_plotter(values):
    keys = ["completed todos", "not completed todos"]
    plt.title("done tasks")
    plt.bar(keys, values)
    plt.legend()
    plt.show()
