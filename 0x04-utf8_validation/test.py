#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65] # true
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data)) # true

data = [229, 65, 127, 256]
print(validUTF8(data)) # false

data = [241, 165, 138] 
print(validUTF8(data)) # false [1111 0001, 1010 0101, 1000 1010]
                       # false because first byte signifies that the 
                       # character is 4 bytes long however data has only 3 bytes

data = [241, 165, 138, 80] 
print(validUTF8(data)) # false [1111 0001, 1010 0101, 1000 1010, 0101 0000]
                       # false because 4th byte does not follow bit pattern
                       # of continuation ie 10xx xxxx

data = [241, 165, 138, 128]
print(validUTF8(data)) # true [1111 0001, 1010 0101, 1000 1010, 1000 0000]
                       # unlike the false 1 above 4th byte here follows
                       # utf8 continuation bits pattern 

data = [241, 165, 138, 128, 241, 165, 138, 128, 65, 92, 241, 165, 138, 128]
print(validUTF8(data))  # true [
                        #       1111 0001, 1010 0101, 1000 1010, 1000 0000,
                        #       1111 0001, 1010 0101, 1000 1010, 1000 0000,
                        #       0100 0001, 0101 1100
                        #       1111 0001, 1010 0101, 1000 1010, 1000 0000,        
                        #         ]
                        # contains copies of the previous passed ones with
                        # some ascii in between

data = [241, 165, 138, 128, 241, 165, 138, 128, 65, 92, 241, 165, 138, 128, 241]
print(validUTF8(data))  # false [
                        #       1111 0001, 1010 0101, 1000 1010, 1000 0000,
                        #       1111 0001, 1010 0101, 1000 1010, 1000 0000,
                        #       0100 0001, 0101 1100
                        #       1111 0001, 1010 0101, 1000 1010, 1000 0000,
                        #       1111 0001      
                        #         ]
                        # contains copies of the previous passed ones with
                        # some ascii in between and a multibyte starter at the end
                        # without its continuation bytes

data = [248, 165, 138, 128]
print(validUTF8(data)) # false [1111 1001, 1010 0101, 1000 1010, 1000 0000]
                       # because 1st byte has no 0 bit after first 4 1s which
                       # is required to signify end of bytes count that
                       # represent multibye characters

data = [128, 165, 138, 128]
print(validUTF8(data)) # false [1000 0000, 1010 0101, 1000 1010, 1000 0000]
