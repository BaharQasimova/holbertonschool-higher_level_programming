#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    """Serialize the Python dictionary 'data' to JSON and save it to 'filename'."""
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """Load JSON data from 'filename' and deserialize it into a Python dictionary."""
    with open(filename, 'r') as f:
        return json.load(f)