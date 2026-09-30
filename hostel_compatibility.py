# Hostel Roommate Compatibility System
# CSE1021 - Introduction to Problem Solving and Programming
#
# Each student answers questions about their habits.
# We compare two students and give a compatibility score out of 100.

students = []   # every student is a dictionary stored in this list

def ask_number(question, low, high):
    # keeps asking until the user types a valid number
    while True:
        text = input(question)
        if text.isdigit():
            n = int(text)
            if n >= low and n <= high:
                return n
        print("Please enter a number from", low, "to", high)

def ask_yes_no(question):
    while True:
        ans = input(question + " (y/n): ")
        if ans == "y" or ans == "Y":
            return 1
        if ans == "n" or ans == "N":
            return 0
        print("Please type y or n")

def find_student(name):
    for s in students:
        if s["name"].lower() == name.lower():
            return s
    return None

def add_student():
    name = input("Enter name: ")
    if name == "":
        print("Name cannot be empty")
        return
    if find_student(name) != None:
        print("This student is already added")
        return

    s = {}
    s["name"] = name
    s["sleep"] = ask_number("Sleeping hour (0-23, 11pm = 23): ", 0, 23)
    s["wake"] = ask_number("Waking hour (0-23): ", 0, 23)
    s["clean"] = ask_number("Cleanliness (1 messy to 5 very neat): ", 1, 5)
    s["noise"] = ask_number("Noise level (1 quiet to 5 loud): ", 1, 5)
    s["study"] = ask_number("Study seriousness (1 chill to 5 topper): ", 1, 5)
    s["guests"] = ask_number("Friends visiting (1 never to 5 always): ", 1, 5)
    s["smoker"] = ask_yes_no("Do you smoke?")
    s["veg"] = ask_yes_no("Are you vegetarian?")

    students.append(s)
    print(name, "added successfully")

def remove_student():
    name = input("Enter name to remove: ")
    s = find_student(name)
    if s == None:
        print("No student with that name")
    else:
        students.remove(s)
        print(s["name"], "removed")

def show_all():
    if len(students) == 0:
        print("No students added yet")
        return
    print()
    print("Name  Sleep  Wake  Clean  Noise  Study  Guests  Smoker  Veg")
    for s in students:
        print(s["name"], "  ", s["sleep"], "  ", s["wake"], "  ", s["clean"],
              "  ", s["noise"], "  ", s["study"], "  ", s["guests"],
              "  ", s["smoker"], "  ", s["veg"])

def hour_gap(a, b):
    # 23 and 1 are only 2 hours apart, not 22
    d = a - b
    if d < 0:
        d = -d
    if d > 12:
        d = 24 - d
    return d

def difference(a, b):
    # how far apart two numbers are (never negative)
    if a > b:
        return a - b
    return b - a

def compatibility(a, b):
    score = 100

    score = score - hour_gap(a["sleep"], b["sleep"]) * 4
    score = score - hour_gap(a["wake"], b["wake"]) * 3
    score = score - difference(a["clean"], b["clean"]) * 7
    score = score - difference(a["noise"], b["noise"]) * 5
    score = score - difference(a["study"], b["study"]) * 4
    score = score - difference(a["guests"], b["guests"]) * 3

    # smoking matters a lot, food habit matters less
    if a["smoker"] != b["smoker"]:
        score = score - 20
    if a["veg"] != b["veg"]:
        score = score - 5

    # a loud person with a serious studier is a problem
    if a["noise"] >= 4 and b["study"] >= 4:
        score = score - 10
    elif b["noise"] >= 4 and a["study"] >= 4:
        score = score - 10

    if score < 0:
        score = 0
    return score

def rating(p):
    if p >= 85:
        return "Excellent"
    elif p >= 70:
        return "Good"
    elif p >= 50:
        return "Average"
    else:
        return "Poor"

def compare_two():
    a = find_student(input("First student: "))
    b = find_student(input("Second student: "))
    if a == None or b == None:
        print("One of the students was not found")
    elif a == b:
        print("Please enter two different students")
    else:
        p = compatibility(a, b)
        print(a["name"], "and", b["name"], "->", p, "%", rating(p))

def best_matches():
    me = find_student(input("Find matches for: "))
    if me == None:
        print("Student not found")
        return

    results = []
    for s in students:
        if s != me:
            results.append((compatibility(me, s), s["name"]))
    results.sort(reverse=True)

    print("Best matches for", me["name"], ":")
    count = 0
    for r in results:
        print(r[1], "->", r[0], "%", rating(r[0]))
        count = count + 1
        if count == 3:
            break

def allot_rooms():
    rooms = []
    if len(students) < 2:
        print("Need at least 2 students")
        return rooms

    # make every possible pair with its score
    pairs = []
    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            p = compatibility(students[i], students[j])
            pairs.append((p, students[i]["name"], students[j]["name"]))

    pairs.sort(reverse=True)    # best pairs first

    taken = []
    for pair in pairs:
        n1 = pair[1]
        n2 = pair[2]
        if n1 in taken or n2 in taken:
            continue
        rooms.append(pair)
        taken.append(n1)
        taken.append(n2)

    for s in students:
        if s["name"] not in taken:
            print(s["name"], "has no partner, needs a single room")
    return rooms

def show_rooms(rooms):
    if len(rooms) == 0:
        print("No rooms allotted yet, choose option 6 first")
        return
    room_no = 101
    total = 0
    for r in rooms:
        print("Room", room_no, ":", r[1], "+", r[2], "->", r[0], "%")
        room_no = room_no + 1
        total = total + r[0]
    print("Average compatibility:", total / len(rooms), "%")

def load_sample():
    # a few students so we can test without typing everything
    names = ["Aman", "Ravi", "Karan", "Dev", "Sameer"]
    data = [[23, 6, 4, 2, 5, 2, 0, 1],
            [0, 8, 3, 4, 3, 4, 0, 0],
            [22, 6, 5, 1, 5, 1, 0, 1],
            [1, 9, 2, 5, 2, 5, 1, 0],
            [23, 7, 4, 2, 4, 2, 0, 1]]
    for i in range(len(names)):
        d = data[i]
        s = {"name": names[i], "sleep": d[0], "wake": d[1], "clean": d[2],
             "noise": d[3], "study": d[4], "guests": d[5],
             "smoker": d[6], "veg": d[7]}
        students.append(s)

def main():
    rooms = []
    load_sample()
    while True:
        print()
        print("===== HOSTEL ROOMMATE SYSTEM =====")
        print("1. Add student")
        print("2. Show all students")
        print("3. Compare two students")
        print("4. Best matches for a student")
        print("5. Remove student")
        print("6. Allot rooms")
        print("7. Show room list")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_all()
        elif choice == "3":
            compare_two()
        elif choice == "4":
            best_matches()
        elif choice == "5":
            remove_student()
        elif choice == "6":
            rooms = allot_rooms()
            show_rooms(rooms)
        elif choice == "7":
            show_rooms(rooms)
        elif choice == "0":
            print("Thank you!")
            break
        else:
            print("Invalid choice")

main()