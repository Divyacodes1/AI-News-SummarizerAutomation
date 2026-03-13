import requests
from send_email import sendmail
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os


load_dotenv()


NEWS_API_KEY=os.getenv("NEWS_API_KEY")

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
url=("https://newsapi.org/v2//top-headlines?"
"category=business&language=en&pagesize=8&sortBy=publishedAt&apiKey="+NEWS_API_KEY)
#make a request
r=requests.get(url)
#Get a dictionary
content=r.json()# to make the content dictionary we used "json"
articles=content["articles"]
#AI summarizing the news
model=init_chat_model(model="gemini-2.5-flash",model_provider="google-genai",api_key=GOOGLE_API_KEY)
prompt=f"""
You need to summarize the news in two paragraphs where second paragraph consists
 of the news that how it affect the stock market
Here are the news articles:
{articles}
"""
response=model.invoke(prompt)
response_str=response.content

body="Subject:News Summary\n\n"+response_str+"\n\n"

#body.encode("utf-8")
sendmail(message=body)
