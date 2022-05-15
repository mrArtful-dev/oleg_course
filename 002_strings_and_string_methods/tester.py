user_input = input('Please choose\n'
                   '1.Print hello\n'
                   '2.Print world\n'
                   '--> ')

if user_input == '1':
    print('Hello')
elif user_input == '2':
    print('World')
else:
    print('Choice is out of range')