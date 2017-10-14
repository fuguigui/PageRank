import numpy as np
class PageRank(object):
    def __init__(self,itr,err,alpha=0):
        self._itr_=itr
        self._error_=err
        self._alpha_=alpha

    def run(self,matrix,init,size):

        print "running the pagerank algorithm..."

        improve=1.
        before=init
        m=np.transpose(matrix)
        for i in range(self._itr_):
            comp=self._alpha_*np.dot(m, before)+(1-self._alpha_)*np.ones(size)
            improve=sum(abs(comp-before))

            i=i+1
            if improve<self._error_:
                break
            before=comp
        return comp
