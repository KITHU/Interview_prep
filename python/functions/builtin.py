# https://www.programiz.com/python-programming/methods/built-in/bytearray
# any() return true if there is a true value in an interable else 
# return false while all() returns true if all are true else returns false

Str = 'alpha2'
print(any(a.isdigit() for a in Str)) # return True since 2 is a num
print(all(a.isdigit() for a in Str)) # return False since 2 is a digit and others are not

# abs() returns absolute value
print(abs(-20)) # prints 20 
print(abs(-3 -4j)) # prints 5.0 which is the magnitude

# ascii() returns representation of ascii characters escaping none ascii
print(ascii('pythön')) # prints 'pyth\xf6n'
print('pyth\xf6n') # prints pythön
 
# bin() returns binary replisentation of an interger with prefix ob
print(bin(78)) # return 0b1001110

# bool()  returns False if value is empty or false else True
print(bool(1)) # print True
print(bool(0)) # print False

 
