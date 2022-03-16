from sklearn.grid_search import GridSearchCV
from sklearn.linear_model import Ridge, Lasso
from KNN import KNN
from Logistic_regression import LR
from Perceptron import model
from SVC import SVM_sgd
from sklearn.pipeline import Pipeline

# (a) Pipeline for PCA & nmf (Non-negative Matrix Factorization)

clf = Pipeline([('pca', decomposition.PCA(n_components=150, whiten=True)),
                ('nmf', nmf())])

clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)
print(metrics.confusion_matrix(y_pred, y_test))

# (b) GridSearch for four classification

for Model in [KNN, LR, model, SVM_sgd]:
    gscv = GridSearchCV(Model(), dict(alpha=alphas), cv=3).fit(x_train, y_train)
    print('%s: %s' % (Model.__name__, gscv.best_params_))
   
# (c) GridSearch for binary classification (RandomForest, XGBoost)

RF = RandomForestClassifier()
RF.fit(x_train, y_train)

xgb = XGBClassifier(eval_metric='logloss',use_label_encoder =False)
xgb.fit(x_train, y_train)

for Model in [RF, xgb]:
    gscv = GridSearchCV(Model(), dict(alpha=alphas), cv=3).fit(x_train, y_train)
    print('%s: %s' % (Model.__name__, gscv.best_params_))
    
# (d) Type of regularization ( Lasso, Ridge )
from sklearn.linear_model import Ridge, Lasso

for Model in [Ridge, Lasso]:
    gscv = GridSearchCV(Model(), dict(alpha=alphas), cv=3).fit(X, y)
    print('%s: %s' % (Model.__name__, gscv.best_params_))
