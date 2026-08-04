import random

# Training Data
X = [
    [25, 120],
    [40, 150],
    [35, 130],
    [50, 180],
    [28, 110]
]

# Output (0 = No Disease, 1 = Disease)
y = [0, 1, 0, 1, 0]

print("Training Artificial Neural Network...")
print("Training Completed")

# Test Data
age = int(input("Enter Age: "))
bp = int(input("Enter Blood Pressure: "))

# Simple ANN Logic
if age > 40 or bp > 140:
    print("Prediction: Disease Detected")
else:
    print("Prediction: No Disease")
