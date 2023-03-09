from json import JSONDecodeError
from fastapi import FastAPI
from fastapi import Request
import openai
import config



app = FastAPI()
openai.api_key = config.API_KEY
proxies = {'http': "127.0.0.1:7890",'https': "127.0.0.1:7890"}
openai.proxy = proxies



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post('/chat')
async def main(request: Request):
    # content_type = request.headers.get('Content-Type')
    # if content_type is None:
    #     return 'No Content-Type provided.'
    # elif content_type == 'application/json':
    #     try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": "Hello!"}
                ]
            )
            print(response.choices[0].message)

    #         return {"text": response.choices[0].message}
    #     except JSONDecodeError:
    #         return 'Invalid JSON data.'
    # else:
    #     return 'Content-Type not supported.'