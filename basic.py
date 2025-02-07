print("Hello Python World!")
message = "Hello Python World!"
print(f"origin message is {message}")
print(f".lower() message is {message.lower()}")
print(f"after .lower() message is {message}") #test whether .lower() changes the value of message
print(f".upper() message is {message.upper()}")
print(f".title() message is {message.title()}")
print(f"\t{message}")

blankDel = " python "
print(blankDel)
print(blankDel.lstrip())
print(blankDel.rstrip())
print(blankDel.strip())
print(blankDel)

url = "https://xxx"
data = "xxx.csv"
print(url.removeprefix("https://"))
print(data.removesuffix(".csv"))
print(url)
print(data)

universe_age = 14_000_000_000
print(universe_age)
x, y, z = 0, 0, 0
print(x, y, z)

MAX_N = 5000  #Use uppercase letters to indicate that a variable should be treated as a constant.
