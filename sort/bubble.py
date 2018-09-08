'''

@author: gongyo
'''
import inspect


def swap(src1, i, j):
    tmp = src1[i];
    src1[i] = src1[j];
    src1[j] = tmp;
    return src1;


class SortLearner:

  def getCurrentMethod(self):
    return inspect.stack()[1][3]

  def bubbleSort(self, src1):
    print '===', self.getCurrentMethod();
    print "source: ", src1;
    for i in range(0, len(src1)):
      j = 0
      for j in range(0, len(src1) - i - 1):
        if src1[j] > src1[j + 1]:
          swap(src1, j, j + 1)
    print "result: ", src1;
    return src1;

  def selectionSort(self, src1):
    print '===', self.getCurrentMethod();
    print "source: ", src1;
    for i in range(0, len(src1)):
      minIndex = i;
      for j in range(i + 1, len(src1)):
        if src1[j] < src1[minIndex]:
          minIndex = j
      if minIndex != i:
        swap(src1, i, minIndex)
    print "result: ", src1;
    return src1;

  def insertSort(self, src1):
    print '===', self.getCurrentMethod();
    return src1;
  
  def _mergeConque(self, src1, left, mid, right):
    i=0
    j=0
    while i<=mid and j <=right:
      pass;

  def _mergeDivide(self, src1, left, right):
    if(left < right):
      mid = (right + left) / 2
      self._mergeDivide(src1, left, mid)
      self._mergeDivide(src1, mid + 1, right)
      self._mergeConque(src1, left, mid, right)

  def mergeSort(self, src1):
    print '===', self.getCurrentMethod();
    self._mergeDivide(src1, 0, len(src1) - 1);
    return src1;

  
if __name__ == '__main__':
  pass
  src1 = [7, 3, 0, 1, 8, 9, 5];
  
  learner = SortLearner()
  learner.bubbleSort(src1[:])
  learner.selectionSort(src1[:])
  learner.mergeSort(src1[:])
