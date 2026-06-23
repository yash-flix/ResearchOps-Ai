import json

def save_report(state):
    with open("output.json", "w") as f:
        json.dump(state, f, indent=2)