grades = {
    "A": 80,
    "B": 70,
    "C": 60,
    "D": 50,
    "E": 40,
}

def mark_grade(percentage):
    
    for grade, percent in grades.items():
        if percentage >= percent:
            return grade

def calculate_target_grade(egrade, tgrade):

    eper = grades.get(egrade)
    tper = grades.get(tgrade)

    if tper > eper:
       return "You need to work hard."
    elif tper == eper:
       return "You  achived same score."
    elif tper < eper:
       return "You achived it."
    else:
      return "Sorry"

percentage = input("Enter your percentage: ")
tgrade = input("Enter your target grade: ")

egread = mark_grade(int(percentage))
if egread == None:
    print("Invalid grade")
else:
    print("Your grade is: ", egread)
    result = calculate_target_grade(egread, tgrade)
    print(result)
