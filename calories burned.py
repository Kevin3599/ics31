# LAB: Expression for calories burned during workout
def calories(age, weight, heart_rate, time):
    return ((age * 0.2757) + (weight * 0.03295) + (heart_rate * 1.0781) - 75.4991) * time / 8.368

age = float(input())
weight = float(input())
heart_rate = float(input())
time = float(input())

result = calories(age, weight, heart_rate, time)
print(f'Calories: {result:.2f} calories')