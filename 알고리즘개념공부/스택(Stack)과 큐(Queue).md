* 스택(Stack)
  * 입력과 출력을 한 방향으로 제어하는 알고리즘, 데이터를 쌓아 놓는 자료 구조
  * 배열, 노드 -> 작업이 복잡함
  * 데이터를 올릴 때 - Push, 데이터를 뺄 때 - Pop
  * LIFO(Last In First Out) 방식
  
  ```py
  def push(item):
      stack.append(item)
   
  def pop():
      return stack.pop()
  
  if __name__ == '__main__':
      stack = []
      push(1)
      push(2)
      
      print("현재 스택: ")
      print(stack)
      
      while stack:
          print("POP > {}".format(pop()))
          
  ```
  * 시간의 효율성 - 검색할 필요 없이 가장 위에 있는 데이터를 가져오고 넣음 -> 배열과 비슷한 효율
  * 공간의 효율성 - 크기를 정해놓고 사용 -> 비슷한 효율

* 큐(Queue)
 * FIFO(First In First Out) - 처음으로 저장한 데이터를 사용
 * 배열을 사용하여 만드는 것이 편리함
 ```py
 def put(item):
     queue.append(item)

 def get():
     return queue.pop()
 
 if __name__ == '__main__':
     queue = []
     
     put(1)
     put(2)
     
     print("현재 queue: ")
     print(queue)
     
     while queue:
       print("POP > {}".format(get()))
 ```
 * 시간의 효율성 - 스택과 같이 검색 과정이 필요 없음
 * 공간의 호율성 - 스택과는 다르게 원형 큐 형태로 사용함 -> 배열 크기와는 상관없이 돌면서 사용이 가능
