number = input('Enter a number: ')
encode = ''
for i in number:
    i = int(i) + 3
    encode += str(i)
print('Encoded number:', encode)