N=10000
cnt=1

for i in range(N):
    print("연산 횟수"+str(cnt))
    cnt+=1

   #n과3n은 같은 시간복잡도이다. (상수는 치지 않는다, 너무 극단적)
    
    n=10000
    cnt =1

    for i in range(N):
        for j in range(N):
            print("연산 횟수"+str(cnt))
            cnt+=1
            #d이식은 j가 하나 더 들어가 있으므로 시간 복잡도가 n의 제곱!
            

     