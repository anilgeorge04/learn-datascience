# Simple ML examples from Sci-Kit Learn
# Source: https://www.youtube.com/watch?v=T5pRlIbr6gg
from random import randint
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier

# people with [height, weight, shoe size] and gender labels
people = []
gender = []
for _ in range(1000):
    people.append([randint(160, 190), randint(45, 95), randint(38, 48)])
    gender.append("male" if randint(0, 1) == 0 else "female")

# print(people)
# print(gender)

# Variable to store model
log = LogisticRegression()
dt = tree.DecisionTreeClassifier()
neigh = KNeighborsClassifier(n_neighbors=3)
gnb = GaussianNB()
rf = RandomForestClassifier(n_estimators=2)

# Trains the model on our dataset
log.fit(people, gender)
dt.fit(people, gender)
neigh.fit(people, gender)
gnb.fit(people, gender)
rf.fit(people, gender)

# predict and print gender based on height, weight, shoe size
# according to each classifier model
print("-"*3+" PREDICTIONS "+"-"*3)
print("K Neighbors: " + str(neigh.predict([[190, 70, 43]])))
print("Decision Tree: " + str(dt.predict([[190, 70, 43]])))
print("Logistic Regression: " + str(log.predict([[190, 70, 43]])))
print("Naive Bayes: " + str(gnb.predict([[190, 70, 43]])))
print("Random Forest: " + str(gnb.predict([[190, 70, 43]])))
