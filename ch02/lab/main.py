import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 10
cost_per_class = cost_per_week/classes_per_week
print(cost_per_class, "dollars is the cost per class.")
print(weeks, type(weeks))
print(classes, type(classes))
print(tuition, type(tuition))
print(cost_per_week, type(cost_per_week))
print(classes_per_week, type(classes_per_week))
print(cost_per_class, type(cost_per_class))


#Part B
ice_cream_flavors = ("Vanilla", "Chocolate", "Mint", "Banana", "Cookies and Cream")
best_flavor = random.choice(ice_cream_flavors)
print(best_flavor)