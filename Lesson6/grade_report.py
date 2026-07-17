while True:
    students = [
        {'name': 'Joha', 'maths':40, 'english':20, 'science':10},
        {'name': 'Male', 'maths':60, 'english':90, 'science':70},
        {'name': 'Mak', 'maths':40, 'english':25, 'science':5},
        {'name': 'Jy', 'maths':70, 'english':50, 'science':10},
        {'name': 'MJ', 'maths':100, 'english':70, 'science':70},
        
    ]
    def grading(i):
        maths,english,science =[],[],[]
        avg_grade = round(sum([i['maths'],i['english'],i['science']])/3,2)
        maths.append(i['maths'])
        english.append(i['english'])
        science.append(i['science'])
        if avg_grade >= 80:
            assign_letter = "A"
        elif avg_grade >=70 and avg_grade <=79:
            assign_letter = "B"
        elif avg_grade >=60 and avg_grade <=69:
            assign_letter = "C"
        elif avg_grade >=50 and avg_grade <=59:
            assign_letter = "D"
        elif avg_grade < 50:
            assign_letter = "F"

        if avg_grade > 49:
                status = 'Pass' 
        else:
                status = 'Fail'
        
        return avg_grade,assign_letter, status, maths,english,science


    def overall():
        avg_marks = []
        maths,english,science =[],[],[]

        for i in students:
            avg_grade,assign_letter, status,math_i,english_i,science_i=grading(i)
            avg_marks.append(avg_grade)
            maths.append(math_i)
            english.append(english_i)
            science.append(science_i)

        class_average = round(sum(avg_marks)/len(avg_marks),2)
        print(f'''
    CLASS STATISTICS:\n
    class average: {class_average}
    highest mark: 
    maths  : {max(maths)}
    english: {max(english)}
    science: {max(science)}
    lowest mark:
    maths  : {min(maths)}
    english: {min(english)}
    science: {min(science)}
    ''')

    def formatted_display(students):

        for i in students:
            avg_grade,assign_letter, status,maths,english,science =grading(i)
            print(f"""
    Student report card: 
    Name: {i['name']}
    Average: {avg_grade}
    Grade: {assign_letter}
    Status: {status}\n""")
        if len(students) > 1:
            overall()
        else:
            pass

    formatted_display(students)     

    search = None
    while search is None:
         
        try:
            search = input('search for Student: `yes or no`y: ')
            if search.lower() not in ['yes','no','y','n']:
                raise ValueError
        except ValueError:
             print("Enter: `yes or no`")
        else:
            if search.lower() in ['yes','y']:

                st_name = input("Search Student:")
                for i in students:
                    if i['name'] == st_name:
                        i = [i,]
                        print('\n~~ SEARCHED STUDENT: ~~')
                        formatted_display(i)
            else:
                break


    again = None
    while again is None:
         
        try:
            again = input('show report again: `yes or no`y: ')
            if again.lower() not in ['yes','no','y','n']:
                raise ValueError
        except ValueError:
             print("Enter: `yes or no`")        
    
    if again.lower() in ['yes','y']:
         continue
    else:
        break
              

