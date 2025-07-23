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
```python

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

c) Encoding Categorical Data
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
- Classification
```python

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
```


 - Regression
```python

from sklearn.metrics import mean_squared_error, r2_score
```

## Step 8: Improve with Cross-Validation & Tuning
a) Cross-Validation
```python

from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)
print(scores.mean())
```


b) Grid Search
```python

from sklearn.model_selection import GridSearchCV

params = {'n_estimators': [50, 100], 'max_depth': [3, 5, None]}
grid = GridSearchCV(model, params, cv=3)
grid.fit(X_train, y_train)

print(grid.best_params_)
```


## Step 9: Use Pipelines
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






