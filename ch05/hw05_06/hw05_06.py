# hw05_06
students = [student for student in range(1, 11)]

while students:
    print('未簽到座號:', end=' ')
    for student in students:
        print(student, end=' ')
    checkin = int(input('\n請輸入座號(1~10): '))
    students.remove(checkin)

print('未簽到座號: 沒有，全員到齊!')