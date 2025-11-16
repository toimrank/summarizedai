from fastapi import FastAPI, Request, Response, status, HTTPException
from typing import Optional

app = FastAPI()

users =[{
    "id" : 1,
    "name" : "Jack",
    "age" : 23,
    "city" : "Ausitn",
    "password" : "abc123"
}]

sessions = {}

# Get Users,
@app.get("/")
def get_message():
    return {"message" : "This is first FastAPI App !"} 

# Get Users,
@app.get("/hello/{name}")
def get_message(name : str):
    return {"message" : f"name is {name}"} 

# Get Users,
@app.get("/users")
def get_users():
    return users

@app.post("/user")
async def create_user(request : Request, response : Response):
    user = await request.json()
    print(user)
    response.status_code=status.HTTP_201_CREATED
    users.append(user)
    return {
        "received_data" : users    
    } 

@app.get("/user/{user_id}")
async def get_user(user_id : int, response : Response):
    for index , user in enumerate(users):
        if user["id"] == user_id:
            response.status_code = status.HTTP_200_OK
            return users[index] 
        
@app.put("/user/{user_id}")
async def update_user(user_id : int, request : Request, resposne : Response):
    updated_user = await request.json()
    for index , user in enumerate(users):
        if user["id"] == user_id:
            users[index].update(updated_user)
            resposne.status_code = status.HTTP_200_OK
    return {
        "received_data" : users[index]  
    }      

@app.delete("/user/{user_id}")
async def delete_user(user_id : int, request : Request, resposne : Response):
    for index , user in enumerate(users):
        if user["id"] == user_id:
            del users[index]
            resposne.status_code=status.HTTP_204_NO_CONTENT
            return
    raise HTTPException(status_code=404, detail="User not Found")  


@app.post("/login")
async def login(response : Response, request : Request, 
    user_id : str, password : str):
    for user in users:
        if user["id"] == int(user_id) and user["password"] == password:
            session_id = f"{user_id}_session"
            sessions[session_id] = {"username" : user_id}
            print(sessions)
            response.set_cookie(
                key="session_id",
                value=session_id,
                httponly=True,
                max_age=3600
            )
            return {"message" : "Login Successgull"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/profile")
async def profile(request : Request):
    session_id: Optional[str] = request.cookies.get("session_id")
    print(session_id)
    print(sessions)
    if session_id and session_id in sessions:
        return {"message" : f"Welcome {sessions[session_id]["username"]}"}
    else:
        raise HTTPException(status_code=401, detail="Not Authenticated!")
    
@app.post("/logout")
async def logout(response : Response, request : Request):
    session_id: Optional[str] = request.cookies.get("session_id")
    print(f"logout = {sessions}")
    print(f"cookie = {request.cookies}")
    print(f"session ID from request cookie >>>> {session_id}")
    if session_id and session_id in sessions:
        print("Inside if >>>>>>>>>>>>")
        del sessions[session_id]
        print(f"After delete session : {sessions}")
        response.delete_cookie(key="session_id")
        return {
            "message" : "Logout Succefull!"
        }
    else:
        print(">>>>>>>>>>>>>>>>>>>>>")
        raise HTTPException(status_code=401, detail="Not Authenticated")
