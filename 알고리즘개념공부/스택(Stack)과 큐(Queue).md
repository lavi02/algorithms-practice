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
