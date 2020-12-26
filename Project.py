names = ["Serdar","Elif","Fatma","Sevda"]
surnames = ["Babacan","Gültekin","Yılmaz","Taşdemir"]
courses = ["Müzik","Matematik","Kimya","Bilgisayar","Fizik"]

for i in range(3):
    name = input('İsim giriniz:')
    surname = input('Soyad giriniz:')

    for j in range (4):
        if (name == names[j] and surname == surnames[j]):
            f=1
            break


        else:
            f=0

    if (f==1):
        print("Welcome "+ name + " " + surname)
        course = int(input('Enter the number of courses you took:'))
        if course<3:
            print('You failed in class.')
        elif course>5:
            print('You can take max 5 courses!')
        else:
            for b in range(course):
                print(courses)
                lesson = input('Please choose an course:')
                if lesson in courses:
                    midterm = int(input('Enter your midterm score:'))
                    final = int(input('Enter your final score:'))
                    project = int(input('Enter your project score:'))
                    grades = {"Midterm": midterm, "Final": final, "Project": project}
                    print(grades)
                    x = midterm * 30 / 100 + final * 50 / 100 + project * 20 / 100
                    print('Grade:', x)
                    if x > 90:
                        print('AA\nYou passed.')
                    elif x <= 90 and x > 70:
                        print('BB\nYou passed.')
                    elif x <= 70 and x > 50:
                        print('CC\nYou passed.')
                    elif x <= 50 and x >= 30:
                        print('DD\nYou passed.')
                    else:
                        print('FF\nYou failed.')
                    if (b==(course-1)):
                        print('\nIf you have FF, you failed.\nIf you did not get FF, congratulaions you passed!')

                else:
                    print('There is no such course!\nPlease try again.')
                    break


        break
    else:
        if(i==2):
            print("")
        else:
            print("You have {} attempts left!".format(3-(i+1)))

if (f==0):
    print ("Please try again later.")