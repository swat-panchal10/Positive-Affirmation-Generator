import random

mood_affirmations = {
    "happy": [
        "Keep shining, your light is contagious!",
        "Joy is your superpower.",
        "You’re doing amazing, keep smiling!"
    ],
    "sad": [
        "This too shall pass.",
        "You are stronger than you think.",
        "Even the darkest night will end and the sun will rise."
    ],
    "anxious": [
        "Breathe in peace, breathe out stress.",
        "You are safe, you are calm.",
        "Everything is going to be okay."
    ],
    "angry": [
        "Let go of what you can't control.",
        "Peace begins with you.",
        "Your calm mind is your strength."
    ],
    "tired": [
        "Rest is productive.",
        "You deserve to take it slow today.",
        "Recharging is essential, not optional."
    ],
    "default": [
        "You are loved. You are enough.",
        "Every day is a new beginning.",
        "Believe in your brilliance."
    ]
}

emojis = {
    "happy": "😊",
    "sad": "😢",
    "anxious": "😰",
    "angry": "😡",
    "tired": "😴",
    "default": "🌟"
}

def get_affirmation(emotion):
    for mood in mood_affirmations:
        if mood in emotion:
            return {
                "mood": mood,
                "affirmation": random.choice(mood_affirmations[mood]),
                "emoji": emojis[mood]
            }
    return {
        "mood": "default",
        "affirmation": random.choice(mood_affirmations["default"]),
        "emoji": emojis["default"]
    }
