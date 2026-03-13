from langchain.chat_models import init_chat_model
Google_api_key="AIzaSyDzvcxHLblRDk_adGCgTu1GAHwarTUZK4Y"
model=init_chat_model(
    model="gemini-2.5-flash",  #This model returns list and gemini 2.0 returns string directly
    model_provider="google-genai",
    api_key=Google_api_key)
response=model.invoke("Hi!")
response_str=(response.content[0]['text'])
print(response_str)