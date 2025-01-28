dict={

    'a':1,
    'b':2
}
print(dict['b'])
dict={
    '123':[1,2,3],
    '123':'hello'
}
print(dict['123'])
user={
    'basket':[1,2,3],
    'greet':'hello'
}
print(user.get('age'))
print('basket' in user)
print('age' in user)
print('hello' in user.values())
print(user.clear())