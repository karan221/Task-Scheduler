import requests
from datetime import datetime
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def is_valid_url(url):
    """
    Helper function used to check if a string is a valid url.
    """
    validate = URLValidator()
    try:
        validate(url)
        return True
    except ValidationError:
        return False

def is_valid_datetime(datetime_str):
    """
    Helper function used to check if a datetime string is valid.
    """
    try:
        date_time = datetime.strptime(datetime_str, "%d-%m-%YT%H:%M:%S")
        now = datetime.now()
        if now > date_time:
            return False
        return True
    except:
        return False

def job(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Task Completed.")
    else:
        print("Task failed.")