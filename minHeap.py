import sys

class minHeap:
  def __init__(self):
    self.data = [None] # 0번째 노드는 None
  
  def push(self, x):
    # 마지막 노드 뒤에 새로운 노드를 삽입하고 부모와 비교하며 정렬한다.
    self.data.append(x)
    here = self.size()
    while here > 1:
      if self.data[here] < self.data[here//2]:
        self.data[here], self.data[here//2] = self.data[here//2], self.data[here]
        here = here//2
      else:
        break

  def pop(self):
    # 루트노드를 마지막 노드와 위치교환 후 마지막 노드를 pop하고 루트 노드를 자식들과 비교하며 정렬한다.
    if self.size() > 0:
      self.data[1], self.data[-1] = self.data[-1], self.data[1]
      result = self.data.pop(-1)
      self.minHeapify(1)
    else:
      result = None
    return result

  def minHeapify(self, here):
    # here[부모노드]과 자식노드들의 키를 비교하며 정렬
    left = here*2
    right = here*2+1
    min_ = here

    if left <= self.size() and self.data[min_] > self.data[left]:
      min_ = left
    if right <= self.size() and self.data[min_] > self.data[right]:
      min_ = right

    if min_ != here:
      self.data[here], self.data[min_] = self.data[min_], self.data[here]
      self.minHeapify(min_)

  def size(self):
    # 노드의 수 (0번째 제외)
    return len(self.data)-1

heap = minHeap()
