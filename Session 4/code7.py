
students = [
    {
        "Name": "A",
        "Age": 12
    },
    {
        "Name": "B",
        "Age": 22
    },
    {
        "Name": "A",
        "Age": 7
    },

]


students.sort(key=lambda d: d["Age"])
print(students)
