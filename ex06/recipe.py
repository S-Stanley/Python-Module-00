#!/usr/bin/python3

cookbook = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}

def print_all_recipe_name():
    for cook in cookbook:
        print(cook)

def print_details_recipe(recipe_name: str):
    for cook in cookbook:
        if cook == recipe_name:
            print(cookbook[cook])

def delete_recipe(recipe_name: str):
    print(len(cookbook))
    del cookbook[recipe_name]

def add_recipe():
    name = input('Enter a name: ')
    ingredients = input('Enter ingredients: ')
    prep = input('Enter a preparation time: ')
    meal_type = input('Enter a meal type: ')

    if not prep.isnumeric() or int(prep) < 0:
        print("ERROR: prep time shoud be int positive")
        exit(1)
    if name.strip() == '':
        print("ERROR: name cannot be empty")
        exit(1)
    if meal_type.strip() == '':
        print("ERROR: meal type cannot be empty")
        exit(1)

    cookbook[name] = {
        "ingredients": ingredients.split('\\n'),
        "meal": meal_type,
        "prep_time": int(prep)
    }


def ask():
    print('List of available option:')
    print('1: Add a recipe')
    print('2: Delete a recipe')
    print('3: Print a recipe')
    print('4: Print the cookbook')
    print('5: Quit')
    choice = input()
    if choice == '1':
        add_recipe()
    elif choice == '2':
        delete_recipe(input('Recipe name: '))
    elif choice == '3':
        print_details_recipe(input('Recipe name: '))
    elif choice == '4':
        print_all_recipe_name()
    elif choice == '5':
        exit(0)
    else:
        print('ERROR: please retry')
    ask()

print('Welcome to the Python Cookbook !')
ask()

