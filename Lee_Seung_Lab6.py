def encode(number):
    encode = ''
    for i in number:
        i = int(i) + 3
        encode += str(i)
    print('Encoded number:', encode)


def decode(encoded_number):
    decoded = ''
    for digit in encoded_number:
        decoded_digit = int(digit) - 3
        decoded += str(decoded_digit)
    return decoded



if __name__ == '__main__':
    number = input('Enter a number: ')
    encode(number)

