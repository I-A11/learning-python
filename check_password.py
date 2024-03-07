def check_password(new_password):
    correct_password = 'ABC123'
    if new_password == correct_password:
        print('Your password is correct')
        return True
    else:
        ('Invalid password')
        return False
    

def main():
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        new_password = input('Enter your password: ')
        if check_password(new_password):
            break

        else:
            attempts += 1
            remaining_attempts =  max_attempts - attempts
            if remaining_attempts > 0:
                print(f'You have {remaining_attempts} attempts left')

    if attempts == max_attempts:
        print('You have exceeded the maximum number of attempts.')

main()