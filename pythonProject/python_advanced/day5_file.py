import os 
# os는 python 표준 라이브러리로 운영체제와 상호작용하는 다양한 기능제공
# 파일시스템 탐색 및 삭제, 변경, 생성...
print(os.getcwd()) # 현재 파일위치
dir = os.getcwd()
file_list = os.listdir(dir) # 현재 위치의 모든 파일리스트 
print(file_list)
del_file_path = os.path.join(dir, file_list[0]) # 경로 결합
print(del_file_path)
os.remove(del_file_path) # 파일삭제, rmdir:폴더삭제

