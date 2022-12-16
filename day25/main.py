# with open("weather_data.csv") as weather_data:
#     days_weather = weather_data.readlines()
#
#
# print(days_weather)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import math
# print(type(data))
# print(data["temp"])

# print(data["temp"].mean())
#
# print(data["temp"].max())

# monday = data[data.day == "Monday"]
# monday_fahr = (monday.temp * 1.8) + 32
# print(monday_fahr)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = 0
cinnamon = 0
black = 0
fur_Colors = data["Primary Fur Color"]

#or grey_squirrels_count = len(data[data["Primary Fur Color"]) for each color
for squirrel in range(len(fur_Colors)):
    if fur_Colors[squirrel] == "Gray":
        gray += 1
    elif fur_Colors[squirrel] == "Cinnamon":
        cinnamon += 1
    elif fur_Colors[squirrel] == "Black":
        black += 1

data_dict = {
    'gray': [gray],
    'cinnamon' : [cinnamon],
    'black' : [black],
}

data_to_write = pandas.DataFrame(data_dict)
data_to_write.to_csv("color_data.csv")






