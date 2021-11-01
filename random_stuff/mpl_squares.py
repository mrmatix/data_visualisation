import matplotlib.pyplot as plt

x_values = list(range(1, 126))
y_values = [x**3 for x in x_values]
plt.plot(x_values, y_values, linewidth=5)

# set chart title and label axes
plt.scatter(x_values, y_values, c=y_values,
            cmap=plt.cm.Blues, edgecolor='none', s=50)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# set size of tick labels
plt.axis([0, 1100, 0, 1100000])
#plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()
