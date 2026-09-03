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

# 27. while 반복문**: A while loop repeats its block of code as long as a given condition remains true, checking that condition again before every iteration — unlike for, the number of repetitions isn't fixed in advance.

while문은 주어진 조건이 참인 동안 코드 블록을 계속 반복하며, 매 반복 전에 조건을 다시 확인한다 — for문과 달리 반복 횟수가 미리 정해져 있지 않다.

# 28. 무한 루프(infinite loop)**: If nothing inside a while loop ever changes the condition to false, the loop will never stop and must be force-terminated (e.g. with Ctrl+C).

while문 안에서 조건을 거짓으로 만들어줄 코드가 없으면 반복문이 영원히 멈추지 않으며, 이 경우 Ctrl+C 같은 방법으로 강제 종료해야 한다.

# 29. for vs while 선택 기준**: Use for when the number of iterations is known or based on a fixed sequence (like a range); use while when the loop should continue until a condition changes, with the number of iterations unknown in advance.

반복 횟수가 정해져 있거나 고정된 범위(range 등)를 도는 경우엔 for문을, 조건이 바뀔 때까지 계속 반복해야 하고 몇 번 반복될지 미리 알 수 없는 경우엔 while문을 사용한다.

# 30. while 조건 변수의 사전 초기화**: A variable used in a while condition must already exist before the loop starts, since the condition is checked before the loop body ever runs — so it needs an initial value that won't accidentally make the condition true (or false) too early.

while문의 조건에 쓰이는 변수는 반복문 몸통이 실행되기도 전에 조건이 먼저 확인되기 때문에, 반복 시작 전에 미리 존재해야 한다 — 이때 조건을 너무 일찍 참(또는 거짓)으로 만들지 않는 초기값을 넣어줘야 한다.

# 31. input()은 항상 문자열을 반환**: The input() function always returns a string, even if the user types digits, so it must be converted with int() (or float()) before being used in numeric comparisons or arithmetic.

input() 함수는 사용자가 숫자를 입력해도 항상 문자열(str)을 반환하기 때문에, 숫자 비교나 계산에 쓰려면 int()(또는 float())로 변환해야 한다.

# 32. 하드코딩보다 변수 재사용**: When the same value is used in multiple places (like a target number checked in several conditions), storing it in one variable and reusing that variable is better than repeating the literal value, since it only needs to be updated in one place later.

같은 값이 여러 곳에서 쓰일 때(예: 여러 조건에서 비교하는 목표 숫자), 그 값을 리터럴로 반복해서 쓰는 것보다 변수 하나에 저장해서 재사용하는 것이 낫다 — 나중에 값을 바꿀 때 한 곳만 고치면 되기 때문이다.
앞에 # 붙여줘

# 33. 리스트(List)**: A list is an ordered collection that can hold multiple values together in a single variable, created with square brackets [] and comma-separated items.
리스트는 여러 개의 값을 하나의 변수에 순서대로 담는 자료구조로, 대괄호 []와 쉼표로 구분된 값들로 만든다.

# 34. 인덱스(index)와 0부터 시작하는 규칙**: Each item in a list has a position number called an index, and Python starts counting from 0, so the first item is list[0], not list[1].
리스트 안의 각 값은 인덱스라는 위치 번호를 가지며, 파이썬은 0부터 세기 때문에 첫 번째 값은 list[1]이 아니라 list[0]이다.

# 35. 음수 인덱스**: Negative indices count from the end of the list, so list[-1] refers to the last item and list[-2] to the second-to-last.
음수 인덱스는 리스트의 끝에서부터 세며, list[-1]은 마지막 값을, list[-2]는 뒤에서 두 번째 값을 가리킨다.

# 36. len() 함수**: The len() function returns the number of items stored in a list (or the length of a string).
len() 함수는 리스트에 담긴 값의 개수(또는 문자열의 길이)를 반환한다.

# 37. 리스트를 for문에 바로 사용**: A list can be passed directly into a for loop, and each iteration automatically retrieves the next value in order — no index or range() is needed.
리스트는 for문에 바로 넣을 수 있으며, 반복할 때마다 인덱스나 range() 없이도 순서대로 값을 하나씩 자동으로 꺼내준다.

# 38. append() — 값 추가**: The append() method adds a new item to the end of a list.
append() 메서드는 리스트의 맨 뒤에 새로운 값을 추가한다.

# 39. remove() — 값 제거**: The remove() method deletes a specified value from a list by its actual value, not its index — and raises an error if that value isn't found in the list.
remove() 메서드는 인덱스가 아니라 실제 값을 기준으로 리스트에서 해당 값을 제거하며, 리스트에 그 값이 없으면 에러가 발생한다.

# 40. 리스트를 통째로 출력할 때의 형태**: Printing an entire list displays it with brackets, quotes, and commas exactly as Python represents it internally (e.g. ['a', 'b']), which differs from printing individual items one at a time.
리스트 전체를 print()로 출력하면 파이썬 내부 표현 그대로 대괄호, 따옴표, 쉼표가 포함된 형태(예: ['a', 'b'])로 나오며, 이는 개별 값을 하나씩 출력하는 것과는 다른 형태다.

