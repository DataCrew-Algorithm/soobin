# 단지번호붙이기
# 이것이 취업을 위한 코딩테스트다 '음료수 얼려먹기' 참고
# https://blog.naver.com/sooave/222300485598 참고


import sys
n = int(sys.stdin.readline())

# 2차원의 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))  # 문자열의 '맨앞'과 '맨뒤'의 whitespace(띄어쓰기, 탭, 엔터) 제거 해줌 (중간중간에 있는것들은 제거 안됨) 

# print(graph)  [[110100], [110101], [1110101], [111], [100000], [111110], [111000]]


count = 0
# dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    global count 

    # 주어진 범위를 벗어나는 경우 즉시 종료 ( 범위 : [0,0]~[n-1,n-1] )
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return  # False 안써도됨 = 종료
    
    # 현재 노드가 1이라면
    if graph[x][y] == 1:
        
        # 집이 존재하는것이므로 count 1 증가
        count += 1
        # 해당 노드를 재방문 하지 않기위해 0으로 바꿔줌
        graph[x][y] = 0

        # 상, 하, 좌, 우 모두 재귀적으로 호출
        dfs(x-1, y)  # 좌
        dfs(x, y-1)  # 하
        dfs(x+1, y)  # 우
        dfs(x, y+1)  # 상
        return True
    return     # 종료

# 모든 노드(위치)에 대하여 단지수 출력 & 단지 내 집의 수 오름차순 정렬
result = 0
danji = []
for a in range(n):
    for b in range(n):
        # 현재 위치에서 dfs 수행
        if dfs(a,b) == True:
            result += 1
            danji.append(count)
            count = 0

print(result)
danji.sort()
for c in danji:
    print(c)
