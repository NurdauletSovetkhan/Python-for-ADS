import json
import random

def load_questions(source):
    if source == "Midterm":
        with open("mid.json") as f:
            return json.load(f)
    elif source == "Final":
        with open("end.json") as f:
            return json.load(f)
    elif source == "Both":
        with open("mid.json") as f1, open("end.json") as f2:
            return json.load(f1) + json.load(f2)

def get_random_questions(all_qs, count):
    return random.sample(all_qs, count)
