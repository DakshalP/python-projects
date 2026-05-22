'''
    Decoder Encoder
    - A fun project coded when learning python
    -Run the program and type 'encode' and enter a message to convert into a code.
     You can then decode the message by typing 'decode'
'''

numCode = "7 2 6 9 16 8 26 3 23 18 12 15 24 20 4 25 5 10 13 14 17 22 1 21 19 11 a b c d e f g h i j k"


wordCode = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0 1 2 3 4 4 6 7 8 9 ."

numCode = numCode.split()
wordCode = wordCode.split()
punctuation = " , ! ? ; : # ' ( ) [ ] &".split()

def useCode():

  intro = 'null'
  
  wordInput = "Error"
  codeInput = "Error"

  outputBar = ""
  
  while intro != 'DECODE' and intro != 'D' and intro != 'ENCODE' and intro != 'E':
    intro = str.upper(input("\nWould you like to decode or encode: "))
    
  if intro == "ENCODE" or intro == "E":
    wordInput = str.upper(input("\n   Please input your text: "))
  elif intro == "DECODE" or intro == "D":
    codeInput = input("\n   Please input your code: ")
  else:
    print('Error')
  
  
  
  
  codeOutput = ['.'] * len(wordInput)
  for index in range(len(codeOutput)):
    codeOutput[index] = wordInput[index]
    
  #change split character here (and one time below)
  wordOutput = codeInput.split('.')
  
  
  
  decoderKey = {'_':' '}
  encoderKey = {' ':'_'}
  
  for index in range(len(numCode)):
    decoderKey[numCode[index]] = wordCode[index]
  for index in range(len(numCode)):
    encoderKey[wordCode[index]] = numCode[index]
  
  for mark in punctuation:
    decoderKey[mark] = mark
    encoderKey[mark] = mark
  
  
  for index in range(len(codeOutput)):
    codeOutput[index] = encoderKey.get(codeOutput[index], '�')
    outputBar += "--"

  
  for index in range(len(wordOutput)):
    wordOutput[index] = decoderKey.get(wordOutput[index], '�')
    outputBar += "--"
  
  # adds a bar to format what is returned
  if len(outputBar) >= 82:
    outputBar = "----------------------------------------------------------------------------------"
  elif len(outputBar) <= 13:
    outputBar = "-------------"

  #returns values
  print("\n" + outputBar)
  if intro == "DECODE" or intro == "D":
    print("The message is:")
    print(str.upper(''.join(wordOutput)))
  elif intro == "ENCODE" or intro == "E":
    print("Your code is:")
    #change this to change split character (and one time above)
    print('.'.join(codeOutput))
  #¦
  #⠂
  print(outputBar + "\n")
  useCode()

useCode()