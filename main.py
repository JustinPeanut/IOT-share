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


@app.post('/chat-3')
async def main(request: Request):
    content_type = request.headers.get('Content-Type')
    if content_type is None:
        return 'No Content-Type provided.'
    elif content_type == 'application/json':
        try:
            json = await request.json()
            rq = json['text']
            response = openai.Completion.create(
                engine="davinci",
                prompt=rq,
                max_tokens=1024,
                n=1,
                stop=None,
                # 随机程度，值越高越随机，范围0-2
                temperature=0.1,
            )

            return {"text": response.choices[0].text.strip()}
        except JSONDecodeError:
            return 'Invalid JSON data.'
    else:
        return 'Content-Type not supported.'

@app.post('/chat-turbo')
async def main(request: Request):
    content_type = request.headers.get('Content-Type')
    if content_type is None:
        return 'No Content-Type provided.'
    elif content_type == 'application/json':
        try:
            json = await request.json()
            rq = json['text']
            response = openai.Image.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": rq}
                ]
                 )
            print(response)

            return {"text": response.choices[0].message}
        except JSONDecodeError:
            return 'Invalid JSON data.'
    else:
        return 'Content-Type not supported.'

@app.post('/img-turbo')
async def main(request: Request):
    content_type = request.headers.get('Content-Type')
    if content_type is None:
        return 'No Content-Type provided.'
    elif content_type == 'application/json':
        try:
            json = await request.json()
            num = json['num']
            rq = json['text']
            response = openai.Image.create(
                prompt=rq,
                n=num
                 )
            print(response)

            return {"text": response.data}
        except JSONDecodeError:
            return 'Invalid JSON data.'
    else:
        return 'Content-Type not supported.'