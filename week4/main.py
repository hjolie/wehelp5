from fastapi import FastAPI, Form, Request, Depends
from typing import Optional
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

SECRET_KEY = "user_key"
SESSION_COOKIE = "user_id"

app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY, session_cookie=SESSION_COOKIE)

def get_session(request: Request):
    return request.session

@app.get("/")
async def welcome(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/signin")
async def post_signin(username: Optional[str] = Form(None), password: Optional[str] = Form(None), session: dict = Depends(get_session)):
    if username == None or password == None:
        error_message = "請輸入帳號和密碼"
        return RedirectResponse(url=f"/error?message={error_message}", status_code=302)
    
    if username == "test" and password == "test":
        session["username"] = username
        session["password"] = password
        session["signed-in"] = True
        return RedirectResponse(url="/member", status_code=302)
    else:
        error_message = "帳號或密碼輸入錯誤"
        return RedirectResponse(url=f"/error?message={error_message}", status_code=302)

@app.get("/member")
async def get_member(request: Request, session: dict = Depends(get_session)):
    if session["signed-in"] == False:
        return RedirectResponse(url="/", status_code=302)
    return templates.TemplateResponse("success.html", {"request": request})

@app.get("/signout")
async def get_signout(session: dict = Depends(get_session)):
    session["signed-in"] = False
    return RedirectResponse(url="/", status_code=302)

@app.get("/error")
async def error(request: Request, message: str = None):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})
