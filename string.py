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

# a common way to change the nth char in a string
def replace_char(original_string, n, new_char):
    if 0 <= n < len(original_string): 
        new_string = original_string[:n] + new_char + original_string[n+1:]
        return new_string
    else:
        return "索引超出字符串长度范围"

original_string = "hello"
n = 3
new_char = "p"
result = replace_char(original_string, n, new_char)
print(result) 