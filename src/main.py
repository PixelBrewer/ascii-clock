#!/usr/bin/python

import sys

def main():
    print (ascii_zero + ' ' + ascii_one + ' ' + ascii_two + ' ' + ascii_three + ' ' + ascii_four + ' ' + ascii_five + ' ' + ascii_six + ' ' + ascii_seven + ' ' + ascii_eight + ' ' + ascii_nine)

ascii_one = """
1111
  11
  11
  11
111111
"""

ascii_two ="""
 2222
22  22
   22
  22
222222
"""

ascii_three = """
333333
    33
333333
    33
333333
"""

ascii_four = """
44  44
44  44
444444
    44
    44
"""
 
ascii_five = """
555555
55
55555
    55
55555
"""

ascii_six = """
666666
66
666666
66  66
666666
"""

ascii_seven = """
777777
   77
  77
 77
77
"""

ascii_eight = """
888888
88  88
888888
88  88
888888
"""

ascii_nine = """
999999
99  99
999999
    99
999999
"""

ascii_zero = """
 0000
00  00
00  00
00  00
 0000
"""

if __name__ == '__main__':
    main()


