import requests
import random
import html

EDUCATION_CATEGORY_ID = 9
API_URL = f"https://opentdb.com/api.php?amount=10&type=multiple"

def get_educational_questions():
    try:
        response = requests.get(API_URL, timeout = 10)
        print("Status code:", response.status_code)
        if response.status_code == 200:
            data = response.json()
            if data['response_code'] == 0 and data['results']:
                return data['results']
            else:
                print("No question found")
                return[]
        else:
            print("Failed to fetch educational questions.")
            return[]
    except requests.exceptions.RequestExceptions as e:
        print("Error:", e)
        return[]
questions = get_educational_questions()
print(questions)

