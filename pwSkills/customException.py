class AgeValidationError(Exception):
    """Custom exception for age validation"""
    def __init__(self, msg):
        self.msg = msg

def validate_age(age):
    if age < 0:
        raise AgeValidationError("Age cannot be negative")
    elif age > 150:
        raise AgeValidationError("Age cannot be more than 150")
    else:
        print("Age is valid")

try:
    age = int(input("Enter your age: "))
    validate_age(age)
except AgeValidationError as e:
    print(e.msg)
