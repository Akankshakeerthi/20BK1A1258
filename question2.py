train_name = "chennai exp"
train_number = "234"
departure_time = {
    "Hours": 7,
    "Minutes": 30,
    "Seconds": 0
}
seats_available = {
    "sleeper": 25,
    "AC": 10
}
price = {
    "sleeper": 250,
    "AC": 1000
}
delayed_by = 2

output = f"Train: {train_name}\n"
output += f"Train Number: {train_number}\n"
output += f"Departure Time: {departure_time['Hours']}:{departure_time['Minutes']}:{departure_time['Seconds']}\n"
output += f"Seats Available: Sleeper - {seats_available['sleeper']}, AC - {seats_available['AC']}\n"
output += f"Price: Sleeper - {price['sleeper']}, AC - {price['AC']}\n"
output += f"Delayed by: {delayed_by} minutes"

print(output)
train_name = "hyderabad"
train_number = "2390"
departure_time = {
    "Hours": 8,
    "Minutes": 30,
    "Seconds": 0
}
seats_available = {
    "sleeper": 35,
    "AC": 10
}
price = {
    "sleeper": 250,
    "AC": 1000
}
delayed_by = 1

output1 = f"Train: {train_name}\n"
output1 += f"Train Number: {train_number}\n"
output1 += f"Departure Time: {departure_time['Hours']}:{departure_time['Minutes']}:{departure_time['Seconds']}\n"
output1 += f"Seats Available: Sleeper - {seats_available['sleeper']}, AC - {seats_available['AC']}\n"
output1 += f"Price: Sleeper - {price['sleeper']}, AC - {price['AC']}\n"
output1 += f"Delayed by: {delayed_by} minutes"

print(output1)

