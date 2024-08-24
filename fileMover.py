import os
import shutil
from collections import deque

# 파일 문자 및 인덱스 번호 자르기
def cut_file(first_str, end_str, file_list):
    for file in file_list:
        file_findex = file.find(first_str)
        file_findex +=1
        file_eindex = file.find(end_str)
        target_name = file[file_findex:file_eindex]
        print(target_name)
    return target_name

# 파일 이동
def move_file(src, dst, origin_dir, target_dir, file, folder):
    shutil.move(src, dst)
    print(origin_dir + '\\' + file + "의 파일을 " + target_dir + folder + '\\' + "로 이동하였습니다.")


# 메인 함수 전개
def main():
    print("프로그램을 실행합니다.")

    print("처리할 폴더의 주소를 입력:")
    origin_dir = input()

    print("목적지 폴더의 주소를 입력:")
    target_dir = input()

    print("첫번째 문자를 입력:")
    first_str = input()

    print("마지막 문자를 입력:")
    end_str = input()

    # deque 선언
    origin_file_list = deque()
    target_dir_list = deque()

    # deque에 파일 리스트 담기
    for file in os.listdir(origin_dir):
        origin_file_list.append(file)   
    for file in os.listdir(target_dir):
        target_dir_list.append(file)
    
    cut_file(first_str, end_str, origin_file_list)


if __name__ == "__main__":
    main()