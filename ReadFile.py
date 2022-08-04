def Read(file):
  sequencia = False
  countSeq = 0
  
  with open(file) as f:
    line = f.readline()
    line = line. rstrip('\n')
    countDown = int(line)
    
    while True:
        
      pertence = True
      line = f.readline()
      line = line.rstrip('\n')

      if not line or countDown == 0:
        break

      for char in line:
        if char == 'a' or char == 'b':
          if char == 'a' and not sequencia:
            sequencia = True
          elif char == 'b' and sequencia:
            if countSeq < 1:
              countSeq = 1
            else:
              sequencia = False
              countSeq = 0            
              
          elif char != 'b':
            pertence = False
            print(line + ': não pertence')
            break
          
        else:
          pertence = False
          print(line + ': não pertence')
          break     
          
      countDown -= 1

      if pertence:
        print(line + ': pertence')
