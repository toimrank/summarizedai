from fastapi import FastAPI, Request, Response, status, HTTPException
from typing import Optional, List, Annotated
from pydantic import BaseModel, Field # type: ignore

app = FastAPI()

class User(BaseModel):
    id : int
    name: Annotated[str, Field(pattern=r'^[A-Za-z]+$', description="Only Letters allowed", min_length=1)]
    age :int = Field(..., gt=0, description="Age must be greater than zero!")
    city : str
    password : str


users: List[User] = [
    User(id=1, name="jack", age=23, city="Austin", password="abc123")
]

sessions = {}

# Get Users,
@app.get("/")
def get_message():
    return {"message" : "This is first FastAPI App !"} 

# Get Users,
@app.get("/users")
def get_users():
    return users

@app.post("/user")
async def create_user(user : User, response : Response):
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
async def update_user(user_id : int, updated_user : User, resposne : Response):
    for index , user in enumerate(users):
        if user.id == user_id:
            update_data = updated_user.dict(exclude_unset=True)
            print(updated_user)
            for key, value in update_data.items():
                setattr(users[index], key, value)
                print(users)
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
    if session_id and session_id in sessions:
        del sessions[session_id]
        response.delete_cookie(key="session_id")
        return {
            "message" : "Logout Succefull!"
        }
    else:
        HTTPException(status_code=401, detail="Not Authenticated")