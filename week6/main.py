from fastapi import FastAPI, Form, Request, Depends
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
import mysql.connector

db = mysql.connector.connect(user='root', password='abcd1234',
                              host='127.0.0.1',
                              database='website')
cursor = db.cursor()

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

@app.post("/signup")
async def post_signup(request: Request, name: Annotated[str, Form()] = None, username: Annotated[str, Form()] = None, password: Annotated[str, Form()] = None):
    new_name = name
    new_username = username
    new_password = password

    query = ("SELECT * FROM member "
             "where username = %s")
    cursor.execute(query, (new_username,))
    result = cursor.fetchall()

    if result:
        error_message = "此帳號已被使用"
        redirect_url = request.url_for("get_error").include_query_params(message=error_message)
        return RedirectResponse(redirect_url, status_code=302)
    else:
        add_new_member = ("INSERT INTO member "
            "(name, username, password) "
            "VALUES (%s, %s, %s)")

        new_member_data = (new_name, new_username, new_password)
        
        cursor.execute(add_new_member, new_member_data)

        db.commit()

        return RedirectResponse(url="/", status_code=302)

@app.post("/signin")
async def post_signin(request: Request, username: Annotated[str, Form()] = None, password: Annotated[str, Form()] = None, session: dict = Depends(get_session)):
    signin_username = username
    signin_password = password

    query = ("SELECT id, name, username, password FROM member")
    cursor.execute(query)
    result = cursor.fetchall()

    for (member_id, name, username, password) in result:
        if signin_username == username and signin_password == password:
            session["member_id"] = member_id
            session["username"] = username
            session["name"] = name

            redirect_url = request.url_for("get_member")
            return RedirectResponse(redirect_url, status_code=302)
    
    error_message = "帳號或密碼輸入錯誤"
    redirect_url = request.url_for("get_error").include_query_params(message=error_message)
    return RedirectResponse(redirect_url, status_code=302)

@app.get("/member")
async def get_member(request: Request, session: dict = Depends(get_session)):
    if session == {}:
        return RedirectResponse(url="/", status_code=302)
    
    display_name = session["name"]
    
    message_query = ("SELECT member.name, message.content FROM message "
                     "join member on message.member_id = member.id "
                     "order by message.time desc "
                     "limit 5")
    cursor.execute(message_query)
    result = cursor.fetchall()

    return templates.TemplateResponse("success.html", {"request": request, "name": display_name, "result": result})

@app.post("/createMessage")
async def post_message(request: Request, message: Annotated[str, Form()] = None, session: dict = Depends(get_session)):
    member_id = session["member_id"]
    
    if message is not None:
        add_new_message = ("INSERT INTO message "
            "(member_id, content) "
            "VALUES (%s, %s)")
        
        new_message_data = (member_id, message)
        
        cursor.execute(add_new_message, new_message_data)

        db.commit()
    
    redirect_url = request.url_for("get_member")
    return RedirectResponse(redirect_url, status_code=302)

@app.get("/signout")
async def get_signout(session: dict = Depends(get_session)):
    session.clear()
    return RedirectResponse(url="/", status_code=302)

@app.get("/error")
async def get_error(request: Request, message: str):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})