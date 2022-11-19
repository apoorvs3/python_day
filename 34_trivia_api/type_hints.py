age: int
name: str
height = float
is_human = bool

# Type hint


def check(age: int) -> bool:
    if age > 18:
        drive = True
    else:
        drive = False
    return 'This is not acceptable'


print(check('should be int'))
