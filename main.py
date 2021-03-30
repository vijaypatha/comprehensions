number = [1, 2, 3]
# increase the list by 1
new_list = []

for n in number:
    new_number = n+1
    new_list.append(new_number)
print(f"new_list is {new_list}")



# List Comprehension

New_list = [item+1 for item in number]
print(f"New_list with list_comprehension is {New_list}")

target_range = []
for n in range(1, 5):
    new_list_rage = n * 2
    target_range.append(new_list_rage)
print(target_range)

lc_new_list = [item*3 for item in range(1, 5)]

print(f"lc new list is {lc_new_list}")

names = ["heidi", "vijay", "indi"]

print([item for item in names if len(item) < 5])

print([item.upper() for item in names if len(item) > 4])

print([item*item for item in number])

print([item for item in number if item % 2 == 0])


set1 = [3, 6, 5, 8, 33, 12, 7, 4, 72, 2, 42, 13]
set2 = [3, 6, 13, 5, 7, 89, 12, 3, 33, 34, 1, 344, 42]

print([item for item in set1 if item in set2])

print(list(set(set1).intersection(set2)))

# text files: Opening

with open("file1.txt") as file1:
    file1_data = file1.readline()