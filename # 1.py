# 1. create a list called foods with the strings pizza, burger, pasta
foods = ["pizza", "burger", "pasta"]

# 2. print the list to verify
print(foods)

# 3. add sushi to the list
foods.append("sushi")

# 4. create a second list, initially empty, called deserts
deserts = []

# 5. add ice cream and pie to the deserts list
deserts.extend(["ice cream", "pie"])

# 6. add the contents of deserts to foods
foods.extend(deserts)

# 7. add fries to the middle of the foods list

## 方法 1：推荐，清晰易懂 ✅
foods.insert(len(foods) // 2, "fries")

# ✅ 可选方法 2：使用切片插入
# foods[len(foods)//2:len(foods)//2] = ["fries"]

# ✅ 可选方法 3：不推荐，会生成新列表
# foods = foods[:len(foods)//2] + ["fries"] + foods[len(foods)//2:]

# 8. print the length of the foods list
print(len(foods))

# 9. create a new variable called clone, assign to copy of foods
clone = foods.copy()

# 10. remove fries from foods
foods.remove("fries")

# 11. pop 2nd item from foods
foods.pop(1)
