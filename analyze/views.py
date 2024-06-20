from django.shortcuts import render
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from django.middleware import csrf

# Create your views here.

def index(request):
     emoji = {-10:'🤬',-9:'🤬',-8:'😡',-7:'😡',-6:'🤨',-5:'🙄',-4:'😳',-3:'😟',-2:'😟',-1:'😟',0:'😐',
              1:'🙂',2:'😊',3:'😀',4:'😃',5:'😛',6:'😝',7:'😜',8:'😍',9:'😍',10:'🥰'}
     csrf_token = csrf.get_token(request)
     b = 0; text = 'Type something here'
     if request.method == "POST":
          text = request.POST.get('sentence','').strip()
          s=SentimentIntensityAnalyzer()
          b = s.polarity_scores(text)['compound']
     emo = emoji.get(int(b*10),'😐')
     print(int(b*10))
     return render(request, 'analyze/index.html', {'value':emo,'token':csrf_token,'text':text})
