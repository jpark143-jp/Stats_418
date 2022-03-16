from algorithms.classifiers import loss_grad_svm_vectorized
from algorithms.gradient_check import grad_check_sparse
from algorithms.classifiers import loss_grad_svm_vectorized
import time

# weights W 
W = np.random.randn(10, x_train.shape[0]) * 0.001

tic = time.time()
loss_vec, grad_vect = loss_grad_svm_vectorized(W, x_train, y_train, 0)
toc = time.time()
print 'Vectorized loss: %f, and gradient: computed in %fs' % (loss_vec, toc - tic)

def grad_check_sparse(f, x, analytic_grad, num_checks):

  h = 1e-5

  print x.shape

  for i in xrange(num_checks):
    ix = tuple([randrange(m) for m in x.shape])
    print ix
    x[ix] += h # increment by h
    fxph = f(x) # evaluate f(x + h)
    x[ix] -= 2 * h # increment by h
    fxmh = f(x) # evaluate f(x - h)
    x[ix] += h # reset

    grad_numerical = (fxph - fxmh) / (2 * h)
    grad_analytic = analytic_grad[ix]
    rel_error = abs(grad_numerical - grad_analytic) / (abs(grad_numerical) + abs(grad_analytic))
    print 'numerical: %f analytic: %f, relative error: %e' % (grad_numerical, grad_analytic, rel_error)
    

f = lambda w: loss_grad_svm_vectorized(w, x_train, y_train, 0)[0]
grad_numerical = grad_check_sparse(f, W, grad_vect, 10)

# Svm regression classifier using SGD
from algorithms.classifiers import SVM

# SGD algorithm
SVM_sgd = SVM()
tic = time.time()
losses_sgd = SVM_sgd.train(x_train, y_train, method='sgd', batch_size=200, learning_rate=1e-6,
              reg = 1e5, num_iters=1000, verbose=True, vectorized=True)
toc = time.time()
print 'Traning time for SGD with vectorized version is %f \n' % (toc - tic)

y_train_pred_sgd = SVM_sgd.predict(X_train)[0]
print 'Training accuracy: %f' % (np.mean(y_train == y_train_pred_sgd))

