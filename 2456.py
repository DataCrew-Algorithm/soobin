# 학급회장 (실패)

student_score = [list(input()) for _ in range(7)]
# [['6'], ['3', ' ', '1', ' ', '2'], ['2', ' ', '3', ' ', '1'], ['3', ' ', '1', ' ', '2'], ['1', ' ', '2', ' ', '3'], ['3', ' ', '1', ' ', '2'], ['1', ' ', '2', ' ', '3']]

# 반의 학생들의 수 N명은 제외하고자 student_score를 슬라이싱해줌
student_score = student_score[1:]
# [['3', ' ', '1', ' ', '2'], ['2', ' ', '3', ' ', '1'], ['3', ' ', '1', ' ', '2'], ['1', ' ', '2', ' ', '3'], ['3', ' ', '1', ' ', '2'], ['1', ' ', '2', ' ', '3']]

# 1번후보의 점수만 score1에 저장 (str로 저장됨) (이하동문)
score1 = student_score[0][0] + student_score[1][0] + student_score[2][0] + student_score[3][0] + student_score[4][0] + student_score[5][0]
score2 = student_score[0][2] + student_score[1][2] + student_score[2][2] + student_score[3][2] + student_score[4][2] + student_score[5][2]
score3 = student_score[0][4] + student_score[1][4] + student_score[2][4] + student_score[3][4] + student_score[4][4] + student_score[5][4]

# 각 점수의 합을 구하기 위해 int로 바꿔줌
score_i1 = list(map(int, score1))
score_i2 = list(map(int, score2))
score_i3 = list(map(int, score3))

# 세 후보의 점수의 합
sum1 = sum(score_i1)
sum2 = sum(score_i2)
sum3 = sum(score_i3)

# 점수 최대 
# if max(sum1, sum2, sum3) == sum1:
#     print(1, sum1)
# elif max(sum1, sum2, sum3) == sum2:
#     print(2, sum2)
# elif max(sum1, sum2, sum3) == sum3:
#     print(3, sum3)

# 갯수 최대
if list(score1).count('3') > list(score2).count('3') or list(score1).count('3') > list(score3).count('3'):
    print(1, sum1)
elif list(score2).count('3') > list(score1).count('3') or list(score2).count('3') > list(score3).count('3'):
    print(2, sum2)
elif list(score3).count('3') > list(score1).count('3') or list(score3).count('3') > list(score2).count('3'):
    print(3, sum3)

elif (list(score1).count('3') == list(score2).count('3') and list(score1).count('2') > list(score2).count('2')) or (list(score1).count('3') == list(score3).count('3') and list(score1).count('2') > list(score3).count('2')):
    print(1, sum1)
elif (list(score2).count('3') == list(score1).count('3') and list(score2).count('2') > list(score1).count('2') ) or (list(score2).count('3') == list(score3).count('3') and list(score2).count('2') > list(score3).count('2')):
    print(2, sum2)
elif (list(score3).count('3') == list(score1).count('3') and list(score3).count('2') > list(score1).count('2') ) or (list(score3).count('3') == list(score2).count('3') and list(score3).count('2') > list(score2).count('2')):
    print(3, sum3)

elif list(score1).count('3') == list(score2).count('3') == list(score3).count('3') and list(score1).count('2') == list(score2).count('2') == list(score3).count('2'):
    print(0, max(sum1, sum2, sum3))


