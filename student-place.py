
student1 = int(input("Student 1: "))
student2 = int(input("Student 2: "))
student3 = int(input("Student 3: "))

if student1 > student2 and student1 > student3:
    print("Student 1")
    if student2 > student3:
        print("Student 2")
        print("Student 3")
    else:
        print("Student 3")
        print("Student 1")
elif student2 > student1 and student2 > student3:
    print("Student 2")
    if student1 > student3:
        print("Student 1")
        print("Student 3")
    else:
        print("Student 3")
        print("Student 1")
elif student3 > student1 and student3 > student2:
    print("Student 3")
    if student1 > student2:
        print("Student 1")
        print("Student 2")
    else:
        print("Student 2")
        print("Student 1")