guess = 0
answer = 7
while guess != answer:
    guess = int(input("정답을 입력하세요"))
    if guess > answer:
        print("더 작아요")
    elif guess < answer: 
        print("더 커요")

  

print("정답")

