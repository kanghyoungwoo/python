import operator
#student = {}
student_list = []
## 클래스 선언부분 ##

class Student:

    def __init__(self,dep,id,name,kor,eng,math,sum,avg,grade):
        self.dep = dep
        self.id = id
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.sum = sum
        self.avg = avg
        self.grade = grade

    # 학생 정보를 보여줌 #

    def showStudent(self):
        print("이름: ",self.name)
        print("학과: ",self.dep)
        print("학번: ",self.id)
        print("국어: ",self.kor)
        print("영어: ",self.eng)
        print("수학: ",self.math)
        print("총점: ",self.sum)
        print("평균: ",self.avg)
        print("학점: ",self.grade)
        print("#############################")

## 함수 선언 부분 ##

def showMenu():
    print("#### 메뉴를 선택하세요 ####")
    print("1. 데이터 추가")
    print("2. 데이터 검색")
    print("3. 데이터 삭제")
    print("4. 데이터 정렬")
    print("0. 종료")
    select = input("메뉴를 선택하세요: ")
    return select

# 학생들의 정보 입력함수 #
def input_student():
    print("\n데이터 추가\n 추가할 학생의 학과, 학번, 이름, 국어점수, 영어점수, 수학점수를 입력하세요\n")
    depart = input("학과: ")
    id = input("학번: ")
    name = input("이름: ")
    kor = int(input("국어점수: "))
    eng = int(input("영어점수: "))
    math = int(input("수학점수: "))
    sum = kor + eng + math  # 총점
    avg = int(sum / 3)  # 평균
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

    # 학점 grade평균이 95점 이상이면 'A+'
    # 90점 이상이면 'A0'
    # 85점 이상이면 'B+'
    # 80점 이상이면 'B0'
    # 65점 미만이면 'F'

    ## student[id] = [depart, id, name, kor, eng, math, sum, avg, grade]  # 총점 평균 학점?
    ## 인스턴스 만들기 ##
    student = Student(depart, id, name, kor, eng, math, sum, avg, grade)
    #객체 리스트에 담기
    student_list.append(student)
    return student_list
# 학생들의 전체 정보를 보여주는 함수 #
# sort #
def showAll(student_list):
    for student in student_list:
        student.showStudent()

# 학생 검색 함수 #
def search_student():
    name = input("검색할 학생의 이름을 입력하세요: ")
    for student in student_list:
        if student.name == name:
            student.showStudent()
        else:
            print("존재하지 않는 학생입니다.")

# 학생 삭제 함수 #
def delete_student():
    print("데이터삭제\n")
    delname = input("삭제할 학생의 이름을 입력하세요:")
    for i, student in enumerate(student_list):
        if student.name == delname:
            del student_list[i]

# 학생 정렬 함수
def sort_student():
    print("학번별 데이터정렬")
    sorted_list = sorted(student_list, key = lambda student: student.id)
    for student in student_list:
        showAll(sorted_list)

def exit_program():
    print('프로그램을 종료합니다')


## 메인 코드 부분 ##

## 클래스를 이용해 메인코드에서 인스턴스 만들기 ##

while 1:
    menuSelect = showMenu()
    if menuSelect == "1":
        input_student()

    elif menuSelect == "2":
        search_student()

    elif menuSelect == "3":
        delete_student()

    elif menuSelect == "4":
        sort_student()

    elif menuSelect == "0":
        exit_program()
        break