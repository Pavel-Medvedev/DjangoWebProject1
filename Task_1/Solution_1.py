def print_students(Group):
    if Group == []:
        print("There is no student in sorted group")
        return
    print(u"Name".ljust(15), u"Surmane".ljust(10), u"Exams".ljust(50), u"Marks".ljust(20))
    for Student in Group:
        print(Student["Name"].ljust(15), Student["Surname"].ljust(10), str(Student["Exams"]).ljust(50), str(Student["Marks"]).ljust(20))

def sorting_students_by_average_grade(Group, Grade):
    Sorted_Groupmates = []
    for Student in Group:
        if Grade <= sum(Student["Marks"])/len(Student["Marks"]):
            Sorted_Groupmates.append(Student)
    return Sorted_Groupmates;

Groupmates = [
    {
        "Name": "Pavel",
        "Surname": "Medvedev",
        "Exams": ["Informatics", "Philosophy", "Mathematics"],
        "Marks": [4, 4, 4]
    },
    {
        "Name": "Pavel",
        "Surname": "Medvedev",
        "Exams": ["Informatics", "Philosophy", "Mathematics"],
        "Marks": [3, 3, 3]
    },
    {
        "Name": "Pavel",
        "Surname": "Medvedev",
        "Exams": ["Informatics", "Philosophy", "Mathematics"],
        "Marks": [5, 5, 5]
    },
    {
        "Name": "Pavel",
        "Surname": "Medvedev",
        "Exams": ["Informatics", "Philosophy", "Mathematics"],
        "Marks": [4, 4, 3]
    },
    {
        "Name": "Pavel",
        "Surname": "Medvedev",
        "Exams": ["Informatics", "Philosophy", "Mathematics"],
        "Marks": [5, 3, 3]
    },
    ]

print_students(sorting_students_by_average_grade(Groupmates, float(input("Input the average grade for sorting groupmates: "))));