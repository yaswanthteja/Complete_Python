# 🎓 Scikit-learn (sklearn) Complete Guide 
---

## 🌱 0. What is Machine Learning?

> Machine Learning is teaching a computer (robot) to learn from examples instead of programming every step.

### Common ML Tasks:
- 🎯 Classification: Spam or not?
- 📈 Regression: Predict a number (like house price)
- 🧩 Clustering: Group similar things (like types of customers)

---

## 🧠 1. What is Scikit-learn?

 > Scikit-learn (sklearn) is a Python library that helps you build machine learning models easily.

Check out official documentation [here](https://scikit-learn.org/stable/)

✅ Built on:
- NumPy
- Pandas
- SciPy
- Matplotlib

🧰 It provides tools for:
- Data cleaning
- Model training
- Model evaluation
- Optimization
- Deployment

---

## 🗂️ 2. Machine Learning Project Structure

1. Load data 📂  
2. Explore data 🔍  
3. Preprocess data 🧹  
4. Split data 🪓  
5. Train model 🧠  
6. Make predictions ✨  
7. Evaluate model 📊  
8. Tune/improve model 🚀  
9. Deploy model 🌐

---

##  Installation

```
pip install scikit-learn

```



## 📂 Step 1: Load the Data

### 📦 Built-in Dataset

```python
from sklearn.datasets import load_iris
data = load_iris()

X = data.data
y = data.target

```

## For External CSV

```python
import pandas as pd

df = pd.read_csv("data.csv")
X = df.drop('target', axis=1)
y = df['target']
```





## Step 2: Explore the Data (EDA)
```python

print(X.head())        # First 5 rows
print(X.describe())    # Summary stats
print(X.isnull().sum())  # Check missing values
```


## Step 3: Preprocessing the Data
a) Handle Missing Values

```python
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)
```
b) Scaling Features

Scaling Features

It Making sure all numeric features are on the **same scale**, so one feature doesn’t dominate another.

### Why is it needed?
Some ML models (like KNN, SVM, Logistic Regression) work better when all features are in the same range.

### Example:
| Feature      | Range     |
|--------------|-----------|
| Age          | 18 - 90   |
| Salary       | 10,000 - 100,000 |

👉 Without scaling, "Salary" could overpower "Age" in the model.

### How to do it?




```python

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

c) Encoding Categorical Data

- Converting text labels into numbers so the ML model can understand them.

- Why?
    - Models can’t learn from strings like "red", "blue" or "yes", "no" — they need numbers.

- Types of encoding:
    - Label Encoding: Each category becomes a number
"male" -> 0, "female" -> 1

    - One-Hot Encoding: Each category becomes a new column
color = red, green, blue → [1,0,0], [0,1,0], [0,0,1]




```python

from sklearn.preprocessing import OneHotEncoder, LabelEncoder
```


## Step 4: Split the Data
```python

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

```


## Step 5: Train the Model
Example: Classification
```python

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X_train, y_train)
```

## Step 6: Make Predictions
```python

y_pred = model.predict(X_test)

```

## Step 7: Evaluate the Model
### Classification
- Confusion Matrix

- A table that shows how many predictions your model got right and wrong.

|                | Predicted Yes       | Predicted No        |
| -------------- | ------------------- | ------------------- |
| **Actual Yes** | True Positive (TP)  | False Negative (FN) |
| **Actual No**  | False Positive (FP) | True Negative (TN)  |


- It helps understand types of errors (e.g., is your spam detector marking real emails as spam?).

```python

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
```


### Regression
```python

from sklearn.metrics import mean_squared_error, r2_score
```

## Step 8: Improve with Cross-Validation & Tuning
a)  Cross-Validation

- Instead of using just one train-test split, split your data multiple times to get a more accurate performance estimate.

- Most common: K-Fold Cross-Validation
- Split data into k parts (e.g., 5)

- Train on 4 parts, test on 1

- Repeat k times

- Average the results


```python

from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)
print(scores.mean())
```


b) Grid Search

- An automatic method to find the best hyperparameters (settings) for your model.

- How?
    - Try all combinations of values you give

    - Pick the one that performs best on validation data

```python

from sklearn.model_selection import GridSearchCV

params = {'n_estimators': [50, 100], 'max_depth': [5, 10]}
grid = GridSearchCV(RandomForestClassifier(), param_grid=params, cv=3)
grid.fit(X_train, y_train)

print(grid.best_params_)

```

c) RandomizedSearchCV
Similar to Grid Search — but instead of trying all combinations, it tries random ones (faster!).

When to use?
When the parameter space is large and you want to save time.

```python
from sklearn.model_selection import RandomizedSearchCV

params = {'n_estimators': [10, 50, 100, 200], 'max_depth': [3, 5, 10, None]}
search = RandomizedSearchCV(RandomForestClassifier(), param_distributions=params, n_iter=5)
search.fit(X_train, y_train)

print(search.best_params_)

```




## Step 9: Use Pipelines

A way to chain preprocessing and model steps together — so they run as one workflow.

Why?
- Code becomes cleaner

- Less risk of forgetting steps (like scaling)


```python

from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier())
])

pipeline.fit(X_train, y_train)
```
## Bonus: 

### Clustering (Unsupervised Learning)
- KMeans
```python

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
print(kmeans.labels_)
```

### Dimensionality Reduction
- PCA (Principal Component Analysis)
```python

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

```


## Major sklearn Modules

| Module                    | Purpose                    |
| ------------------------- | -------------------------- |
| `sklearn.datasets`        | Sample datasets            |
| `sklearn.model_selection` | Splits, cross-validation   |
| `sklearn.preprocessing`   | Data cleaning and encoding |
| `sklearn.linear_model`    | Linear/logistic regression |
| `sklearn.ensemble`        | Random forest, boosting    |
| `sklearn.svm`             | Support vector machines    |
| `sklearn.metrics`         | Accuracy, error, scores    |
| `sklearn.pipeline`        | Combine steps              |
| `sklearn.cluster`         | KMeans, DBSCAN             |
| `sklearn.decomposition`   | PCA, NMF                   |






