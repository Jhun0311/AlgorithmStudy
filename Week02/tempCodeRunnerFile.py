from collections import deque

print("===== Stack 구현 =====")

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("삽입 후:", stack)

removed = stack.pop()
print("삭제된 값:", removed)
print("현재 스택:", stack)


print("\n===== Queue 구현 =====")

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print("삽입 후:", list(queue))

removed = queue.popleft()
print("삭제된 값:", removed)
print("현재 큐:", list(queue))


print("\n===== 선택 정렬 =====")

arr = [64, 25, 12, 22, 11]

for i in range(len(arr)):
    min_idx = i

    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j

    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print("정렬 결과:", arr)


print("\n===== 버블 정렬 =====")

arr2 = [5, 1, 4, 2, 8]

for i in range(len(arr2)):
    for j in range(len(arr2) - 1 - i):
        if arr2[j] > arr2[j + 1]:
            arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]

print("정렬 결과:", arr2)


print("\n===== 자료구조 활용 문제 (올바른 괄호 검사) =====")

s = "(()())"

stack = []
valid = True

for ch in s:
    if ch == "(":
        stack.append(ch)
    else:
        if len(stack) == 0:
            valid = False
            break
        stack.pop()

if len(stack) != 0:
    valid = False

if valid:
    print("올바른 괄호 문자열입니다.")
else:
    print("올바르지 않은 괄호 문자열입니다.")