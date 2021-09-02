# Project Scope

This Module help to select the base model over various ML Algorithms for our classification

## Installation

```bash
pip3 install maxiverse (or) pip3 install maxiverse_(version)
```

## Usage

```python
>>> from maxiverse.classifier.evaluator import EvalModel
>>> 
>>> EvalModel._has_classifier()
# ['logreg', 'svm', 'dtree', 'rnf', 'nvbys', 'adabst', 'knn', 'xgbst']
>>> 
>>> 
>>> EvalModel(X_train, Y_train, 10)._perform_validate(['knn'])
         KNearestClassifier	Best Score
Accuracy	0.978644	    KNearest Classifier
Precision	0.992221	    KNearest Classifier
Recall	    0.964826	    KNearest Classifier
F1 Score	0.978320	    KNearest Classifier
>>> 
>>> EvalModel(X_train, Y_train, 20)._perform_validate(['knn', 'rnf'])
         KNearestClassifier	Random Forest Best Score
Accuracy	0.978644	      0.983600    RandomForest
Precision	0.992221	      0.994982    RandomForest
Recall	    0.964826	      0.972086    RandomForest
F1 Score	0.978320	      0.983391    RandomForest
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)