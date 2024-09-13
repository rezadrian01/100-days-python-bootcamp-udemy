import pandas
BASE_PATH = "section 25/demo"

# data = pandas.read_csv(f"{BASE_PATH}/weather_data.csv")
# monday_data = data[data.day == 'Monday']
# monday_temp_F = monday_data.temp * 9/5 + 32
# print(monday_temp_F)

# data_dict = {
#     "students": ['Amy', 'James', 'Angela'],
#     "scores": [76, 56, 65]
# }

# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv(f"{BASE_PATH}/new_data.csv")
# print(new_data)

data = pandas.read_csv(f"{BASE_PATH}/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])
data_dict = {
    "Fur Color": ["gray", "Cinnamon" , "black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv(f"{BASE_PATH}/squirrel_count.csv")