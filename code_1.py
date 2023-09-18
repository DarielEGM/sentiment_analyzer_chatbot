#import the textblob library
from textblob import TextBlob

#The Feeling class returns a string with the name and color values ​​it receives from the "range" duple.
class Feeling:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def __str__(self):
        return "\x1b[1;{}m{}".format(self.color, self.name) + "\x1b[0;37m"
 
   
#Duple of "ranges" with values ​​according to the data returned by the textblob.
ranges = [
    ((0,1),Feeling("Positive", "32")),
    ((-1,-0.1),Feeling("Negative", "31"))
]
        
#Class that, depending on the result obtained by the Textblob and compared with the values ​​of the "ranges" duple, returns a call to the Feeling class with input values.
class FeelingAnalyzer:
    def __init__(self,ranges):
        self.ranges = ranges
       
    def feeling_analyzer(self,text):
        analysis = TextBlob(text)
        for range, feeling in self.ranges:
            if range[0] < analysis.sentiment.polarity <=range[1]:
                return feeling
        return Feeling("Neutral", "37")    
        
        
#Instantiation of the Feeling class       
analyzer = FeelingAnalyzer(ranges)

#Loop to keep chat running indefinitely
while True:
    user_promt = input("\x1b[1;33m" + "\nTell me something: " + "\x1b[0;37m")
    print(f"The text is emotional: {analyzer.feeling_analyzer(user_promt)}")
    
    
    

        
        
