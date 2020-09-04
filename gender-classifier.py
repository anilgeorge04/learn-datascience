# Source: https://www.youtube.com/watch?v=T5pRlIbr6gg
from random import randint
from sklearn import tree

# 11 people with [height, weight, shoe size] and gender labels
people = []
gender = []
for _ in range(11):
    people.append([randint(160, 190), randint(45, 95), randint(38, 48)])
    gender.append("male" if randint(0, 1) == 0 else "female")

# print(people)
# print(gender)

# Variable to store Decision Tree model
clf = tree.DecisionTreeClassifier()

# Trains the decision tree on our dataset
clf = clf.fit(people, gender)

# predict gender based on height, weight and shoe size
prediction = clf.predict([[190, 70, 43]])

print(prediction)