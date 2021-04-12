# Section 12.2.11 snippets
# NOTE: This section's Self Check snippets are included in this file
# because the self check continues the interactive session.

from pathlib import Path

from textblob import TextBlob

blob = TextBlob(Path('RomeoAndJuliet.txt').read_text())

blob.word_counts['juliet']

blob.word_counts['romeo']

blob.word_counts['thou']

blob.words.count('joy')

blob.noun_phrases.count('lady capulet')


# Section 12.2.11 Self Check snippets

# Exercise 2
blob.word_counts['a']

blob.word_counts['an']

blob.word_counts['the']


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
