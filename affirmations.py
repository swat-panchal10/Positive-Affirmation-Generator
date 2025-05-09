import random

affirmation_bank = {
    "happy": [
        "Keep spreading your light—it’s contagious!",
        "Your joy uplifts everyone around you!"
    ],
    "sad": [
        "You are stronger than your sadness.",
        "Even the darkest night will end and the sun will rise."
    ],
    "angry": [
        "Breathe. You are in control of your emotions.",
        "Let go and allow peace to flow in."
    ],
    "anxious": [
        "You are safe, calm, and grounded.",
        "One step at a time—you’ve got this."
    ],
    "motivated": [
        "Your passion fuels your greatness!",
        "You're unstoppable—keep pushing forward!"
    ],
    "tired": [
        "Rest is productive. Recharge and shine again.",
        "Take a pause—you deserve it."
    ],
    "stressed": [
        "You are doing your best, and that’s enough.",
        "Peace is within reach—just breathe."
    ],
    "neutral": [
        "Every day is a fresh start.",
        "Believe in your potential—amazing things await."
    ]
}

def get_affirmation(emotion):
    return random.choice(affirmation_bank.get(emotion, affirmation_bank["neutral"]))
