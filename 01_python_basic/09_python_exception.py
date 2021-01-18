## exception (예외)

# Error - compile time error : 문법 오류
#       - run time error : 실행 시 발생하는 오류

# 어떤 runtime error들은 비정상 종료되지 않고 프로그램을 지속적으로 수행시킬 수 있는 방법이 있다.

# exception 처리는 하나의 구문밖에 없다.

# try~
# except
# else
# finally

def my_func(my_list):

    total_sum = 0   # list 안의 숫자들을 누적한다.

    try:
        total_sum = my_list[0] + my_list[1] + my_list[2]
        print("try가 수행되었어요!!")

    except Exception:
        print("오류가 존재합니다.")     # 예외처리를 해야 한다!

    else:
        print("오류가 없어요!!")

    finally:
        print("무조건 수행되요!!")

my_func([1, 2, 3])
# try가 수행되었어요!!
# 오류가 없어요!!
# 무조건 수행되요!!

my_func([1, 2])
# 오류가 존재합니다.
# 무조건 수행되요!!