from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    num_train=X.shape[0]
    for i in range(num_train):
        score=X[i].dot(W)
        score-=np.max(score)
        p=np.exp(score)/np.sum(np.exp(score))
        loss+=-np.log(p[y[i]])
        dW[:,y[i]]-=X[i].T
        matrix=((X[i,:].T).reshape(-1,1)).dot(p.reshape(1,-1))
        dW+=matrix
    loss/=num_train
    loss+=reg*np.sum(W*W)
    dW/=num_train
    dW+=2*reg*W
    
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    num_train=X.shape[0]
    score=X.dot(W)
    score1=score.T
    score1-=np.max(score,axis=1)
    score=score1.T
    p1=np.exp(score1)/np.sum(np.exp(score),axis=1)
    p=p1.T
    loss=-np.sum(np.log(p[range(num_train),y]))
    loss/=num_train
    loss+=reg*np.sum(W*W)
  
    matrix=(X.T).dot(p)
    dW+=matrix
    for i in range(num_train):
        dW[:,y[i]]-=X.T[:,i]
    dW/=num_train
    dW+=2*reg*W
    
    
    

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW
