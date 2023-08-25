def myFunction(age: int):
    if age > 80:
        print("ur 2 old, man")


def greate(name: str) -> str:
    return f"Hi, {name}"


def add2nums(x: int, y: int):
    sum = x + y
    return sum


greate("sama")
myFunction(90)
print(add2nums(6, 7))


def main() -> None:
    friends: list[str] = ["mido", "7amada", "7oda", "mohamed"]
    for friend in friends:
        print( greate(friend))
        if "mido" in greate(friend):
            print(f"ur cute, {friend}")

def greet2():
    print("hi")        

print(greet2)
print(id(greet2))
print(type(greet2))

hi = greet2
hi()
