# # `new_dict = {new_key : new_item for item in list}` a list
# names = ["heidi", "indi", "Vijay"]
# import random
#
# students_score = {student: random.randint(35, 100) for student in names}
# print(students_score)
#
# # `new_dict = {new_key : new_item for (key, value) in dict.items()}`
#
# past_dict = {student: students_score for (student, students_score) in students_score.items() if students_score > 75}
# print(past_dict)

names = ["Vijay", "Heidi", "Indi"]
import random

students_score = {student: random.randint(35, 100) for student in names}
# new_dict = {new_key: new_value for item in list}
print(students_score)

past_dict = {student: students_score for (student, students_score) in students_score.items() if students_score > 75}
# new_dict = {new_key: new_value for (key, value) in dict.item()}
print(past_dict)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
word_list = sentence.split()
result = {word: len(word) for word in word_list}
print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# Write your code 👇 below:

weather_f = {weather: ((temp_c * 9/5) + 32) for(weather, temp_c) in weather_c.items()}
# new_dict = {new_key: new_value for (key, value) in dict.item()}


print(weather_f)