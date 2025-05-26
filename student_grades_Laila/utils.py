# utils.py

def calculate_average(scores):
    return sum(scores) / len(scores)

def assign_grade(average):
    if average >= 85:
        return 'A'
    elif average >= 75:
        return 'B'
    elif average >= 65:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'
