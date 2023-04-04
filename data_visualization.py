import numpy as np
import matplotlib.pyplot as plt

# Reading the data from text file
with open("weather_data.txt") as f:
    lines = f.readlines()

# Preprocessing the data
weather_data = []
for line in lines:
    line = float(line.replace("\n", ""))
    weather_data.append(line)

# Histogram
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
counts, bins = np.histogram(weather_data)
plt.hist(bins[:-1], bins, weights=counts)

plt.savefig("histogram.png")
plt.clf()

# Bar chart
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html
days = list(range(len(weather_data)))
plt.bar(days, weather_data)

plt.savefig("bar_chart.png")
plt.clf()

# Pie chart
# https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html
fig, ax = plt.subplots()

weather_labels = []
for weather in weather_data:
    if weather <= 5:
        weather_labels.append("cold")
    elif 5 < weather <= 12:
        weather_labels.append("just fine")
    else:
        weather_labels.append("hot")

label_occurrences = [
    weather_labels.count("cold"),
    weather_labels.count("just fine"),
    weather_labels.count("hot"),
]
ax.pie(label_occurrences, labels=["cold", "just fine", "hot"])

plt.savefig("pie_chart.png")
plt.clf()

# Time series
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
plt.plot(days, weather_data)

plt.savefig("time_series.png")
plt.clf()

# Scatter graph
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
weather_colors = []
for label in weather_labels:
    if label == "cold":
        weather_colors.append("blue")
    elif label == "just fine":
        weather_colors.append("yellow")
    else:
        weather_colors.append("red")

plt.scatter(days, weather_data, c=weather_colors)

plt.savefig("scatter_plot.png")
plt.clf()

print("Hello GitHub!")
