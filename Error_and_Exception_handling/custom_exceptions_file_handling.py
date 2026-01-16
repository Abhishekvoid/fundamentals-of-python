
# Raising Your own Errors

def divide_safe(a,b):
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    
    return a/b

try:
    print(divide_safe(10, 10))
except ZeroDivisionError as e:
    print(f"Caught: {e}")

# custom Exceptions

class validatorError(Exception):
    """base validation error"""
    pass

class EmailInvalidError(validatorError):
    def __init__(self, email):
        self.email = email
        super().__init__(f"invalid email format: {email}")

class UserExistsError(validatorError):
    def __init__(self,  username):
        super().__init__(f"User '{username}' alredy exists")
    

def register_email(email, username):
    if "@" not in email:
        raise EmailInvalidError(email)
    if username == "admin":
        raise UserExistsError(username)
    print("user registered!")

# file handling + exceptions

import json
import os
from pathlib import Path

class ConfigError(Exception):
    pass

class ConfigFileNotFound(ConfigError):
    pass

class ConfigParseError(ConfigError):
    pass

def load_config(config_path):
    """Production config loader with full error handling"""
    config_path = Path(config_path)
    
    try:
        if not config_path.exists():
            raise ConfigFileNotFound(f"Config not found: {config_path}")
        
        with open(config_path, 'r') as f:  # Auto-close!
            return json.load(f)
            
    except json.JSONDecodeError as e:
        raise ConfigParseError(f"Invalid JSON in {config_path}: {e}")
    except PermissionError:
        raise ConfigError(f"No permission to read {config_path}")
    except Exception as e:
        raise ConfigError(f"Unexpected error loading {config_path}: {e}")

# Production usage:
try:
    config = load_config("settings.json")
    print("Config loaded:", config)
except ConfigFileNotFound:
    print("Create default config")
except ConfigParseError as e:
        print(f"Fix JSON: {e}")
finally:
    print("Cleanup complete")