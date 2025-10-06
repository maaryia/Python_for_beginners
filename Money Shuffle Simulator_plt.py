import matplotlib.pyplot as plt
import random

random.seed()

people = []
for i in range(0, 50):
    people.append(100)

for x in range(0, 10):
    for person1 in range(0, 50):
        person2 = random.randrange(0, 50)
        while people[person2] == 0:
            person2 = random.randrange(0, 50)
        if people[person1] != 0:
            people[person1] = people[person1] - 1
            people[person2] = people[person2] + 1

plt.bar(range(0, 50), sorted(people, reverse=True))
plt.show()


#ُSECOND WAY
# import matplotlib.pyplot as plt
# import random

# # Set a seed for reproducibility
# random.seed(42)

# # Create a list of 50 people with 100 resources each
# people = [100 for _ in range(50)]

# # Simulate resource transfer between people
# for _ in range(100):
#     person1 = random.randint(0, 49)
#     person2 = random.randint(0, 49)
    
#     # Ensure person2 has resources to give
#     while people[person2] == 0:
#         person2 = random.randint(0, 49)
    
#     # Transfer one resource from person1 to person2
#     if people[person1] > 0:
#         people[person1] -= 1
#         people[person2] += 1

# # Plot the final distribution of resources
# plt.figure(figsize=(10, 6))
# plt.bar(range(len(people)), sorted(people, reverse=True))
# plt.xlabel("Person")
# plt.ylabel("Resources")
# plt.title("Distribution of Resources")
# plt.show()