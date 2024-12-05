def fibonacci(n: int, resultType: str.lower):
    answer = [0, 1]

    for i in range(2, n+1):
        answer.append(answer[i-1] + answer[i-2])

    if resultType == "all":
        return answer
    elif resultType == "my":
        return answer[n]
    elif resultType == "both":
        return answer, answer[n]
    else:
        return "entry error"

user_input = int(input("Type a number: "))
result = str(input("What you want? (all, my, both): "))
print(fibonacci(user_input, result))