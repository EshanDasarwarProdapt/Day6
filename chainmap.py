from collections import ChainMap

student = {
    "name": "Eshan",
    "Age": 22
}

course = {
    "Course": "Python",
    "Duration": "3 months"
}

combined = ChainMap(student, course)

print(combined)
print(dict(combined))  # Convert to a regular dictionary
