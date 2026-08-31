# TIL
# 1. git init: Turns the current folder into a Git repository. It creates a hidden .git folder that lets Git start tracking changes to your files -- like turning on "save history" for your project.
Git은 코드의 변경 기록을 계속 저장해주는 도구,(게임의 저장포인트) git init 를 실행하면 그 폴더 안에 .git이라는 숨겨진 폴더가 생김, 그 순간부터 Git이 폴더 안에 파일 변화를 지켜볼게 하고 준비하는것.

# 2. add . :Stages all changed files in the current folder, getting them ready to commit.
현재 폴더의 변경된 파일들을 커밋할 준비상태(스테이징)로 올린다

# 3. git commit -m "메시지" Saves the staged changes to the repository's history with a message describing what was done.

스테이징된 변경사항을 메시지와 함께 저장소 기록에 저장한다.

# 4. Variable(변수) : A variable is a named box that stores a value so you can use it later.
변수는 값을 저장해두고 나중에 꺼내 쓸 수 있는 이름 붙은 상자이다. 

# 5. Data Type(자료형) : A data type tells Python what kind of value a variable holds, like a number or text.
자료형은 변수에 담긴 값이 숫자인지 글자인지 등을 알려주는 종류를 말한다.

# 5-1. int(정수) - 소수점없는 숫자
# 5-2. float(실수) - 소수점 있는 숫자
# 5-3. str(문자열) - 글자, 텍스트 *문자열은 반드시 " " 로 감싸줘야함

# 6. input(): Gets text the user types and returns it, always as a string.
input()은 사용자가 입력한 값을 받아오는 함수이다. 무엇을 입력하든 항상 문자열(str)로 받아온다.

# 7. print(): You can combine values using commas (auto adds spaces) or f-strings (lets you control spacing and format freely).
print()로 여러 값을 합칠 때, 콤마(,)를 쓰면 값 사이에 자동으로 공백이 들어가고, f-string(f"...")을 쓰면 공백과 형태를 내가 원하는 대로 조절할 수 있다.

# 8. Type Conversion(타입 변환): Values from input() are always strings, so you must convert them with int() or float() before doing math.
input()으로 받은 값은 항상 문자열이기 때문에, 숫자로 계산하려면 int()나 float()로 변환해야 한다.

# 9. if / else: Lets your program choose between two blocks of code depending on whether a condition is true or false.
조건이 참인지 거짓인지에 따라 서로 다른 코드 블록을 실행하게 해주는 문법이다. if 다음 줄은 반드시 들여쓰기(스페이스 4칸)로 구분해야 한다.

# 10. Comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`): Compare two values and return True or False, unlike `=` which assigns a value.
두 값을 비교해서 True/False를 반환하는 연산자이다. `=`는 값을 대입하는 것이고 `==`는 두 값이 같은지 비교하는 것이라 완전히 다르다.

# 11. `%` (modulo/나머지 연산자): Returns the remainder of a division, and always returns a value between 0 and (divisor - 1), even for negative numbers.
나눗셈의 나머지를 구하는 연산자이다. 음수여도 결과는 항상 0 이상, 나누는 수 미만으로 나온다. `x % 2 == 0`이면 짝수, 아니면 홀수로 판별할 수 있다.

# 12. elif: Lets you check additional conditions in order when the first `if` condition is false, before falling back to `else`.
첫 번째 if 조건이 거짓일 때 추가 조건을 순서대로 확인하게 해주는 문법이다. 조건이 3개 이상으로 나뉠 때 사용한다 (예: 양수/음수/0 판별).
    
**13. elif 실행 순서**: `if`/`elif`/`else` chain checks conditions from top to bottom and stops at the first one that's True — every condition after that is skipped.
`if`/`elif`/`else`는 위에서부터 순서대로 조건을 확인하다가, 처음으로 참인 조건을 만나면 그 블록만 실행하고 이후 조건은 전부 건너뛴다.

**14. and, or (논리 연산자)**: `and` requires both conditions to be true, while `or` only needs one of them to be true.
`and`는 두 조건이 모두 참이어야 전체가 참이 되고, `or`는 둘 중 하나만 참이어도 전체가 참이 된다.

**15. elif 조건 순서의 함정**: When conditions overlap (like `score >= 60`), the chain must check stricter/higher conditions first, or a broad condition will match too early and block the correct branch.
`elif`로 등급을 나눌 때, 낮은 기준을 먼저 쓰면 범위가 넓어서 너무 일찍 걸려버려 원하는 결과가 안 나온다. 그래서 엄격한(높은) 조건부터 먼저 확인해야 한다 (예: 학점 매기기는 90점 이상부터 순서대로 확인).