josephus = []

class Link (object):
  def __init__ (self, data, next=None):
    self.data = data
    self.next = next

class CircularList (object):
  def __init__ (self):
    self.first = None
    self.last = None
    self.rank = 0 

  def insert (self, data):
    current = self.first
    newLink = Link(data)
    if current is None:
        self.first = newLink

    else:
      self.last.next = newLink
      newLink.next = self.first

    self.last = newLink
    self.rank += 1

  def find (self, key):
    current = self.first.next
    while current is not self.first:
      if current.data is key:
        return current
      current = current.next

    return None    

  def isEmpty(self):
    return self.first is None

  def delete (self, key):
    current = self.first
    previous = self.first
    while current.data is not key:
      if current is self.last: 
        return None

      previous = current
      current = current.next

    if current is self.first:
      self.first = current.next
      self.last.next = current.next
      self.rank -= 1
      return key

    if current is self.last:
      self.last = previous
      previous.next = self.first
      self.rank -= 1
      return key
    previous.next = current.next
    current = previous
    self.rank -= 1      
    return key

    return None

  def deleteAfter (self, start, n):
    del josephus[:]

    current = self.first
    while current.next.data is not start:
      current = current.next
      
    while self.rank >= 1:
      count = 0 
      while count is not n:
        current = current.next
        count += 1
      josephus.append(current.data)
      self.delete(current.data)


      
  def __str__ (self):
    l = []
    current = self.first
    count = 0
    while count < self.rank:
      l.append(current.data)
      current = current.next
      count += 1

    return " ".join(str(x) for x in l)


def main():
  
  jose = CircularList()
  for i in range (1, 41):
    jose.insert(i)

  
  jose.deleteAfter(1, 3) 
  print(" ".join(str(x) for x in josephus))
  
  mark = CircularList()
  [mark.insert(x) for x in range (1, 6)]
  mark.deleteAfter(1, 3)    
  print(" ".join(str(x) for x in josephus))

if __name__=='__main__':
  main()     

