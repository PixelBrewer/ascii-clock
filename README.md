# ascii-clock

A simple digital clock using ascii art

## Idea

The idea to create a perpetual clock using ascii art in the terminal came from my need to have a clock on a second monitor while gaming. I game on Pop!\_OS and unfortunately, the clock on the top bar is not always visible. I wanted to have a clock that would be visible at all times, even when I am in fullscreen mode.

## Example design

To create an ASCII art digital clock for your terminal, you can use code in a language like Python or a similar language that supports printing to the terminal. The core idea is to represent each digit as a series of ASCII characters (e.g., lines, dashes, and spaces) that form a 7-segment display-like pattern.
Here's a breakdown of the steps:

1. Define Digit Representations:
   Create a dictionary or a list that maps each digit (0-9) to its ASCII art representation.
   Each digit can be represented as a 3x4 or 4x3 grid of characters, typically using characters like \_, |, and spaces.
   For example:
   Code

digits = {
0: [" _ ",
"| |",
"| |",
" _ "],
1: [" |",
" |",
" |",
" |"], # ... and so on for other digits
} 2. Get the Current Time:
Use a library or function to retrieve the current hour and minute.
Example using Python's datetime module:
Python

import datetime
current_time = datetime.datetime.now()
hour = current_time.hour
minute = current_time.minute 3. Format Time as a String:
Convert the hour and minute into a string, ensuring they are padded with leading zeros if needed.
Example:
Python

hour_str = str(hour).zfill(2)
minute_str = str(minute).zfill(2) 4. Print the Clock:
Iterate through the digits of the hour and minute strings, using the defined digit representations to print each digit.
Example:
Python

def print_clock(hour, minute): # ... (Define digit representations as shown above) ...

    for row_num in range(4):
        for digit_num in range(len(hour_str)):
            digit_index = int(hour_str[digit_num])
            print(digits[digit_index][row_num], end=" ")
        print("  ", end="")  # Add spacing between hours and minutes
        for digit_num in range(len(minute_str)):
            digit_index = int(minute_str[digit_num])
            print(digits[digit_index][row_num], end=" ")
        print()

5. Update the Clock:
   To make it a dynamic clock, you'll need to call the print_clock function in a loop, refreshing it periodically (e.g., every second).
   Use time.sleep() to pause before updating the clock.
   Example Python Code (Simplified):
   Python

import datetime
import time

def print*clock(hour, minute):
digits = {
0: [" * ", "| |", "| |", " \_ "],
1: [" |", " |", " |", " |"], # ... and so on for other digits
}
hour_str = str(hour).zfill(2)
minute_str = str(minute).zfill(2)

    for row_num in range(4):
        for digit_num in range(len(hour_str)):
            digit_index = int(hour_str[digit_num])
            print(digits[digit_index][row_num], end=" ")
        print("  ", end="")
        for digit_num in range(len(minute_str)):
            digit_index = int(minute_str[digit_num])
            print(digits[digit_index][row_num], end=" ")
        print()

while True:
current_time = datetime.datetime.now()
hour = current_time.hour
minute = current_time.minute
print_clock(hour, minute)
time.sleep(1) # Refresh every second
#Clear the terminal for the next update (optional, may need adaptation for different terminal emulators)
#print('\033[H\033[2J') # This command clears the terminal in many environments
Key Considerations:
Font and Character Set: The choice of characters and their arrangement will determine the style and appearance of the clock.
