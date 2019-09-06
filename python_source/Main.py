import Manu_ExcelData
import ManuPopluationData
import time

print("\n\nWelcome to Term Project")
check = False
list_year = [2014, 2015,2016, 2017]
while(check != True):
    print("\n")
    print("1.연도 별 병원 수 및 인구 수 자료 정리")
    print("2.서울시 연도별 병원 데이터 정보 출력")
    print("3.서울시 연도별 인구 데이터 정보 출력")
    print("4.병원 관련도 그래프 출력")
    print("5.인구 관련도 그래프 출력")
    print("6.프로그램 종료")
    print("\n\n")
    print("Input a Command (TYPE 은 정수): ", end="")

    
    command = input()
    
    try :
        command = int(command)
    except ValueError:
        print("변환 오류 발생 다시 실행합니다.")
        continue
        
    print("\n")
    if(command == 1):
        print("시작과 끝을 알리는 년도를 넣어 주세요.(년도 범위 2014~2017)")
        s_year = input("시작 년도: ")
        if(int(s_year) not in list_year):
            print("잘못 된 입력 값 입니다. 메인 메뉴로 돌아 갑니다.")
            continue
        e_year = input("끝 년도: ")
        if(int(e_year) not in list_year):
            print("잘못 된 입력 값 입니다. 메인 메뉴로 돌아 갑니다.")
            continue
       
        if(int(s_year) > int(e_year)):
            print("잘못 된 입력 값 입니다. 메인 메뉴로 돌아 갑니다.")
            continue
        start_time = time.time()
        
        for i in range(int(s_year), int(e_year)+1):
            Manu_ExcelData.fixexcel(i)
            print(str(i)+'년도 병원 수 정리 완료')
        for i in range(int(s_year), int(e_year)+1):
            ManuPopluationData.p_fixexcel(i)
            print(str(i)+'년도 인구 수 정리 완료')
        end_time = time.time()
        print("총정리 시간 :", "%0.2f" %(end_time - start_time), "초")
    elif(command == 2):
        y_check = False
        while (y_check != True):
            print("\n데이터 출력 메뉴 입니다.")
            print("정리된 연도 데이터만 입력 가능, 종료를 원한다면 0000을 입력해주세요.(연도 범위 2014~2017)")
            year2 = input("알고 싶은 년도를 입력 해주세요. : ")
            if(year2 == '0000'):
                y_check = True
                print("메인 메뉴로 돌아갑니다.")
                break
            elif(int(year2) not in list_year):
                print("범위를 벗어 났습니다.")
            else:
                Manu_ExcelData.show_data(year2)
    elif(command == 3):
        y_check = False
        while (y_check != True):
            print("\n데이터 출력 메뉴 입니다.")
            print("정리된 연도 데이터만 입력 가능, 종료를 원한다면 0000을 입력해주세요.(연도 범위 2014~2017)")
            year = input("알고 싶은 년도를 입력 해주세요. : ")
            if(year == '0000'):
                y_check = True
                print("메인 메뉴로 돌아갑니다.")
                break
            elif(int(year) not in list_year):
                print("범위를 벗어 났습니다.")
            else:
                ManuPopluationData.toatal_data(year)
    elif(command == 4):
        print("\n병원 수 그래프 출력 메뉴 입니다.")
        print("시작과 끝을 알리는 년도를 넣어 주세요.(연도 범위 2014~2017)")
        s_year = input("시작 년도: ")
        if(int(s_year) not in list_year):
            print("잘못 된 입력 값 입니다. 메인 메뉴로 돌아 갑니다.")
            continue
        e_year = input("끝 년도: ")
        if(int(e_year) not in list_year):
            print("잘못 된 입력 값 입니다. 메인 메뉴로 돌아 갑니다.")
            continue
        
        if(int(s_year) > int(e_year)):
            print("잘못 된 입력 값 입니다. 메인 메뉴로 돌아 갑니다.")
            continue

        list_year4 = []
        for i in range(int(s_year), int(e_year)+1):
            list_year4.append(i)
        print("현재 저장 되어 있는 데이터들을 공개 합니다.")
        print("그래프")
        Manu_ExcelData.show_graph(list_year4)
    elif(command == 5):
        print("\n인구 수 그래프 출력 메뉴 입니다.")
        print("시작과 끝을 알리는 년도를 넣어 주세요.(연도 범위 2014~2017)")
        s_year = input("시작 년도: ")
        if(int(s_year) not in list_year):
            print("잘못 된 입력 값 입니다. 메인 메뉴로 돌아 갑니다.")
            continue
        e_year = input("끝 년도: ")

        if(int(e_year) not in list_year):
            print("잘못 된 입력 값 입니다. 메인 메뉴로 돌아 갑니다.")
            continue
        
        if(int(s_year) > int(e_year)):
            print("잘못 된 입력 값 입니다. 메인 메뉴로 돌아 갑니다.")
            continue
        list_year5 = []
        for i in range(int(s_year), int(e_year)+1):
            list_year5.append(i)
        print("현재 저장 되어 있는 데이터들을 공개 합니다.")
        print("그래프")
        ManuPopluationData.show_graph(list_year5)
    elif(command == 6):
        print("프로그램을 종료합니다")
        check = True
    else:
        print("잘못된 명령어 입니다.")

