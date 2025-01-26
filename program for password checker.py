username=input('what is your username?')
password=input('what is your password?')
password_length=len(password)
hidden_password='*' * password_length
print(f'{username},your password,{hidden_password}')#is {password_length}letters long'