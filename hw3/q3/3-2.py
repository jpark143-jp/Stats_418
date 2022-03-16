# Evaluation Metrics

from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import roc_auc_score
import sklearn.metrics as metrics

score_train= model.score(x_train,y_train)
score_test= model.score(x_test,y_test)
y_pred = model.predict(x_test)
cv = cross_val_score(model, x_test, y_test).mean()
auc_roc = roc_auc_score(y_test, y_pred)
recall= metrics.recall_score(y_test, model.predict(x_test))


cm =metrics.confusion_matrix(y_test, model.predict(x_test),labels=[0,1]) # Constructing Confusion Matrix
specificity=cm[0][0]/sum(cm[0])

print(cm)

############################# model = gscv #############################
# (a) Pipeline for PCA & nmf (Non-negative Matrix Factorization)

clf = Pipeline([('pca', decomposition.PCA(n_components=150, whiten=True)),
                ('nmf', nmf())])

clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

### Eval ####

print(metrics.confusion_matrix(y_pred, y_test))

score_train= clf.score(x_train,y_train)
score_test= clf.score(x_test,y_test)
cv = cross_val_score(clf, x_test, y_test).mean()
auc_roc = roc_auc_score(y_test, y_pred)
recall= metrics.recall_score(y_test, clf.predict(x_test))


# (b) GridSearch for four classification

for Model in [KNN, LR, model, SVM_sgd]:
    gscv = GridSearchCV(Model(), dict(alpha=alphas), cv=3).fit(x_train, y_train)
    print('%s: %s' % (Model.__name__, gscv.best_params_))
    
### Eval ####

print(metrics.confusion_matrix(y_pred, y_test))

score_train= gscv.score(x_train,y_train)
score_test= gscv.score(x_test,y_test)
cv = cross_val_score(gscv, x_test, y_test).mean()
auc_roc = roc_auc_score(y_test, y_pred)
recall= metrics.recall_score(y_test, gscv.predict(x_test))
   
# (c) GridSearch for binary classification (RandomForest, XGBoost)

RF = RandomForestClassifier()
RF.fit(x_train, y_train)

xgb = XGBClassifier(eval_metric='logloss',use_label_encoder =False)
xgb.fit(x_train, y_train)

for Model in [RF, xgb]:
    gscv = GridSearchCV(Model(), dict(alpha=alphas), cv=3).fit(x_train, y_train)
    print('%s: %s' % (Model.__name__, gscv.best_params_))
    
### Eval ####
print(metrics.confusion_matrix(y_pred, y_test))

score_train= gscv.score(x_train,y_train)
score_test= gscv.score(x_test,y_test)
cv = cross_val_score(gscv, x_test, y_test).mean()
auc_roc = roc_auc_score(y_test, y_pred)
recall= metrics.recall_score(y_test, gscv.predict(x_test))

# (d) Type of regularization ( Lasso, Ridge )
from sklearn.linear_model import Ridge, Lasso

for Model in [Ridge, Lasso]:
    gscv = GridSearchCV(Model(), dict(alpha=alphas), cv=3).fit(X, y)
    print('%s: %s' % (Model.__name__, gscv.best_params_))
    
### Eval ####

print(metrics.confusion_matrix(y_pred, y_test))

score_train= gscv.score(x_train,y_train)
score_test= gscv.score(x_test,y_test)
cv = cross_val_score(gscv, x_test, y_test).mean()
auc_roc = roc_auc_score(y_test, y_pred)
recall= metrics.recall_score(y_test, gscv.predict(x_test))
 




