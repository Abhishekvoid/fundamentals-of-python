
# 1. Raising Your own Errors

def divide_safe(a,b):
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    
    return a/b

try:
    print(divide_safe(10, 10))
except ZeroDivisionError as e:
    print(f"Caught: {e}")

# 2. custom Exceptions

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

# 3. file handling + exceptions

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


# 4. context manager + exceptions

class DatabaseConnection:
    def __enter__(self):
        self.conn =  sqlite3.connect('app.db')
        return self.conn
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
        return True

with DatabaseConnection() as db:
    db.excute("Insert into users...")

# 4.1 logging + sentry Intergration

import logging
logger = logging.getLogger(__name__)

def process_payment(amount):
    try:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        # Payment logic...
    except ValueError as e:
        logger.warning(f"Payment validation failed: {e}")
        raise
    except Exception as e:
        logger.error(f"Payment failed: {e}", exc_info=True)
        sentry.capture_exception(e)
        raise PaymentProcessingError("Payment gateway error")
    
# Real-World Examples
# Example 1: API Rate Limiter.
class RateLimitExceeded(Exception):
    pass

class APIRateLimiter:
    def __init__(self, max_requests=100):
        self.max_requests = max_requests
        self.count = 0
    
    def check_limit(self):
        self.count += 1
        if self.count > self.max_requests:
            raise RateLimitExceeded(f"Max {self.max_requests} requests exceeded")