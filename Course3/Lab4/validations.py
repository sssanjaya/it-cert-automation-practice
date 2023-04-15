import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    
    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-zA-Z0-9._]*$', username):
        return False
    # Usernames can't begin with a dot or underscore
    if username[0] in ['.', '_']:
        return False
    # Usernames can't end with a dot or underscore
    if username[-1] in ['.', '_']:
        return False
    # Usernames can't have consecutive dots or underscores
    if '..' in username or '__' in username:
        return False
    # Usernames can't have a dot or underscore immediately before or after another dot or underscore
    if '._' in username or '_. ' in username or '_.' in username or '._' in username:
        return False
    return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # False
