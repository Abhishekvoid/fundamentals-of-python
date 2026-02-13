"""
Validation Generator

Problem:
    - Create a generator that:
        - yields validation errors one by one
    - Stop when all validations pass

Hint: yield, lazy evaluation
"""

def validation_gen(data):

    if not data.get("username"):
        yield "username missing"
    if "@" not in data.get("email", ""):
        yield "invalid email"
    if len(data.get("password") < 8):
        yield "password lenght is short! it must contain * letters"
    
errors = list(validation_gen(data))