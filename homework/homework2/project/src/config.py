import sys, os
from pathlib import Path
from dotenv import load_dotenv

# load environment
# kinda wierd we need to change the name, do I need to write code to check for environment
def load_env():
    return load_dotenv()


# get key
#looks for an environment variable called name.
#If it exists → returns its value.
#If not → returns the provided default (or None if no default is given).
from typing import Optional

def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(name, default)