import os
import shutil

print("처리할 폴더의 주소를 입력:")
origin_dir = input()

print("목적지 폴더의 주소를 입력:")
target_dir = input()

print("첫번째 문자를 입력:")
first_str = input()

print("마지막 문자를 입력:")
end_str = input()

# 폴더내 파일 리스트 가져오기
file_list = os.listdir(origin_dir)
file_list_target = os.listdir(target_dir)

for file in file_list:
    # 파일 문자 및 인덱스 번호 자르기
    file_findex = file.find(first_str)
    file_findex +=1
    file_eindex = file.find(end_str)
    target_name = file[file_findex:file_eindex]

    # 파일 이동
    for folder in file_list_target:
        if folder.upper() == target_name.upper():
            print(folder + " 폴더 발견")
            src = os.path.join(origin_dir, file)
            dst = os.path.join(target_dir, folder)
            print("소스 파일 " + src + "도착 폴더 " + dst)

            # 중복 파일 발견 처리
            dst_files = os.listdir(dst)
            for df in dst_files:
                if df.upper() == file.upper():
                    print("중복파일 존재확인 및 삭제")
                    del_file = os.path.join(dst, df)
                    print("삭제될 파일은" + del_file + "입니다.")
                    os.remove(del_file)
            # 파일 이동 재게
            shutil.move(src, dst)
            print(origin_dir + '\\' + file + "의 파일을 " + target_dir + folder + '\\' + "로 이동하였습니다.")
            break
