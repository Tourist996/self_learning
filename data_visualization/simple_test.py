import matplotlib.pyplot as plt
numbers = range(1, 1001)
squares = [i * i for i in numbers]

plt.style.use('seaborn-v0_8-dark')
fig, ax = plt.subplots()
print(plt.style.available) #to see which style you can use in your system
# ax.plot(numbers, squares, linewidth=3)
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# ax.tick_params(labelsize=14)
ax.scatter(numbers, squares, color=(0, 0.8, 0), s=2)
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Square of Value", fontsize=14)
ax.tick_params(labelsize=14)
plt.show()