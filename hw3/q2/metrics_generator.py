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
recall= metrics.recall_score(y_test, basemodel.predict(x_test))


cm =metrics.confusion_matrix(y_test, model.predict(x_test),labels=[0,1]) # Constructing Confusion Matrix
specificity=cm[0][0]/sum(cm[0])

print(cm)

