def solution(age):
    return str(age).translate(str.maketrans('0123456789', 'abcdefghij'))