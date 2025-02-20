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

letters = ['a', 'b', 'd', 'c']
print(letters)
print(letters[-2])
letters.append('e')
print(letters)
letters.pop()
print(letters)
del letters[1]
print(letters)
letters.pop(1)
print(letters)
letters.remove('c')   #only delete the first val
print(letters)     

letters = ['a', 'b', 'd', 'c']
letters.sort()
print(letters)
letters = ['a', 'b', 'd', 'c']
print(sorted(letters))
print(letters)
letters.reverse()
print(letters)

for letter in letters:
    print(letter)
for i in range(0, 4):
    print(letters[i])
print(min(letters))
print(max(letters))
nums = [1, 2, 3, 4]
print(sum(nums))
squares = [value ** 2 for value in range(1, 11)]
print(squares)
print(nums[0:3])
print(nums[:])
nums_copy = nums[:] 
nums_2 = nums      #there is no difference between nums_2 and nums

tuple = (1, 2)
tuple = (2, 3)          #Can be assigned, but cannot modify the element's value
print(tuple)

if 1 in nums:
    print("yes")
if 5 not in nums:
    print("yes")

favorite_colors = {"c" : "red", "b" : "yellow", "a" : "green"}
print(favorite_colors["a"])
del(favorite_colors["a"])
print(favorite_colors.get("a", "no a"))
print(favorite_colors.get("b", "no b"))

for k, v in favorite_colors.items():
    print(k, v)
for k in favorite_colors.keys():
    print(k)
for v in favorite_colors.values():
    print(v)
print(sorted(favorite_colors))
print(favorite_colors)

prompt = "input some number, just now!\n"
input_num = input(prompt)
print(f"The number you input is {input_num}, but the type of the number is {type(input_num)}")
input_num = int(input_num)
print(f"Now the type of the number is {type(input_num)}")
