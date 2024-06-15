# main.py

import mood_response

mood = input("How are you feeling today? ")
response = mood_response.mood_response(mood)
print(response)
