# My Heart Will Go On

<img src="https://img.cinemablend.com/filter:scale/quill/7/f/f/2/d/c/7ff2dca8b628deb838445a3dc2561d9889047620.jpg?mw=600" width="50%" />

## Description

The first in-class part of today's lab focused on understanding the basics of machine learning. Now, we're going to dig into some code and write machine learning classifiers using a Python framework called scikit-learn, one of the most popular libraries for predictive analytic models in Python.

Our data set will be `Titanic.csv` file we worked with last time. We're going to create a model that will allow us to understand the characteristics that contributed to passengers suriving the sinking of the *Titanic*. Along the way, we'll learn some more about building and evaluating predctive models.

## Get the Data

Create a new directory for this lab, then copy `Titanic.csv` from last week's lab.

```
mkdir Lab_12

cd Lab_12

cp ../Lab_11/Titanic.csv .
```

Make a new file and put the following code inside it:

```
touch model.py

open model.py
```

```
import pandas as pd
import numpy as np

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Open the Titanic dataset
df = pd.read_csv('Titanic.csv')


# Print the first few lines of the dataframe
#
# Check the names and types of each column
print(df.head())
```

Save and run `model.py` and verify that you can print the head of the data set.

## Decision Tree

For our first trick, we're going to build a small decision tree from the **entire** Titanic data set. For reasons I'll explain in more detail below, you usually don't want to use the entire data set for your model, but this will let us practice creating and visualizing the tree.

Add the following lines to your code:

```
# scikit-learn can't work with arbitrary strings, like "male" and "female"
# Create a new field that turns the "Sex" string into a binary number
df['Sex_numeric'] = np.where(df['Sex'] == 'male', 1, 0)


# Pull out the Pclass, Age, and Sex_numeric columns into their own dataframe
X = df[['Pclass', 'Age', 'Sex_numeric']]


# Extract the target variable
y = df.pop('Survived').values
print(y)
```

- The first line converts the `Sex` field, which is a string `male` or `female`, into a 0/1 number; scikit-learn wants numeric features, not strings.

- The second line pulls out the three columns of training data, `Pclass`, `Age`, and the new `Sex_numeric` field.

- The third line pulls out the `Survived` column as the target variable.

Our overall goal is to build a model that can accurately predict whether a passenger survived or not based on that passenger's `Pclass`, `Age`, and `Sex`. Our first model will be a `DecisionTreeClassifier`, one of scikit-learn's built-in decision tree models. Add the following lines:

```    
# Create the Decision TreeClassifier object
# max_depth=2 restricts the size of the tree to only two splits
clf = tree.DecisionTreeClassifier(max_depth=2)


# Fit the decision tree
# Our goal is to predict Survival based on Pclass, Age, and Sex
clf.fit(X, y) 
```

Setting `max_depth=2` restricts the tree-generation algorithm to only performing two splits. We'll explore the implications of this a little later.

Re-run the model. You won't see any output yet, but you can verify that everything loads and runs correctly.

## Visualize the Tree

Decision trees lend themselves to visual inspection. Add the following line to script, which outputs the content of the trained tree to a file called `tree.dot`. The file is the GraphViz format, which is used to visualize graph-based models. The extra parameters control some additional styling and presentation options for the tree.

```
tree.export_graphviz(clf, out_file='tree.dot', feature_names=['Pclass', 'Age', 'Sex_numeric'],
                     class_names=['Did not survive', 'Survived'],  filled=True, rounded=True, special_characters=True,
                     proportion=True)
```


Re-run the script, then print the contents of `tree.dot`:

```
cat tree.dot
```

Highlight and copy the output (**make sure to include the final terminating `}` that closes the code block**).  Go to the link below, remove any existing code, then paste your code into the window to view the model.

https://dreampuf.github.io/GraphvizOnline/

You can click on the model to download it and then open it up in a larger window.

**Copy your tree into your lab document**.

Start by looking at the root node.

- The root corresponds to the entire data set. Look for "100%" in the middle of the node.

- The percentages at the bottom express the proportion of passengers at the root node (which is the entire set of passengers) that did not vs. did survive the sinking of the *Titanic*. Overall, 61.4% of passengers **did not survive** the sinking and 38.6% did. Therefore, if you had to assign a class to a passenger given no additional information, your highest probability outcome would be **Did Not Survive**.

- The second line of the node says `gini = `. This is the GINI coefficient, a measure of the "impurity" of the node. You may have heard of the GINI coefficient before, because it's widely used in economics as a measurement of inequality. Interpreting the score is kind of difficult (it's an abstract nonlinear measurement), but in our case, GINI scores close to 0 are **good**, because they indicate a node that is composed mostly of one class. Higher GINI scores correspond to **greater impurity**, which indicates nodes that should be further subdivided. In general, the decision tree algorithm works by looking for splits that lead the "pure" nodes, as measured by maximizing the change in GINI coefficient.

- The top line of the node indicates the test used to divide the entire group into two subgroups. Here, the top-level test is `Sex_numeric < .5`. Recall that `Sex_numeric` is 0/1 variable where 0 indicates female and 1 indicates male. Therefore, the top-level split in the tree is separating the passengers into a women (in the left branch) and men (in the right branch).

The node on the left corresponds to all women, which make up 35.4% of the data set.

- **Question**: What is the probability that an arbitrary woman survived the sinking?

- **Question**: What is the second-level split used to further separate the women?

- **Question**: What can you say about women in the 1st and 2nd passenger classes vs. women in the 3rd class? What were the differences in their survival rates?

The node on the right corresponds to all men, which made up 64.6% of the data set.

- **Question**: What is the probability that an average man survived the sinking?

- **Question**: What is the second-level split used to further separate the men? What differences in survival rates do you observe between the two second level categories?


