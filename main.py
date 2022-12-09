def menu():
    print('*****CLASS RECORD******')
    print('[1] - ADD NEW STUDENT')
    print('[2] - SEARCH STUDENT')
    print('[3] - DELETE STUDENT')
    print('[4] - UPDATE  STUDENT')
    print('[5] - DISPLAY CLASS RECORD')
    print('[6] - EXIT')


def total_mark(total_pass_fail):
    if total_pass_fail >= 60:
        return True
    else:
        return False


def max_quiz(allowed_quiz_score):
    while allowed_quiz_score > 20:
        return True
    else:
        return False


def max_mid(allowed_mid_score):
    while allowed_mid_score > 40:
        return True
    else:
        return False


def max_final(allowed_final_score):
    while allowed_final_score > 40:
        return True
    else:
        return False


menu()
choice = int(input('Enter choice: '))

students = dict()  # to create an empty dictionaries
while choice != 6:
    if choice == 1:
        # Add new student
        print('♣♣♣♣♣♣ADD NEW STUDENT♣♣♣♣♣♣')
        name = input('Enter student name: ')
        details = dict()  # dictionary to store the information of the Student
        details['subject'] = input('Enter subject: ')
        details['quiz'] = float(input('Enter quiz mark: '))
        while max_quiz(details['quiz']):
            if max_quiz(details['quiz']):
                print('Error! Please try to enter quiz mark again. ☺')
                details['quiz'] = float(input('Enter quiz mark: '))
            else:
                continue
        details['mid'] = float(input('Enter mid mark: '))
        while max_mid(details['mid']):
            if max_mid(details['mid']):
                print('Error! Please try to enter mid mark again. ☺')
                details['mid'] = float(input('Enter mid mark: '))
            else:
                continue
        details['final'] = float(input('Enter final mark: '))
        while max_final(details['final']):
            if max_final(details['final']):
                print('Error! Please try to enter final mark again. ☺')
                details['final'] = float(input('Enter final mark: '))
            else:
                continue
        details['total'] = details['quiz'] + details['mid'] + details['final']
        if total_mark(details['total']):
            print("Passed↑")
        else:
            print('Failed↓')
        students[name] = details  # add new item to the dictionary
    elif choice == 2:
        # Search Student
        print('∞∞∞∞∞∞SEARCH STUDENT∞∞∞∞∞∞')
        student_name = input('Enter student name: ')
        if student_name in students:
            print('┼┼┼┼┼┼STUDENT DETAILS┼┼┼┼┼┼')
            print(f'Name: {student_name}')
            subject = students[student_name].get('subject')
            print(f'Subject: {subject} ')
            quiz = students[student_name].get('quiz')
            print(f'Quiz: {quiz} ')
            mid = students[student_name].get(('mid'))
            print(f'Mid: {mid} ')
            final = students[student_name].get(('final'))
            print(f'Final:{final}')
            total = students[student_name].get(('total'))
            print(f'Total Marks: {total} ')
        else:
            print('Please enter the right name of student again.☻')
            continue
    elif choice == 3:
        # Delete Student
        print('±±±±±±DELETE STUDENT±±±±±±')
        student_name = input('Enter student name: ')
        if student_name in students.keys():
            students.pop(student_name)
            print(f'{student_name} has been deleted! ☺☻')
        else:
            print('Please enter the right name of student again.☻')
            continue
    elif choice == 4:
        # Update Student
        print('♥♥♥♥♥♥UPDATE STUDENT♥♥♥♥♥♥')
        student_name = input('Enter student name: ')
        if student_name in students.keys():
            students[student_name]['subject'] = input('Enter subject: ')
            students[student_name]['quiz'] = float(input('Enter quiz mark: '))
            while students[student_name]['quiz'] > 20:
                print('Error! Please try to enter quiz mark again. ☺')
                students[student_name]['quiz'] = float(input('Enter quiz mark: '))
            students[student_name]['mid'] = float(input('Enter mid mark: '))
            while students[student_name]['mid'] > 40:
                print('Error! Please try to enter mid mark again. ☺')
                students[student_name]['mid'] = float(input('Enter mid mark: '))
            students[student_name]['final'] = float(input('Enter final mark: '))
            while students[student_name]['final'] > 40:
                print('Error! Please try to enter final mark again. ☺')
                students[student_name]['final'] = float(input('Enter final mark: '))
            students[student_name]['total'] = students[student_name]['quiz'] + students[student_name]['mid'] + students[student_name]['final']
            print(f'{student_name} has been updated! ☺☻')
        else:
            print('Please enter the right name of student again.☻')
            continue
    elif choice == 5:
        # Display Class Record
        print('☼☼☼☼☼☼DISPLAY CLASS RECORD☼☼☼☼☼☼')
        print('STUDENT NO. \tNAME \tSUBJECT \tQUIZ \tMID \tFINAL \tTOTAL')
        dictionary_lenght = len(students)
        count = 0
        while count < dictionary_lenght:
            count += 1
            disp_stud_name = list(students.keys())[count - 1]
            stud_detail = students.get('subject')
            list_stud_details = list(students.values())[count - 1]
            print(count, '\t', disp_stud_name, '\t', list_stud_details.get('subject'), '\t',
                  list_stud_details.get('quiz'), '\t', list_stud_details.get('mid'), '\t',
                  list_stud_details.get('final'), '\t', list_stud_details.get('total'))
    else:
        # Search Student
        print('╪╪╪╪╪╪INVALID OPTION╪╪╪╪╪╪')
    menu()  # function call
    choice = int(input('Enter choice: '))
print('♪♪♪♪♪♪Thank you. Bye.♪♪♪♪♪♪')