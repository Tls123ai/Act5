def check_grade(grades):
    if grades >= 90 and grades <= 100:
        return "Exellent! You did a great job!"
    elif grades >= 80 and grades <= 89:
        return "Good job! Keep it up!"
    elif grades >= 70 and grades <= 79:
        return "You passed, but there's room for improvements."
    elif grades < 70:
        return "You failed. Better luck next time"
    else:
        return "Invalid Grades"
        
user = int(input("Enter Grades: "))

print(check_grade(user))
