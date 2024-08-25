import os
import shutil
from collections import deque

# 파일 문자 및 인덱스 번호 자르기
def cut_file_string(first_str, end_str, progress_file):
    file_findex = progress_file.find(first_str)
    file_findex +=1
    file_eindex = progress_file.find(end_str)
    target_name = progress_file[file_findex:file_eindex]
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

    # 파일 리스트 구성
    origin_file_list = deque()
    target_dir_list = os.listdir(target_dir)

    # deque 요소 처리
    for file in os.listdir(origin_dir):
        origin_file_list.append(file)

    while origin_file_list:
        file = origin_file_list.popleft()
        print(file)
        target_name = cut_file_string(first_str, end_str, file)
        print(target_name)



if __name__ == "__main__":
    main()