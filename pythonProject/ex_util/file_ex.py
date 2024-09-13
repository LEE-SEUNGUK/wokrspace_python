import os
root = 'C:\\'

# 파일 시스템의 디렉토리 트리를 반복적으로 순회
# 주어진 경로의 하위 디렉토리와 피일을 재귀적으로 탐색
# root: 현재 디렉토리 경로, dirs: 하위 디렉토리 목록
# files: 해당 디렉토리 내의 파일 목록
# for root, dirs, files in os.walk(root):
#     print(root, dirs, files)
# 시작 경로, 찾을 파일명을 입력받아
# 찾으면 찾았습니다. & 파일 전체 경로 출력

def search_photo(root, file_name):
    for root, dirs, files in os.walk(root):
        print(dirs)
        if file_name in files:
           print(root + '\\' + ''.join(dirs))
           msg = input("이 파일이 맞나요?(y/n)")
           if msg == 'y':
               break
           else:
               pass

question = input("찾을 파일의 경로와 파일명을 입력해!")
root = question.split()[0]
file_name = question.split()[1]

search_photo(root, file_name)