# input -1 <= x <=1, -1 <= y <= 1

x = float(input("x: "))
y = float(input("y: "))

left = y + x
right = y - x

# Option 1: Scale 2 to maximum for each
print("\nOption 1")
print("Left: " + str(left / 2))
print("Right: " + str(right / 2))

# Option 2: Scale 1 to maximum, but if left or right greater than 1, scale so that largest value is at 1
print("\nOption 2")
if left > 1 or right > 1:
    greater = max(left, right)
else:
    greater = 1
print("Left: " + str(left / greater))
print("Right: " + str(right / greater))

# Option 3: Neccesary because of the current non-reversing ability of the motors


