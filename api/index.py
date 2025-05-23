import json
import os

def handler(request, response):
    # Enable CORS
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"

    # Load data
    with open(os.path.join(os.path.dirname(__file__), '..', 'data.json')) as f:
        data = json.load(f)

    # Get names from query parameters
    names = request.query.getlist('name')
    # If only one name, getlist may return a string
    if isinstance(names, str):
        names = [names]

    # Create a mapping for fast lookup
    marks_map = {entry["name"]: entry["marks"] for entry in data}
    # Get marks in the order of the names provided
    marks = [marks_map.get(name, None) for name in names]

    return response.json({"marks": marks})
