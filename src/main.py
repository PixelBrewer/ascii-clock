#!/usr/bin/python

import datetime
import time

def main():
    def print_clock(hour, minute, is_pm):
        # Convert 24-hour format to 12-hour format
        display_hour = hour if 1 <= hour <= 12 else hour - 12
        if hour == 0:
            display_hour = 12
        digits = {
        0: [
            " 0000 ",
            "00  00",
            "00  00",
            "00  00",
            " 0000 "
        ],
        1: [
            " 1100 ",
            "   10 ",
            "   10 ",
            "   10 ",
            "111111"
        ],
        2: [
            " 2222 ",
            "    22",
            " 2222 ",
            "22    ",
            "22222 "
        ],
        3: [
            " 3333 ",
            "    33",
            " 3333 ",
            "    33",
            " 3333 "
        ],
        4: [
            "44  44",
            "44  44",
            "444444",
            "    44",
            "    44"
        ],
        5: [
            "555555",
            "55    ",
            "55555 ",
            "    55",
            "55555 "
        ],
        6: [
            " 6666 ",
            "66    ",
            "66666 ",
            "66  66",
            " 6666 "
        ],
        7: [
            "777777",
            "   77 ",
            "  77  ",
            " 77   ",
            "77    "
        ],
        8: [
            " 8888 ",
            "88  88",
            " 8888 ",
            "88  88",
            " 8888 "
        ],
        9: [
            " 9999 ",
            "99  99",
            " 99999",
            "    99",
            " 9999 "
        ]
        }
        
        hour_string = str(display_hour).zfill(2)
        minute_string = str(minute).zfill(2)
        
        # Clear screen before printing
        print("\033[2J\033[H", end="")
        
        print("\n") # Add some padding at the top
        
        for row in range(5):
            print("     ", end="")
            # Print hour digits
            for digit in hour_string:
                print(digits[int(digit)][row], end=" ")
            
            if row == 2:
                print(" :: ", end="")
            else:
                print("    ", end="")
            
            # Print minute digits
            for digit in minute_string:
                print(digits[int(digit)][row], end=" ")
            
            # Print AM/PM indicator
            if row == 2:
                print("   ", "PM" if is_pm else "AM", end="")
            print()  # New line after each row
        
        print("\n")  # Add some padding at the bottom
            
    while True:
        current_time = datetime.datetime.now()
        hour = current_time.hour
        minute = current_time.minute
        is_pm = hour >= 12
        print_clock(hour, minute, is_pm)
        time.sleep(1)

if __name__ == '__main__':
    main()