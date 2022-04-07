# Task - Use if statement, if else statement, if elif statement and nested if statement
# with user input to show the result (Marking with position) of the student
student_name = input("Enter your name: ")

physics = int(input("enter marks obtain in physics: "))
biology = int(input("enter marks obtain in biology: "))
chemistry = int(input("enter marks obtain in chemistry: "))
math = int(input("enter marks obtain in math: "))
english = int(input("enter marks obtain in english: "))
total_marks = 500

if physics >=0 and physics <=100:
    if physics >= 40:
            
            if physics <= 50:
               print("COngratulation you have got: ","c","in physics")
            elif physics <= 60:
                print("COngratulation you have got: ","c+","in physics")
            elif physics <= 70:
                print("COngratulation you have got: ","b","in physics")
            elif physics <= 80:
                print("COngratulation you have got: ","b+","in physics")
            elif physics <= 90:
                print("COngratulation you have got: ","a","in physics")
            elif physics <= 100:
                print("COngratulation you have got: ","A+","in physics")
    else:
        print("you are fail in physics")
else:
    print("enter valid number")


if biology >=0 and biology <=100:
    if biology >= 40:
            
            if biology <= 50:
               print("COngratulation you have got: ","c","in biology")
            elif biology <= 60:
                print("COngratulation you have got: ","c+","in biology")
            elif biology <= 70:
                print("COngratulation you have got: ","b","in biology")
            elif biology <= 80:
                print("COngratulation you have got: ","b+","in biology")
            elif biology <= 90:
                print("COngratulation you have got: ","a","in biology")
            elif biology <= 100:
                print("COngratulation you have got: ","A+","in biology")
    else:
        print("you are fail in biology")
else:
    print("enter valid number")


if chemistry >=0 and chemistry <=100:
    if chemistry >= 40:
            
            if chemistry <= 50:
               print("COngratulation you have got: ","c","in chemistry")
            elif chemistry <= 60:
                print("COngratulation you have got: ","c+","in chemistry")
            elif chemistry <= 70:
                print("COngratulation you have got: ","b","in chemistry")
            elif chemistry <= 80:
                print("COngratulation you have got: ","b+","in chemistry")
            elif chemistry <= 90:
                print("COngratulation you have got: ","a","in chemistry")
            elif chemistry <= 100:
                print("COngratulation you have got: ","A+","in chemistry")
    else:
        print("you are fail in chemistry")
else:
    print("enter valid number")

if math >=0 and math <=100:
    if math >= 40:
            
            if math <= 50:
               print("COngratulation you have got: ","c","in math")
            elif math <= 60:
                print("COngratulation you have got: ","c+","in math")
            elif math <= 70:
                print("COngratulation you have got: ","b","in math")
            elif math <= 80:
                print("COngratulation you have got: ","b+","in math")
            elif math <= 90:
                print("COngratulation you have got: ","a","in math")
            elif math <= 100:
                print("COngratulation you have got: ","A+","in math")
    else:
        print("you are fail in math")
else:
    print("enter valid number")

if english >=0 and english <=100:
    if english >= 40:
            
            if english <= 50:
               print("COngratulation you have got: ","c","in english")
            elif english <= 60:
                print("COngratulation you have got: ","c+","in english")
            elif english <= 70:
                print("COngratulation you have got: ","b","in english")
            elif english <= 80:
                print("COngratulation you have got: ","b+","in english")
            elif english <= 90:
                print("COngratulation you have got: ","a","in english")
            elif math <= 100:
                print("COngratulation you have got: ","A+","in english")
    else:
        print("you are fail in english")
else:
    print("enter valid number")

total_studentNum = physics + biology + chemistry + math + english
student_percent = total_studentNum/5
print(student_name, " you got: ", student_percent ,"percent in total")
if student_percent >= 0:
    if student_percent<=100:
        if student_percent >= 40.0:
            print("pass")
            if student_percent <= 50.0:
               print(student_name,"COngratulation you have got: ","c")
            elif student_percent <= 60.0:
                print(student_name,"COngratulation you have got: ","c+")
            elif student_percent <= 70.0:
                print(student_name,"COngratulation you have got: ","b")
            elif student_percent <= 80.0:
                print(student_name,"COngratulation you have got: ","b+")
            elif student_percent <= 90.0:
                print(student_name,"COngratulation you have got: ","a")
            elif student_percent <= 100.0:
                print(student_name,"COngratulation you have got: ","A+")
        else:
          print("fail",student_name, "Better luck next time")
    else:
        print("please enter valid input")
else:
    print("please enter valiid input")
