import matplotlib.pyplot as plt 

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.figure(1)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.flag, edgecolor='none', s=40)

# Set chart title and label axes.
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=24)
plt.ylabel('Square of Value', fontsize=24)

# Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
#plt.savefig('square_plot.png', bbox_inches='tight')


################################################################
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.figure(2)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.flag, edgecolor='none', s=40)

plt.show()