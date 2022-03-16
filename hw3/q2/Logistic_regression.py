# Logistic Regression Model fitting

LR=LogisticRegression(C=100, solver='lbfgs', max_iter=1000)
LR.fit(x_train, np.ravel(y_train))

score_train=LR.score(x_train,y_train)
score_test=LR.score(x_test,y_test)
y_pred = LR.predict(x_test)
cv = cross_val_score(LR, x_test, y_test).mean()
