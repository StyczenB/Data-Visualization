import matplotlib.pyplot as plt 
from random_walk import RandomWalk

# Keep making new random walks unless write 'n' when asked.
while True:
    # Make a random walk and plot the points.
    rw = RandomWalk()
    rw.fill_walk()
    
    # Set the size of the plotting window.
    plt.figure(dpi=128, figsize=(10, 6))
    point_number = list(range(rw.num_points))
    #plt.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues, edgecolor='none', s=1)
    plt.plot(rw.x_values, rw.y_values, linewidth=1)    

    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()

    keep_running = input("Make another random walk? (y/n): ")
    if keep_running == 'n':
        break