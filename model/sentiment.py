from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

def sentimentCheck(string):
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(string)
    result = "Neutral"
    neutralCheck1 = score["neu"] - score["neg"]
    neutralCheck2 = score["neu"] - score["pos"]
    if score["neu"] > score["pos"] and score["neu"] > score["neg"] and neutralCheck1 >= 0.16 and neutralCheck2 >= 0.16 and score["neg"] < 0.42 and score["pos"] < 0.42:
        result = "Neutral"
    elif score["neg"] > score["pos"] and neutralCheck1 <= 0.16:
        result = "Negative"
    elif score["pos"] > score["neg"] and neutralCheck2 <= 0.16:
        result = "Positive"
    else:
        result = "Neutral"
    #print(score)
    return result

#result = sentimentCheck("neutral")
#print(result)

import dill as pickle
with open('sentiment.pkl', 'wb') as file:
    pickle.dump(sentimentCheck, file)