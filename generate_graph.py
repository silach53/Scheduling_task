class Group:
    def __init__(self, id, students):
        self.id = id
        self.students = students

class Teacher:
    def __init__(self, id, name, availability):
        self.id = id
        self.name = name
        self.availability = availability

import json

class Classroom:
    def __init__(self, id, capacity, features):
        self.id = id
        self.capacity = capacity
        self.features = features

    def to_dict(self):
        return {
            "id": self.id,
            "capacity": self.capacity,
            "features": self.features
        }

groups = [
    Group(1, 30), Group(2, 25), Group(3, 20), Group(4, 35),
    Group(5, 28), Group(6, 32), Group(7, 22), Group(8, 24),
    Group(9, 27), Group(10, 33), Group(11, 23), Group(12, 29),
    Group(13, 31), Group(14, 26), Group(15, 21), Group(16, 34),
    Group(17, 30), Group(18, 25), Group(19, 20), Group(20, 35),
]

teachers = [
    Teacher(1, "Alice", [1, 2, 3, 4, 5]),
    Teacher(2, "Bob", [1, 3, 5]),
    Teacher(3, "Charles", [2, 4]),
    Teacher(4, "David", [1, 2, 3, 4, 5]),
    Teacher(5, "Eva", [2, 3, 4]),
    Teacher(6, "Frank", [1, 3, 4, 5]),
    Teacher(7, "Grace", [1, 2, 4, 5]),
    Teacher(8, "Henry", [2, 4, 5]),
    Teacher(9, "Ivy", [1, 3, 4]),
    Teacher(10, "Jack", [1, 2, 3, 5]),
    Teacher(11, "Kim", [1, 2, 4]),
    Teacher(12, "Linda", [3, 4, 5]),
    Teacher(13, "Mike", [1, 2, 5]),
    Teacher(14, "Nina", [2, 3, 5]),
    Teacher(15, "Oscar", [1, 3, 4, 5]),
    Teacher(16, "Penny", [1, 2, 3, 5]),
    Teacher(17, "Quentin", [2, 3, 4, 5]),
    Teacher(18, "Rose", [1, 3, 5]),
    Teacher(19, "Sam", [2, 4]),
    Teacher(20, "Tina", [1, 2, 3, 4, 5]),
]

classrooms = [
    Classroom(1, 30, ["projector"]),
    Classroom(2, 25, ["projector", "whiteboard"]),
    Classroom(3, 20, ["whiteboard"]),
    Classroom(4, 35, ["projector", "whiteboard"]),
    Classroom(5, 28, ["projector"]),
    Classroom(6, 32, ["projector", "whiteboard"]),
    Classroom(7, 22, ["whiteboard"]),
    Classroom(8, 24, ["projector", "whiteboard"]),
    Classroom(9, 27, ["projector"]),
    Classroom(10, 33, ["projector", "whiteboard"]),
    Classroom(11, 23, ["whiteboard"]),
    Classroom(12, 29, ["projector", "whiteboard"]),
    Classroom(13, 31, ["projector"]),
    Classroom(14, 26, ["projector", "whiteboard"]),
    Classroom(15, 21, ["whiteboard"]),
    Classroom(16, 34, ["projector", "whiteboard"]),
    Classroom(17, 30, ["projector"]),
    Classroom(18, 25, ["projector", "whiteboard"]),
    Classroom(19, 20, ["whiteboard"]),
    Classroom(20, 35, ["projector", "whiteboard"]),
]

