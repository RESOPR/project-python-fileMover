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

    file_list = deque()

    for file in os.listdir(origin_dir):
        file_list.append(file)
    
if __name__ == "__main__":
    main()