from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return{"message":"steeelflow api is running"}git remote add origin https://github.com/amansharma040406-stack/steelflow.git
git branch -M main
git push -u origin main