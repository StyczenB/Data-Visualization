'''from die import Die
import pygal

# Create two D6 (six-sided die)
die_1 = Die()
die_2 = Die()

# Make a few rolls and store results in a list.
results = []
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]
	
# Analyze frequencies of numbers
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 (six-sided die) 1000 times"
hist.x_labels = [str(value) for value in range(2, max_result+1)]
#hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')'''

###########################################################################
# Two D8

from die import Die
import pygal

# Create two D8
die_1 = Die(8)
die_2 = Die(8)

num_rolls = 1000000
# Make a few rolls and store results in a list.
results = []
results = [die_1.roll() + die_2.roll() for roll_num in range(num_rolls)]
	
# Analyze frequencies of numbers
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D8 " + str(num_rolls) + " times"
hist.x_labels = [str(value) for value in range(2, max_result+1)]
#hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('dice_visual.svg')






