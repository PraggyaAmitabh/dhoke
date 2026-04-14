from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Dhoke API is live 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}
#from fastapi import FastAPI imports the FastAPI class from the package you installed.

#app = FastAPI() creates the application object that Uvicorn will run.

#@app.get("/") creates a route for the root URL, so when the browser hits /, that function returns JSON.

#@app.get("/health") gives you a second route often used to confirm the API is alive.