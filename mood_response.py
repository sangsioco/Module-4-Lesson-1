# mood_responses.py

def mood_response(mood):
    mood = mood.lower()
    responses = {
        "happy": "That's great to hear! Keep smiling!",
        "sad": "I'm sorry to hear that. I hope things get better soon.",
        "excited": "That's awesome! Enjoy the excitement!",
        "angry": "Take a deep breath. It's going to be okay.",
        "tired": "You should get some rest. Take care of yourself.",
        "nervous": "Try to stay calm. You've got this!"
    }
    
    return responses.get(mood, "I don't have a response for that mood, but I'm here for you!")

