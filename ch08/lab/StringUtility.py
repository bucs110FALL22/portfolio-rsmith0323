class StringUtility:
  def __init__(self, string):
    '''takes string as a parameter and stores it as an instance variable'''
    self.string = string

  def __str__(self):
    '''returns the internal string itself unchanged'''
    return str(self.string)

  def vowels(self):
    '''Counts the number of vowels in the string as a string'''
    count = 0
    vowels = 'AEIOUaeiou'
    for eachChar in self.string: 
      if eachChar in vowels:
        count = count + 1
    if count >= 5:
      return "many"
    else:
      return str(count)
      
  def bothEnds(self):
    '''returns a string made of the first 2 and last 2 chars of the original string'''
    if len(self.string) <= 2:
      return ""
    else:
      return(self.string[:2] + self.string[-2:])

  def fixStart(self):
    '''returns a string where all occurrences of its first char have been changed to '*' but the first char remains the same'''
    if len(self.string) <=1:
      return self.string
    else:
      firstChar = self.string[0]
      string2 = self.string.replace[firstChar]
      string2 = firstChar + string2[1:]
      return string2
      
  def asciiSum(self):
    '''returns an integer that is the sum of all ascii values in the string'''
    sum = 0 
    for eachChar in self.string:
      eachChar = ord(self.string)
      sum = sum + eachChar
    return sum

  def cipher(self):   
    '''returns an encoded string by incrementing all letters by the length of the string'''
    num = len(self.string)
    string2 = ""
    for i in range(len(self.string)):
      char = self.string[i]
      if char.isupper():
        string2 = string2 + chr((ord(letter) + num - 65) % 26 + 65)
      elif letter.islower():
        string2 = string2 + chr(((ord(letter))+ num - 97) % 26 + 97)
      else: 
        string2 = string2 + " "
    return string2