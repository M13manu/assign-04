# sentiment analysis in a text
# concept: dictionaries and files

'''
You will be given a comment in a file.

Your task is to count the number of positives and number of negatives and return sentiment of the comment.

In the below code you will be given a function sentiment_analysis(filename) where filename is the text file containing the content

Your task is to analyse the positive and negative words and deside what is the sentiment and return it.

Three types of sentiments:
positive, negative, neutral

For positive comment
  #positives should be greater than #negative
  And the different (positive - negative) should be greated than 2 other wise it is neutral.

For negative comment
  #negative should be greater than #positives
  And the difference (negative - positive) should be greater than 2 other wise it is neutral.

For neutral comment
  #positive and #negative should be equal or differ by a count of 1 or 2.

A dictionary with positive and negative words are given in the program.


'''

import unittest

def sentiment_analysis(filename):
  sentiment_words = {"positive":["good","excellent","happy","positive","respect","respectful","respected","nice","constructive"], "negative": ["bad","worse","worsening","worsened","disrespect","ugly","down","vulnerability","vulnerable","disastrous","destructive"]}

  # Delete the bellow line and write your implementation
  c=0
  d=0
  f=open(filename,'r')
  x=f.read()
  y=x.split()
  for i in sentiment_words['positive']:
    for j in y:
      if i==j:
        c+=1
  for i in sentiment_words['negative']:
    for j in y:
      if i==j:
        d+=1
  f.close()
  if c>d and (c-d)>2:
    return 'positive comment'
  elif d>c and (d-c)>2:
    return 'negative comment'
  else:
    return 'neutral comment'


# don't touch the code bellow

class Unit_test(unittest.TestCase):
  def test_01(self):

    self.assertEqual(sentiment_analysis("college1.txt"), "positive comment")
  def test_02(self):
    self.assertEqual(sentiment_analysis("college2.txt"), "negative comment")

  def test_03(self):
    self.assertEqual(sentiment_analysis("college3.txt"), "neutral comment")

  def test_04(self):
    self.assertEqual(sentiment_analysis("news_article.txt"), "neutral comment")

if __name__ == '__main__':
  unittest.main(verbosity=2)
