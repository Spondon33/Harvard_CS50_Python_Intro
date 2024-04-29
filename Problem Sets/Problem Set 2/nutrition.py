fruit_calorie = [
    {"name": "apple", "calorie": "130"},
    {"name": "avocado", "calorie": "50"},
    {"name": "banana", "calorie": "110"},
    {"name": "cantaloupe", "calorie": "50"},
    {"name": "grapefruit", "calorie": "60"},
    {"name": "grapes", "calorie": "90"},
    {"name": "honeydew melon", "calorie": "50"},
    {"name": "kiwifruit", "calorie": "90"},
    {"name": "lemon", "calorie": "15"},
    {"name": "nectarine", "calorie": "60"},
    {"name": "orange", "calorie": "80"},
    {"name": "peach", "calorie": "60"},
    {"name": "pear", "calorie": "100"},
    {"name": "pineapple", "calorie": "50"},
    {"name": "plums", "calorie": "70"},
    {"name": "strawberries", "calorie": "50"},
    {"name": "sweet cherries", "calorie": "100"},
    {"name": "tangerine", "calorie": "50"},
    {"name": "watermelon", "calorie": "80"}
]

user_input = input("Item: ").lower()

for fruit in fruit_calorie:
    if fruit["name"] == user_input:
        print("Calories: " + fruit["calorie"])
