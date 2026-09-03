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

# 16. for 반복문: A for loop repeats a block of code once for each item in an iterable (like a list or range()), automatically stopping when it runs out of items.
for문은 반복 가능한 대상(리스트, range() 등) 안의 값을 하나씩 꺼내면서 코드 블록을 반복 실행하고, 더 이상 꺼낼 값이 없으면 자동으로 멈춘다.

# 17. range() 함수: range(start, stop) generates a sequence of numbers from start up to, but not including, stop.
range(시작, 끝)은 시작값부터 끝값 직전까지의 숫자를 만들어내며, 끝값 자체는 포함되지 않는다 (예: range(1, 11)은 1~10).

# 18. 반복 변수 vs 원본 대상: The variable after in (e.g. x) refers to the whole unchanging sequence, while the loop variable (e.g. i) is reassigned to a new value from that sequence on every iteration.
in 뒤에 오는 대상(x)은 반복 내내 변하지 않는 전체 범위를 가리키고, 반복 변수(i)는 매 반복마다 그 안에서 꺼내진 새로운 값으로 계속 바뀐다.

# 19. 누적 패턴 (accumulator pattern): To sum values across iterations, initialize a variable (e.g. total = 0) outside the loop, then update it inside the loop with total += i so each iteration builds on the previous result.
반복하면서 값을 누적해서 더하려면, 반복문 밖에서 변수를 초기화(total = 0)한 뒤 반복문 안에서 total += i로 계속 갱신해야 이전까지 쌓인 값이 유지된다.

# 20. 초기화가 필요 없는 경우: If a variable is recalculated fresh from scratch on every iteration (not built on the previous value), it doesn't need to be initialized before the loop.
매 반복마다 이전 값과 상관없이 새로 계산되기만 하는 변수(예: result = 2*i)는 반복문 전에 미리 초기화할 필요가 없다 — 누적 여부가 초기화 필요성을 가른다.

# 21. f-string: Writing f"..." before a string lets you embed variables or expressions directly inside {}, which get evaluated and inserted at that position.
문자열 앞에 f를 붙이면(f"...") 중괄호({}) 안에 변수나 계산식을 넣을 수 있고, 그 값이 계산되어 그 자리에 바로 삽입된다.

# 22. 중첩 for문 (nested for loop): A for loop placed inside another for loop, where the inner loop runs completely from start to finish every single time the outer loop advances by one step.
for문 안에 또 다른 for문을 넣는 구조로, 바깥 반복문이 한 단계 진행될 때마다 안쪽 반복문이 처음부터 끝까지 통째로 전부 실행된다.

# 23. 중첩 for문의 총 실행 횟수: The total number of iterations in a nested loop equals the outer loop's count multiplied by the inner loop's count.
중첩 반복문의 전체 실행 횟수는 "바깥 반복 횟수 × 안쪽 반복 횟수"로 계산된다 (예: 바깥 3번 × 안쪽 2번 = 총 6번).

# 24. 들여쓰기와 소속 관계: The level of indentation determines which loop (or block) a line of code belongs to — one level in means it's inside the outer loop, two levels in means it's inside the inner loop.
들여쓰기 단계가 코드가 어느 블록에 속하는지를 결정한다 — 한 단계 들여쓰면 바깥 반복문 안, 두 단계 들여쓰면 안쪽 반복문 안에 속한다.

# 25. 문자열 반복(*): Multiplying a string by an integer with * repeats and concatenates that string that many times, producing one combined string — this differs from multiplying a list, which nests the item inside a longer list instead of joining characters.
문자열에 정수를 곱하면("★" * 3) 그 문자열이 그만큼 반복되어 하나로 이어붙은 문자열이 만들어진다 — 반면 리스트를 곱하면 문자가 이어붙는 게 아니라 리스트 안에 원소가 반복되어 담긴 리스트가 만들어져 결과가 다르다.

# 26. 반복 변수 보존 원칙: The loop variable (e.g. i) should be kept as-is for its original role (like a counter), and any computed result should be stored in a separate new variable instead of overwriting it.
반복 변수(i)는 원래 역할(예: 몇 번째 반복인지 세는 용도)을 유지하도록 그대로 두고, 계산된 결과는 별도의 새 변수(예: line)에 저장해야 한다 — 그래야 나중에 반복 변수를 다시 원래 용도로 쓸 수 있고 코드도 헷갈리지 않는다.