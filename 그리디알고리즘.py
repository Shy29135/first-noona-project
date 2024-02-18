n=1260
count=0

# 큰 단위의 화폐로부터 차례대로 확인하기
array=[500,100,50,10]

for coin in array:
    count+=n//coin #n을 array 배열 인수로 나눈 목을 정수형태로 출력!
    n%=coin #반복문으로 500부터 시작해 array안에 있는 coin값의 순서대로 대입하여, n값이 coin값보다 작아야 함!

    print(count)