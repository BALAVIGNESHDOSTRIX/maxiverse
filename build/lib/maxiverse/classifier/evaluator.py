from maxiverse.base.abstract_base import AbstractEval


try:
  import pandas as pd
  from sklearn.metrics import make_scorer, f1_score, accuracy_score, precision_score, recall_score
  from sklearn.model_selection import cross_validate 
  from sklearn.linear_model import LogisticRegression
  from sklearn.svm import LinearSVC
  from sklearn.tree import DecisionTreeClassifier
  from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
  from sklearn.neighbors import KNeighborsClassifier
  from sklearn.naive_bayes import GaussianNB
  from xgboost import XGBClassifier
except Exception as e:
  raise str(e)

class EvalModel(AbstractEval):
    def __init__(self, x=None, y=None, fold=5):
        self._x = x
        self._y = y
        self._fold = fold 
        self._clstree = {'logreg': LogisticRegression, 'svm': LinearSVC,
                        'dtree': DecisionTreeClassifier, 'rnf': RandomForestClassifier, 
                        'adabst': AdaBoostClassifier, 'nvbys': GaussianNB,
                        'knn': KNeighborsClassifier, 'xgbst': XGBClassifier}
        self._scoring = {'accuracy':make_scorer(accuracy_score), 
            'precision':make_scorer(precision_score),
            'recall':make_scorer(recall_score), 
            'f1_score':make_scorer(f1_score)}
        
    def _has_classifier_names(self, name):
        return {
            'logreg': 'Logistic Regression',
            'svm': 'Support Vector Classifier',
            'dtree': 'Decision Tree',
            'rnf':'Random Forest',
            'nvbys':'Gaussian Naive Bayes',
            'adabst': 'AdaBoost Classifier',
            'knn': 'KNearest Classifier',
            'xgbst': 'XGBoost Classifier'
        }.get(name)
        
        
        
    @staticmethod
    def _has_classifier():
        return ['logreg', 'svm', 'dtree', 'rnf', 'nvbys', 'adabst', 'knn', 'xgbst']
    
    def _perform_validate(self,nmdl=[]):
        models_scores_table = {}
        try:
            for x in nmdl:
                if x not in self._has_classifier():
                    return "{x} - key of Classifier Not Available. so please execute _has_classifier_names() method to see available classifiers".format(x=x)
                validated_obj = self._cross_validate(self._clstree.get(x)())
                models_scores_table.update({
                    self._has_classifier_names(x) : [
                                                    validated_obj['test_accuracy'].mean(),
                                                    validated_obj['test_precision'].mean(),
                                                    validated_obj['test_recall'].mean(),
                                                    validated_obj['test_f1_score'].mean()                
                                            ]
                })
            models_scores_table = pd.DataFrame(models_scores_table, index=['Accuracy', 'Precision', 'Recall', 'F1 Score'])

            #Add 'Best Score' column
            models_scores_table['Best Score'] = models_scores_table.idxmax(axis=1)
        
            # Return models performance metrics scores data frame
            return models_scores_table
        except Exception as e:
            raise str(e)
        
    def _cross_validate(self, model):
        return cross_validate(model, self._x, self._y, scoring=self._scoring, cv=self._fold)