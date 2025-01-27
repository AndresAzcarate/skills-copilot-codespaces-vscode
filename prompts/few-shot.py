# Example 1: Greeting message for morning
# Input: 9 AM
# Output: "Good morning!"

# Example 2: Greeting message for afternoon
# Input: 2 PM
# Output: "Good afternoon!"

# Example 3: Greeting message for evening
# Input: 7 PM
# Output: "Good evening!"

# Now, generate a python code that takes the current time as input using the datetime 
# module and returns the appropriate greeting message.

#Solution:
# Import the datetime module.
from datetime import datetime

# Get the current time.
current_time = datetime.now().time()

# Get the hour from the current time.
hour = current_time.hour

# Check if it is morning, (before 12 PM).
if hour < 12:
    print("Good morning!")

# Check if it is afternoon, (between 12 PM and 5 PM).
elif hour < 17:
    print("Good afternoon!")

# Check if it is evening, (after 5 PM).
elif hour < 21:
    print("Good evening!")
    
# Else it is night.
else:
    print("Good night!")




