# Create a tuple named zoo that contains 10 of your favorite animals.
zoo = ("monkey", "eliphant", "giraffe", "zebra", "horse", "cow", "lion", "tiger", "dog", "cat")

# Find one of your animals using the tuple.index(value) syntax on the tuple.
zebra_index = zoo.index("zebra")

# Determine if an animal is in your tuple by using value in tuple syntax.
animal_to_find = "snake"

if animal_to_find in zoo:
    print(f"{animal_to_find} is in the zoo!")
else:
    print(f"{animal_to_find} is loose, take cover!!")

(first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth) = zoo
print()
print(first)
print(second)
print(third)
print(fourth)
print(fifth)
print(sixth)
print(seventh)
print(eighth)
print(ninth)
print(tenth)

# Convert your tuple into a list.
zoo = list(zoo)

# Use extend() to add three more animals to your zoo.
zoo.extend(["duck", "frog", "fish"])

# Convert the list back into a tuple.
zoo = tuple(zoo)
print()
print(zoo)