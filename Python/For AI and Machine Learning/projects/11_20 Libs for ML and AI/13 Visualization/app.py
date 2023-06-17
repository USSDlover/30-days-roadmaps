import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def plot_matplot():
    # Create the figure and axes
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Generate some sample data
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    # Plot the data
    ax.plot(x, y)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Line Plot')

    # Create a Tkinter window
    root = tk.Tk()
    root.title("Matplotlib in Tkinter")

    # Create a FigureCanvasTkAgg widget to display the Matplotlib plot
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()

    # Pack the widget into the window
    canvas.get_tk_widget().pack()

    # Start the Tkinter event loop
    tk.mainloop()


# Call the function to plot the graph and display it in a window
plot_graph()
