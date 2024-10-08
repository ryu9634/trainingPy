# for 문
'''
for 변수 in 열거행 :
    실행코드

특정범위만큼 코드를 반복 실행하는 조건문
열거형 데이터를 하나씩 변수 값 에 대입하며 실행
'''
# range() 함수
'''
range() 함수
- 숫자의 범위와 증감 값을 정하면 규칙적인 수들의 집합으로 만들어주는 함수

range(a) -> 0 ~ a-1

range(a,b) -> a ~ b-1

range(a,b,c) -> a ~ b-1, c 씩증가
* a,b,c 는 모두 정수(int) 값만 사용가능
'''
'''
#range(11)
- 0부터 10(11-1)까지 1씩 증가 
- 결과값 : 0,1,2,3...9,10

#range(1,11)
- 1부터 10(11-1)까지 1씩 증가
- 결과값 : 1,2,3...9,10

#range(1,11,2)
- 1부터 10(11-1)까지 2씩 증가 
- 결과값 : 1,3,5,7,9
'''
range(5)

list(range(5))

print(list(range(5)))
# for문 활용