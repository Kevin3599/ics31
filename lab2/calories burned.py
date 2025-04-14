# LAB: Expression for calories burned during workout
def calories(age, wght, h_rate, time):
    return ((age * 0.2757) + (wght * 0.03295) + (h_rate * 1.0781) - 75.4991) * time / 8.368

age = float(input())
wght = float(input())
h_rate = float(input())
time = float(input())

result = calories(age, wght, h_rate, time)
print(f'Calories: {result:.2f} calories')