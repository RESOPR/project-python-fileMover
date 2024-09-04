import os
import shutil

# 파일 문자 및 인덱스 번호 자르기
def slice_file_string(first_str, end_str, progress_file):
    file_findex = progress_file.find(first_str)
    file_findex +=1
    file_eindex = progress_file.find(end_str)
    target_name = progress_file[file_findex:file_eindex].upper()
    return target_name

# 메인 함수 전개
def main():

    # GUI 부분 시작점 (추후)
    print("프로그램을 실행합니다.")

    print("처리할 폴더의 주소를 입력:")
    origin_dir = input()

    print("목적지 폴더의 주소를 입력:")
    target_dir = input()

    print("첫번째 문자를 입력:")
    first_str = input()

    print("마지막 문자를 입력:")
    end_str = input()

    # 파일 리스트 불러오기
    try:
        file_list = os.listdir(origin_dir)
        dst_folder_list = os.listdir(target_dir)
    except FileNotFoundError as error:
        print(f"폴더를 찾지 못했어요. : {error}")
        exit()

    # 파일 리스트 구성
    dst_file_list = {folder.upper(): folder for folder in dst_folder_list}

    for file in file_list:
        target_name = slice_file_string(first_str, end_str, file)
        
        if target_name in dst_file_list:
            dst_name = dst_file_list[target_name]
            print(dst_name + "폴더 발견")
            src = os.path.join(origin_dir, file)
            dst = os.path.join(target_dir, dst_name)
            print("소스 파일 " + src + " 도착 폴더 " + dst)

            try:
                shutil.move(src, dst)
                print(f'{src}에서 {dst}로 이동하였습니다.')
            except shutil.Error as error:
                print(f"파일이 중복되었어요. : {error}")
                continue

# 메인 함수 선언부
if __name__ == "__main__":
    main()