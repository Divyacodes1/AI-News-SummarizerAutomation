import requests
from send_email import sendemail
from langchain.chat_models import init_chat_model

api_key="10d20731793b462884d747656b8ca8c9"
Google_api_key="AIzaSyDzvcxHLblRDk_adGCgTu1GAHwarTUZK4Y"
url=("https://newsapi.org/v2//top-headlines?"
"category=business&language=en&pagesize=8&sortBy=publishedAt&apiKey="+api_key)
#make a request
r=requests.get(url)
#Get a dictionary
content=r.json()# to make the content dictionary we used "json"
articles=content["articles"]
#AI summarizing the news
model=init_chat_model(model="gemini-2.5-flash",model_provider="google-genai",api_key=Google_api_key)
prompt=f"""
You're a news summarizer
Write a short paragraph analysing those news .Add another paragraph to
tell  me how they affect the stock market.
Here are the news articles:
{articles}
"""
response=model.invoke(prompt)
response_str=response.content

body="Subject:News Summary\n\n"+response_str+"\n\n"

body=body.encode("utf-8")
sendemail(message=body)
