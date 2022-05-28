courses = ['History', 'Programming', 'Math', 'Literature', 'Physic', 'Math', 'Math']
numbers = [2, 5, 23, 53, 231, 123, 12]

people = [('Roman', 'Smith', 34, 'Male'), ('Mary', 'Gold', 25, 'Female'), ('Jack', 'Jones', 23, None)]

result = []
for num in range(1000):
    if (num ** 2) % 2 == 0:
        result.append(num)
print(result)


# for person in people:
#     print(f'This is {person[0]} {person[1]}. He is {person[2]} years old.')


# for name, surname, age, gender in people:
#     if gender == 'Male':
#         print(f'This is {name} {surname}. He is {age} years old.')
#     elif gender == 'Female':
#         print(f'This is {name} {surname}. She is {age} years old.')
#     else:
#         for letter in name:
#             print(letter)

# cnt = 0
# for num1 in range(10):
#     for num2 in range(10):
#         for num3 in range(10):
#             for num4 in range(10):
#                 print(num1, num2, num3, num4)
#                 cnt += 1
#
#
# print(cnt)
