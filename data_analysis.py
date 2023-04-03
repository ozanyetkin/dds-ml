import math
import statistics

# Reading the data from text file
with open("weather_data.txt") as f:
    lines = f.readlines()

# Preprocessing the data
weather_data = []
for line in lines:
    line = float(line.replace("\n", ""))
    weather_data.append(line)

# Calculating the mean
weather_sum = 0
weather_count = 0
for data in weather_data:
    weather_sum += data
    weather_count += 1

mean_weather = weather_sum / weather_count
print(f"Mean of the data is: {mean_weather}")

# Calculating the median
sorted_data = sorted(weather_data)
middle = (len(sorted_data) - 1) // 2

if middle % 2:
    median_weather = sorted_data[middle]
else:
    median_weather = (sorted_data[middle] + sorted_data[middle + 1]) / 2

print(f"Median of the data is: {median_weather}")

# Calculating the standard deviation
# https://www.google.com/search?q=standard+deviation+formula
variance_weather = sum((x - mean_weather) ** 2 for x in weather_data) / len(
    weather_data
)
standard_deviation = math.sqrt(variance_weather)

print(f"Standard deviation of the data is: {standard_deviation}")

# Calculating the correlation factor
# https://www.google.com/search?q=pearson+correlation+formula
days_data = list(range(1, len(weather_data) + 1))
mean_days = sum(days_data) / len(days_data)

covariance_weather = sum(
    (x - mean_weather) * (y - mean_days) for x, y in zip(weather_data, days_data)
) / math.sqrt(
    sum((x - mean_weather) ** 2 for x in weather_data)
    * sum((y - mean_days) ** 2 for y in days_data)
)

print(f"Correlation factor of the data is: {covariance_weather}")

# But! You actually don't need to reinvent the wheel in programming :)
mean_weather = statistics.mean(weather_data)
print(f"Mean of the data is: {mean_weather}")

median_weather = statistics.median(weather_data)
print(f"Median of the data is: {median_weather}")

standard_deviation = statistics.pstdev(weather_data)
print(f"Standard deviation of the data is: {standard_deviation}")

covariance_weather = statistics.correlation(weather_data, days_data)
print(f"Correlation factor of the data is: {covariance_weather}")
