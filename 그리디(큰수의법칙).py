"""조건)서로 다른 인덱스에 해당하는 같은 숫자는 서로 다른 숫자로 인식한다.
     배열에서 주언진 수들을 m번 더하여, 가장 큰 수를 만드는 알고리즘이고, 같은 
     인덱스(번호) 숫자를 K번 초과해서 더할 수 없다.
     break와 continue의 차이점: 반복문에서, break는 해당 반복문을 벗어나지만, continue는
     제어(반복)흐름을 유지한 상태에서 해당 코드의 실행만 건너뛰는 역할!"""
#n,m,k 공백으로 구분하여 받기
n,m,k = map(int,input().split())

#n개의 배열의 수들을 공백으로 구분하여 입력 받기
data=list(map(int,input().split()))

#가장 큰 수와 작은 수를 나눠서 받기, sort 쓰면 리스트 형태 변환됨!
#기본이 reverse=false 이다
data1=data.copy() #배열의 인수 갯수:n,더하는 횟수:k,가장 큰 수:m
data1.sort() #기본적으로 리스트 오름차순 정렬, 제일 큰 값이 제일 나중에 나옴! 인덱스(=순서)로는 n개일 경우, n-1이 가장 큰 수!
first=data[n-1] #가장 큰 수 
second=data[n-2] #두번째로 큰 수

result=0

while True: 
    for i in range(k) #가장 큰 수를 k번 더해주기
    if m==0:
        break
    result+=first
    m-=1 #더할떄마다 m은 1씩 감소
    if m == 0: #m이 0이라면 반복문 탈출
        break
    result+=second #두번째로 큰 수를 더해주기
    m-=1

print(result)

