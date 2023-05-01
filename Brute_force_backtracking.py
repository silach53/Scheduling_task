import json
with open("graph.txt", "r") as f:
    lines = f.readlines()
    graph = []
    for line in lines:
        graph.append(list(map(int, line.strip().split())))



# Read groups data
with open('groups.json') as f:
    groups = json.load(f)

# Read teachers data
with open('teachers.json') as f:
    teachers = json.load(f)

# Read classrooms data
with open('classrooms.json') as f:
    classrooms = json.load(f)

# Read classrooms data
with open('lessons.json') as f:
    lessons = json.load(f)



def isSafe(vertex, graph, color, c):
    # Function to check if it is safe to assign the given color to the current vertex
    for i in range(len(graph)):
        # Check if there is an edge between the current vertex and i, and if the color of i is the same as the given color
        if graph[vertex][i] and color[i] == c:
            return False
    return True

def graphColoringUtil(graph, numColors, color, vertex):
    # Backtracking function to solve the graph coloring problem
    # If all vertices have been assigned a color, return True
    if vertex == len(graph):
        return True

    # Try assigning different colors to the current vertex
    for c in range(1, numColors+1):
        # Check if it is safe to assign color c to the current vertex
        if isSafe(vertex, graph, color, c):
            # Assign color c to the current vertex
            color[vertex] = c

            # Move to the next vertex
            if graphColoringUtil(graph, numColors, color, vertex + 1):
                return True

            # If assigning color c doesn't lead to a solution, backtrack and remove the color assignment
            color[vertex] = 0

    # If no color can be assigned to the current vertex, return False
    return False

def graphColoring(graph, numColors, color):
    # Function to find the minimum number of colors needed to color the graph
    return graphColoringUtil(graph, numColors, color, 0)

numColors = 5
color = [0] * len(graph)

graphColoring(graph, numColors, color)

def assign_classrooms(lessons, classrooms, color):
    assigned_classrooms = [0] * len(lessons)
    for i, lesson in enumerate(lessons):
        group_size = groups[lesson["group"] - 1]['students']
        required_features = lesson["features"]
        time_slot = color[i]

        # Find available classrooms for the current time slot
        available_classrooms = [
            c
            for c in classrooms
            if c['capacity'] >= group_size
            and all(f in c['features'] for f in required_features)
            and c['id'] not in [assigned_classrooms[j] for j, t in enumerate(color) if t == time_slot]
        ]

        # If there are no available classrooms, the solution is not possible
        if not available_classrooms:
            return None

        # Assign the first available classroom to the lesson
        assigned_classrooms[i] = available_classrooms[0]['id']

    return assigned_classrooms

assigned_classrooms = assign_classrooms(lessons, classrooms, color)
if assigned_classrooms:
    for i in range(len(color)):

        strr=[lessons[i]['features'],
              f"{lessons[i]['teacher']:<2}",
              f"{lessons[i]['group']:<2}",
              f"{assigned_classrooms[i]:<2}",
              f"{color[i]:<1}",f"{i + 1 :<2}"]
        
        """
30: black
31: red
32: green
33: yellow
34: blue
35: magenta
36: cyan
37: white
""" 
        color_of_output=35
        strf=[f"\033[{color_of_output}m{x}\033[0m" for x in strr]
        print(f"Занятия {strf[5]}, его время {strf[4]} и аудитория {strf[3]}, уточнения  Группа:{strf[2]}, Преподаватель:{strf[1]} , Необходимые особенности:{strf[0]:<37}")
        #print(f"Занятия {strf[5]}, его время {strf[4]} и аудитория {strf[3]}, уточнения  Группа:{strf[2]},{strf[1]},{strf[0]:>37},{classrooms[assigned_classrooms[i]-1].features}")
else:
    print("Solution does not exist.")