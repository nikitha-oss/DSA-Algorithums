from array import array

# Static Array
print("STATIC ARRAY")

static_array = array('i', [10, 20, 30, 40, 50])

print("Static array:", static_array)
print("First element:", static_array[0])
print("Third element:", static_array[2])


# Dynamic Array
print("\nDYNAMIC ARRAY")

dynamic_array = []

dynamic_array.append(10)
dynamic_array.append(20)
dynamic_array.append(30)

print("Dynamic array:", dynamic_array)

dynamic_array.append(40)
print("After adding 40:", dynamic_array)

dynamic_array.pop()
print("After removing last element:", dynamic_array)