lessons = [
    {"group": 1, "teacher": 1, "features": ["projector"]},
    {"group": 2, "teacher": 1, "features": ["projector", "whiteboard"]},
    {"group": 3, "teacher": 2, "features": ["whiteboard"]},
    {"group": 4, "teacher": 3, "features": ["projector", "whiteboard"]},
    {"group": 5, "teacher": 4, "features": ["projector"]},
    {"group": 6, "teacher": 5, "features": ["projector", "whiteboard"]},
    {"group": 7, "teacher": 6, "features": ["whiteboard"]},
    {"group": 8, "teacher": 7, "features": ["projector", "whiteboard"]},
    {"group": 9, "teacher": 8, "features": ["projector"]},
    {"group": 10, "teacher": 9, "features": ["projector", "whiteboard"]},
    {"group": 11, "teacher": 10, "features": ["whiteboard"]},
    {"group": 12, "teacher": 11, "features": ["projector", "whiteboard"]},
    {"group": 13, "teacher": 12, "features": ["projector"]},
    {"group": 14, "teacher": 13, "features": ["projector", "whiteboard"]},
    {"group": 15, "teacher": 14, "features": ["whiteboard"]},
    {"group": 16, "teacher": 15, "features": ["projector", "whiteboard"]},
    {"group": 17, "teacher": 16, "features": ["projector"]},
    {"group": 18, "teacher": 17, "features": ["projector", "whiteboard"]},
    {"group": 19, "teacher": 18, "features": ["whiteboard"]},
    {"group": 20, "teacher": 19, "features": ["projector", "whiteboard"]},
    {"group": 1, "teacher": 19, "features": ["projector"]},
    {"group": 2, "teacher": 19, "features": ["projector", "whiteboard"]},
    {"group": 3, "teacher": 18, "features": ["whiteboard"]},
    {"group": 4, "teacher": 17, "features": ["projector", "whiteboard"]},
    {"group": 5, "teacher": 16, "features": ["projector"]},
    {"group": 6, "teacher": 15, "features": ["projector", "whiteboard"]},
    {"group": 7, "teacher": 14, "features": ["whiteboard"]},
    {"group": 8, "teacher": 13, "features": ["projector", "whiteboard"]},
    {"group": 9, "teacher": 12, "features": ["projector"]},
    {"group": 10, "teacher": 11, "features": ["projector", "whiteboard"]},
    {"group": 11, "teacher": 10, "features": ["whiteboard"]},
    {"group": 12, "teacher": 1, "features": ["projector", "whiteboard"]},
    {"group": 13, "teacher": 2, "features": ["projector"]},
    {"group": 14, "teacher": 3, "features": ["projector", "whiteboard"]},
    {"group": 15, "teacher": 4, "features": ["whiteboard"]},
    {"group": 16, "teacher": 5, "features": ["projector", "whiteboard"]},
    {"group": 17, "teacher": 6, "features": ["projector"]},
    {"group": 18, "teacher": 7, "features": ["projector", "whiteboard"]},
    {"group": 19, "teacher": 8, "features": ["whiteboard"]},
    {"group": 20, "teacher": 9, "features": ["projector", "whiteboard"]},
    {"group": 1, "teacher": 20, "features": ["projector"]},
    {"group": 2, "teacher": 19, "features": ["projector", "whiteboard"]},
    {"group": 3, "teacher": 18, "features": ["whiteboard"]},
    {"group": 4, "teacher": 17, "features": ["whiteboard"]},
    {"group": 5, "teacher": 16, "features": ["projector"]},
    {"group": 6, "teacher": 15, "features": ["whiteboard"]},
    {"group": 7, "teacher": 14, "features": ["whiteboard"]},
    {"group": 8, "teacher": 13, "features": ["whiteboard"]},
    {"group": 9, "teacher": 12, "features": ["projector"]},
    {"group": 10, "teacher": 11, "features": ["projector", "whiteboard"]},
    {"group": 11, "teacher": 10, "features": ["whiteboard"]},
    {"group": 12, "teacher": 1, "features": ["projector", "whiteboard"]},
    {"group": 13, "teacher": 2, "features": ["projector"]},
    {"group": 14, "teacher": 3, "features": ["projector", "whiteboard"]},
    {"group": 15, "teacher": 4, "features": ["whiteboard"]},
    {"group": 16, "teacher": 5, "features": ["projector", "whiteboard"]},
    {"group": 17, "teacher": 6, "features": ["projector"]},
    {"group": 18, "teacher": 7, "features": ["projector", "whiteboard"]},
    {"group": 19, "teacher": 8, "features": ["whiteboard"]},
    {"group": 20, "teacher": 19, "features": ["projector", "whiteboard"]},
]

def create_adjacency_matrix(lessons):
    n = len(lessons)
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if (
                lessons[i]["group"] == lessons[j]["group"]
                or lessons[i]["teacher"] == lessons[j]["teacher"]
            ):
                matrix[i][j] = 1
                matrix[j][i] = 1

    return matrix

graph = create_adjacency_matrix(lessons)

with open("graph.txt", "w") as f:
    for row in graph:
        f.write(" ".join(str(val) for val in row))
        f.write("\n")


import json

# Convert the groups list to JSON
groups_json = json.dumps([group.__dict__ for group in groups])

# Convert the teachers list to JSON
teachers_json = json.dumps([teacher.__dict__ for teacher in teachers])

# Convert the lessons list to JSON
lessons_json = json.dumps(lessons)

classrooms_json = json.dumps([c.to_dict() for c in classrooms])

# Write the JSON strings to files
with open("groups.json", "w") as f:
    f.write(groups_json)

with open("teachers.json", "w") as f:
    f.write(teachers_json)

with open("lessons.json", "w") as f:
    f.write(lessons_json)

with open("classrooms.json", "w") as f:
    f.write(classrooms_json)
