from pathlib import Path
import json

# Forma 1:
# numbers = [2, 3, 5, 7, 11, 13]

# path = Path('numbers.json')
# contents = json.dumps(numbers)
# path.write_text(contents)


# Forma 2:
# path = Path('numbers.json')
# contents = path.read_text()
# numbers = json.loads(contents)

# print(numbers)


# Forma 3:
# username = input("What is your name?")

# path = Path('username.json')
# contents = json.dumps(username)
# path.write_text(contents)

# print(f"We'll remember you when you come back, {username}!")


# Forma 4:
def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
    # if path.exist():
    #     contents = path.read_text()
    #     username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        # username = input("What is your name?")
        # contents = json.dumps(username)
        # path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")

greet_user()