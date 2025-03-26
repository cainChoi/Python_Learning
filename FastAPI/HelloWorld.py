from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}   


#해당 파일 폴더로 이동 혹은 실행시 기본이 되는 py 파일 위치를 잡아서 실행함
#실행하는 코드
#uvicorn HelloWorld:app --reload