## Practice

Use the decision tree to predict whether each of the following three hypothetical passengers did or did not survive the sinking. **Write your predictions in your lab document**.

```
Pclass    Age    Sex
------    ---    ---
1         11     M
2         34     F
3         58     F
```

## Bigger Trees

Now return to your script and change the `max_depth=2` parameter of `DecisionTreeClassifier` to `max_depth=10`. Re-run the model and follow the steps above to visualize the tree.

**Question**: What qualitative comparisons can you make between this tree and the previous tree? Do you think this tree is going to be a **more accurate** classifier than the last one? Why or why not?


## Training and Testing

Here is a key challenge of machine learning: We need to create models that have enough complexity to make accurate predictions, but not so much complexity that they **overfit** the data.

**Question**: Do a little Internet research and find a definition of overfitting. Why is overfitting bad for ML models?

Predictive models are almost always training on two different, mutually exclusive data sets:

- A **training set** that is used to build the model and set its parameters.

- A **testing set** that is used to verify how well the model generalizes to data that wasn't used for its training.

Put this line **before** the line of your script that calls `clf.fit`. The function partitions the complete data set into training and testing subsets.

```
# Split the complete data set into training and testing subsets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.33)
```

Change the `clf.fit` line to:

```
clf.fit(X_train, y_train)
```

Finally, add lines to evalute to evaluate the accuracy of the fitted model. First, make predictions for each of the test data points, then compare the predicted results to the true, correct classifications for those points.

```
# Test the fitted model on the testing subset
y_pred = clf.predict(X_test)


# Output the accuracy of the model
# Calculated by comparing the predicted classifications of the test set to the
# correct classifications
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)
```

**Question**: What is the accuracy of the model with a depth of 2? What is the accuracy of the model with a depth of 10?

## Finding a good depth

Intuitively, increasing the tree's depth should make classification accuracy go up: You have more rule and can slice the data into finer and finer subsets. However, there's likely to be a point of diminishing returns, beyond which adding more nodes doesn't substantially increase the performance of the tree.

**Question**: Evaluate your model for settings of `max_depth` from 1 to 20. Record the accuracy generated in each case. Does your data suggest a good tradeoff points between the size of the tree and classification accuracy?

## MNIST

<img src="https://upload.wikimedia.org/wikipedia/commons/2/27/MnistExamples.png" width="50%" />

The MNIST database is a set of handwritten digit images, widely used as an example data set in computer vision and classification research.

**Question**: What does MNIST stand for? Where did the image data come from?

The goal of the MNIST classification problem is to create a classifier that can correctly identify the handwritten digits. Each image in the original data set is 8 x 8, so each "point" in the data set is a vector of 64 image pixel values.

Create a file called `mnist.py` and put the following code inside it:

```
import pandas as pd
import numpy as np

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, plot_confusion_matrix
from sklearn.ensemble import RandomForestClassifier

from sklearn.datasets import load_digits

digits = load_digits()

# flatten the images
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

clf = DecisionTreeClassifier()

# Split data into 50% train and 50% test subsets
X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.50, shuffle=False)

# Learn the digits on the train subset
clf.fit(X_train, y_train)

# Predict the value of the digit on the test subset
predicted = clf.predict(X_test)

accuracy = accuracy_score(predicted, y_test)
print(accuracy)
```

MNIST is built into scikit-learn. The first lines load the data set, then reshape the 8 x 8 images into 64 element linear vectors (scikit-learn does not want rectangular image inputs). The remaining lines are similar to the previous model: create the classifier, split into train and test subsets, train the model, and evalue the accuacy of the fitted model.

**Question**: What is the accuracy of this MNIST classification model?

**Question**: Experiment with changing the `max_depth` of the tree. What effects does changing depth have on the output?

## Land of Confusion

Accuracy, of course, is a single measurement, but the MNIST problem has **ten classes**, one for each digit 0-9. It would be interesting to learn which digits are at greater risk of being misclassified. For example, it seems more likely that 1 and 7 could be confused for each other than 1 and 0.

Add the following code to generate a **confusion matrix**. Download and open the matrix, then **copy it into your lab document**.

```
plot_confusion_matrix(clf, X_test, y_test)

plt.savefig('confusion.pdf', bbox_inches='tight')
plt.close()
```

The diagonals of the matrix correspond to correct classifications. The other cells correspond to misclassified pairs. Each cell shows the **count** of items that fell into each category.

**Question**: What are the two most-frequently misclassified digit pairs?


## Random Forests

Decision trees are a good model, but not every kind of model is appropriate for every problem. Let's try a different model and see if we can obtain better results. Change `DecisionTreeClassifer` to `RandomForestClassifier`.

A random forest, as the name implies, is a classificaiton model bulit from a **collection** of decision trees (because a forest is a group of trees, get it?). The random forest algorithm builds a large number of small decision trees using a randomized process so that each tree is forced to use different features. Given an input, its classification is determined by the **overall consensus** of the set of decision trees. Usually, the classification is determined by simple majority vote, but more complex weighting schemes are possible. Combining multiple simpler classifers to build a more complex predictor is called an **ensemble model**.

**Question**: What is the impact of random forest classifier on prediction accuracy? Does it lead to any significant changes in the misclassified pairs in the confusion matrix?


## Neural Networks

For your last part, watch the first ~15 minutes of this video on the application of neural networks to the digit classification problem (you can stop watching when you get to the part with a lot of math):

https://www.youtube.com/watch?v=aircAruvnKk&vl=en

~**Question**: Summarize the author's argument for why a multi-layer neural network is well-suited to the digit classification problem? What is each layer in the model doing?~


## Submission

Submit your document containing the answers to the questions and the plots to Canvas.
