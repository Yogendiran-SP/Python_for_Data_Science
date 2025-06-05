def marks_insert(n,s):
    marks=[]
    for i in range(1,n+1):
        print("\nEnter the Student",i,"Marks")
        stu1=list(map(int, input("Enter the Marks: ").split()))
        marks.append(stu1)
    return marks

def display_one_student_marks(mark_list,i):
    return mark_list[i-1]

def display_total_marks(mark_list,i):
    return sum(mark_list[i-1])

def display_percentage(mark_list,i):
    s=0
    for j in mark_list[i-1]:
        s+=j
    avg=s/len(mark_list[i-1])
    return avg

def display_high_low(mark_list,i):
    return max(mark_list[i-1]),min(mark_list[i-1])

if __name__=="__main__":
    marks=[]
    while True:
        print("_____________________\nSTUDENT MARKS STORAGE\n_____________________\n")
        print("1. Insert Student's Marks\n2. Retrieve Students Marks\n")
        choice=int(input("Enter your choice (1 or 2): "))

        if choice == 1:
            n = int(input("Enter the no. of Students marks to be inserted: "))
            s = int(input("Enter the no. of Subjects: "))
            res=marks_insert(n,s)
            marks.clear()
            for i in range(0,n):
                marks.append(res[i])

        if choice == 2:
            print("1. Retrieve all the students marks\n2. Retrieve a Student's Marks\n3. Retrieve a Subject Marks\n")
            choice1 = int(input("Enter your choice (1 or 2): "))

            if choice1 == 1:
                print(*marks)

            elif choice1 == 2:
                print("1. Display one student's marks\n2. Display one student's total marks\n3. Display one student's total percentage\n4. Display one student's Highest & Lowest marks\n")
                choice2 = int(input("Enter your choice (1 or 2 or 3 or 4): "))

                if choice2 == 1:
                    student_no = int(input("Which student's marks you want to display (1 or 2 or x): "))
                    print("")
                    print(display_one_student_marks(marks,student_no))
                
                elif choice2 == 2:
                    student_no = int(input("Which student's marks you want to display (1 or 2 or x): "))
                    print("")
                    print(display_total_marks(marks,i))

                elif choice2 == 3:
                    student_no = int(input("Which student's marks you want to display (1 or 2 or x): "))
                    print("")
                    print(display_percentage(marks,i))

                elif choice2 == 4:
                    student_no = int(input("Which student's marks you want to display (1 or 2 or x): "))
                    print("")
                    high,low=display_high_low(marks,i)
                    print(f"Highest  Mark: {high}\nLowest Mark: {low}")