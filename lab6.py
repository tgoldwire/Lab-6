def encode(number):
    encode = ''
    for i in number:
        i = int(i) + 3
        encode += str(i)
    print('Encoded number:', encode)



if __name__ == '__main__':
    number = input('Enter a number: ')
    encode(number)