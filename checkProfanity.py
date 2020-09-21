import csv
import urllib.request


#Extracting all the bad words from the below site and storing in a list
profane_words=[]
data = urllib.request.urlopen("https://www.cs.cmu.edu/~biglou/resources/bad-words.txt")
for line in data:
    words = line.decode().rstrip('\n')
    profane_words.append(words)


#Read the csv file with all the tweets
def read_file():
    tweets_list = []
    #open csv file
    with open(r'C:\Users\Admin\Desktop\tweets.csv', encoding='utf-8') as tweets_file:
        reader = csv.reader(tweets_file)
        #creating list of dicitionaries
        for row in reader:
            temp_dict = {}
            #creating dicitionary of id as key and content as value
            temp_dict[row[0]] = row[3]
            tweets_list.append(temp_dict)
    #deleting first dict as it's just a heading
    del tweets_list[0]
    check_profanity(tweets_list)


def check_profanity(tweets_list):
    for tweet in tweets_list:
        for id,content in tweet.items():
            #sending the tweet content as list of words
            check_profanity_in_sentence(content.split())


#find the percentage of bad words to length of words in a sentence
def check_profanity_in_sentence(sentence):
    #number of words in sentence
    length = len(sentence)
    count=0
    for word in sentence:
        if word.lower() in profane_words:
            count+=1
    degree = (count*100)/length
    print("Degree of Profanity in this tweet is %f %%"%(round(degree, 2)))

#calling the functions
read_file()
