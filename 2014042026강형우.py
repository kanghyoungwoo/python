import operator
student = {}

while 1:
    select = input('\n1. 데이터 추가\n2. 데이터 검색\n3. 데이터 삭제\n4. 데이터 정렬\n0. 종료\n 메뉴를 선택하세요:')
    if select == "1":
        print("\n데이터 추가\n 추가할 학생의 학과, 학번, 이름, 국어점수, 영어점수, 수학점수를 입력하세요\n")
        depart = input("학과: ")
        id = input("학번: ")
        name = input("이름: ")
        kor = int(input("국어점수: "))
        eng = int(input("영어점수: "))
        math = int(input("수학점수: "))
        sum = kor + eng + math #총점
        avg = int(sum/3) #평균
        if avg >= 95:
            grade = 'A+'
        elif avg >= 90:
            grade = 'A0'
        elif avg >= 85:
            grade = 'B+'
        elif avg >= 80:
            grade = 'B0'
        elif avg >= 75:
            grade = 'C+'
        elif avg >= 70:
            grade = 'C0'
        elif avg >= 65:
            grade = 'D+'
        else:
            grade = 'F'

        #학점 grade평균이 95점 이상이면 'A+'
              #90점 이상이면 'A0'
              #85점 이상이면 'B+'
              #80점 이상이면 'B0'
              #65점 미만이면 'F'

        student[id] = [depart,id,name,kor,eng,math,sum,avg,grade] #총점 평균 학점?
        continue
    elif select == "2":
        search = input("\n 검색하고싶은 사람의 학번 또는 이름을 입력하세요:")
        for value in student.values():
            if (value[2] == search) or (value[1] == search):
                print(value)
        continue
    elif select == "3":
        print("데이터삭제\n")
        delname = input("삭제할 학생의 이름을 입력하세요:")
        for key,value in student.items(): #student.items()
            if(value[2] == delname):
                del student[key]
                print("삭제결과:", value[2],"학생의 정보", value, "가 삭제 되었습니다.")
                break
        continue
    elif select == "4":
        print("학번별 데이터정렬")
        for i in sorted(student.keys()):
            print(student[i])
        continue
    elif select == "0":
        break