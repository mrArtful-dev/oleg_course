people = [['Jack', 'Smith', 35, 'male'], ['Mary', 'Gold', 25, 'female'], ['Bob', 'Summer', 15, 'male']]

for person in people:
    if person[3] == 'male':
        print(f'This is {person[0]} {person[1]}. He is {person[2]} years old.')
    else:
        print(f'This is {person[0]} {person[1]}. She is {person[2]} years old.')
