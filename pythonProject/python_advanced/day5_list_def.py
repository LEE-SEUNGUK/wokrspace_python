# 학생 성적
scores = [85, 90, 65, 100, 76]
# 학생 수 ?
num_stu = len(scores) 
print(f"학생수는:{num_stu}")
# 가장 높은 점수는?
max_score = max(scores) # 가장높은
print(f"가장 높은 점수:{max_score}")
# 가장 낮은 점수는? 
min_score = min(scores)
print(f"가장 낮은 점수:{min_score}")
# 전체 평균은? 
avg_score = sum(scores) / num_stu  
print(f'평균 :{avg_score}')
# 정렬 (리스트를 정렬한 새 리스트를 반환)
sorted_socre = sorted(scores)
print(f"scores:{scores}")
print(f"sorted:{sorted_socre}")