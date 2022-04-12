# 첫 글자를 대문자로

# 생각 1)
# num = int(input())              
 
# result = []                   

# for _ in range(num):             
#     result.append(input())
     
# ['powdered Toast Man', 'skeletor', 'Electra Woman and Dyna Girl', 'she-Ra Princess of Power', 'darth Vader']
#  result[i][0].upper() 첫번째 글자만 대문자로 바꿀 수 있도록 for문을 돌려보자 생각했지만 코드 구현 못함

# for i in range(num):
#     result[i][0].upper()  # 여기 for문 적용x 

# print(*result, sep="\n")  # 입력값 그대로 출력되어 나옴


# 생각 2)
# capitalize() 사용하려고 함 : 첫글자는 대문자로 나머지는 소문자로 바꿔주는 함수
# 문제 다시 읽어보니 첫글자만 대문자로 바뀌고 나머지 뒷 문자들은 바뀌면 안된다는 것을 알았음


# 생각 3) 
# 첫 글자만 대문자로 바꾸고 + 뒤에는 그대로 이어서 붙여주자 라고 생각
# num = int(input())              

# result = []                   

# for i in range(num):             
#     result.append(input())
#     print(result[i][0].upper()+result[1:])

# TypeError: can only concatenate str (not "list") to str
# -> 리스트에서 사용불가 -> 리스트로 만들지 말자 -> 빈리스트 생성 X

# 생각 4) 
num = int(input())

for i in range(num):             
    result = input()
    print(result[0].upper()+result[1:])

# 30840KB / 68ms / 113B