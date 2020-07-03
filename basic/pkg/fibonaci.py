class Fibonacci:
    def __init__(self, title="fibonnacci"):
        self.title = title

    def fib(n):
        a, b = 0, 1 
        while a < n:
            print(a, end = ' ') # 줄바꿈없이 출력
            a,b = b, a+b
        print()

    def fib(n):
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a,b = b, a+b
        return result    