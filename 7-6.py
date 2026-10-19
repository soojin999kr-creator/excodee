students = {
    "name": "Kim",
    "math": 80,
    "science": 90
}

students["history"] = 90

if "math" in students:
    del students["math"]

students["science"] = 100

avg = (students["history"] + students["science"]) / 2
print(f"{students['name']}'s average score is {int(avg)}")
