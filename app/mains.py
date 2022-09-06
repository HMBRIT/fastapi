from operator import ne
from typing import Optional, Union
from fastapi import FastAPI, Response, status, HTTPException,Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Body
from fastapi.responses import JSONResponse
from random import randrange
import time
import itemprofit

app = FastAPI()
#hello world
#!6. if given path parameter in not found in route then what will happen? server will response then 
    #! a http error code. [see http status code]. suppose we go to posts/id route and give id parameter which is not in our dictionary or database
    #! so handling this type error we give response to client from a server as route not found error which code is 404
    #! to handle this error code we have to import response module from fastapi and pass as parameter in path operation function (given in @app.get("/posts/{id}"))
    #! instead of hardcoded http status value we should import Status function from fastapi module
    #! BUT USING THIS METHOD IS SO SLOPPY. EVERY TIME WE CHECK THE ERROR AND HARDCODE OUR EXCEPTION WHICH IS NOT GOOD PRACTICE
    # ! SO WE WILL IMPORT HTTTPEXCEPTION FUNCTION FROM FASTAPI MODULE TO AUTOMATE HANDLE EXCEPTION 


#!7. Remember when we create any kind of information using post method we expect server will response us with 201 status 
    #! code which means is created the post
    #! but we see the status code is 200.
    #! which means is ok. This is not right. We should expect the code 201 coz we created a new post
    #! to solve the problem or change the default status code , we pass a another option like status_code = status.[whatever related sataus code] like status.httpstatuscode200
    #! in our decorator function

#!8. to delete using http request we need to @app.delete decorator method with id parameter
    #! create a function find_index_post(id) and return the index number 
    #! then pop out the dictionary from main function. remeber always check the parameter type and give the parameter type in main function
    #! when deleting something server should response with the status code is 204 which means no content. thants meant is deleted
    #! to achive this we pass option status_code in our decorator function
    #! IMPORTANT. WHEN We delete some content we should not return something from our main function.
    #! we just throw the http statuscode 204 with fastapi Response method
    #! thats mean we request to delete an object with specific id parameter and server Response back to us 
    #! that hey your desired id content has been deleted

#!9. sometimes when we request to delete with an id to server which is not found then we should throw an exception to handle that your requested id 
    #! to delete not found
#!10! Update Data. to update something we should use PUT Method. put method need an id in path parameter . 
    # !and in body we take which item should update thats field as raw json format and pass it in decorator.
    # ! the methods looks like 
    #! step one take the id values as parameter
    #! step two put in body which fields should be updated as json format
    #! here we get the data from client we should to verify that those data matching our pydantic Update model schema
    #! Therefore we create a Schema to validate data for updating fields value which is looks like our Post pydantic Schema
    #! but we already have Post Schema so we dont need to create a new schema.
    #! The request comes to update function and check the Post Schema is anything not good then server throw the error 

#! 11 now we have created our fast api
    #!lets create this api as a package. we create a folder called app and make this folder as a package. just create a new py __init__ file in it
    #! now its behave as a package

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:6789",
]

WHITELISTED_IPS = ['123.200.9.110','127.0.0.1']

@app.middleware('http')
async def validate_ip(request: Request, call_next):
    # Get client IP
    ip = str(request.client.host)
    
    # Check if IP is allowed
    if ip not in WHITELISTED_IPS:
        data = {
            'message': f'IP {ip} is not allowed to access this resource.'
        }
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=data)

    # Proceed if IP is allowed
    return await call_next(request)

app.add_middleware(
CORSMiddleware,
allow_origins=["*"], # Allows all origins
allow_credentials=True,
allow_methods=["*"], # Allows all methods
allow_headers=["*"], # Allows all headers
)




class Post(BaseModel):
    title: str
    content: str
    isPublished: bool = True # ! here ispublished a boolean type and default is True
    rating: Optional[int] = None #! here datatype should be integer but not mandatory and degault is None



posts = [
    {'title':'A new Post', 'content': 'my first contend', 'isPublished':True, 'rating':5, 'id':1},
    {'title':'A second Post', 'content': 'my second contend','isPublished':True , 'rating':4,  'id':2},
]



def getpost(id):
    for post in posts: ### iterate over the posts dictionary list
        print (post)
        if post['id'] == id:
            return post # which is a dictionary
        

def find_index_post(id):
    for index, post in enumerate(posts):
        if post['id'] == id:
            return index
#get all posts
@app.get("/posts")
async def get_posts():    
    return{"message": posts}


#############
@app.post("/profit" ,status_code=status.HTTP_200_OK)
async def create_post():
    itemprofit.main()
    return {"data":"success"}


@app.post("/loss" ,status_code=status.HTTP_200_OK)
async def create_loss():
    time.sleep(5)
    return {"dataloss"}

#!reference to no 7 we create an option status_code in our decorator function 
@app.post("/createpost" ,status_code=status.HTTP_201_CREATED)
# here when post request comes here. first its goes to Post Model which is a pydantic model.
# if data is valid then it comes here then 
#  we declare a variable post and set body item to Post 
# then convert json to dictionary in post_dict variable
# add a random id in those dictionary then  append whole dictionary to posts table or dictionary
async def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(5,100000)
    print (post_dict)
    post_dict['title'] = f"{post_dict['title']} {post_dict['id']}"
    posts.append(post_dict)
    return {
        "message" : post_dict
    }


############ id is a path parameter 
############ get a new post using post id

@app.get("/posts/{id}") ########## here take path parameter as id and call the function getpost (id) and return value 
def getOnePost(id: int, response : Response): ######### posts id value and parameter value type must be same type
    postx = getpost(id) 
    print (postx)
    if not postx: ############ if parameter not found in in this route then throw the http status error. See section-6
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message" : f"your searched parameter {id} is not found in this route"} ######## this is hardcoded. we will handle exception like below using Httpexcpetion module
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f"your searched parameter {id} is not found in this route"
            ) ######## here detail is default variable dont change to other variable like message

    return {"post detail" :postx}


#! important... route always seek path and parameter from top to bottom route. so when we call 
#! a route with parameter it iterate from top to bottom route if route matching a parameter then those route will be fired.
#! so we should design our route according to route parameter. here is an  example. above route[posts/id] take parameter as int. so when we call posts/latest it iterate
#! from top to bottom route and match above route and check parameter and then error occured. but it not goes to bottom route.
# @app.get ("posts/latest")
# def getLatestPost ():
#     latestPost = len(posts)-1
#     return {'latestpost': latestPost}

#! Reference to no 8 to delete something using delete http request
@app.delete("/posts/{id}", status_code= status.HTTP_204_NO_CONTENT)
def deletePost(id : int):
    deleteIndex = find_index_post(id)
    #!here referenc to no 9 if id is not found server will trow an exception
    if deleteIndex == None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"your requested id {id} not found to delete"

        )
    posts.pop(deleteIndex)
    # return{"message": f"successfull deleted "} instead of return something the server must Response with status code
    return Response (
        status_code= status.HTTP_204_NO_CONTENT)

    # deleting post
    # find the index of post as per parameter id then pop it
    # to do so we call a function like

#! Reference to No:9 update a field value

@app.put("/posts/{id}")
def updatePost(id : int, updatePost:Post): #! here request come and check the schema 
    print (updatePost)
    #! then we should find the passed id as index and call find_index_post function as post method
    updateIndex = find_index_post(id)
    #! if not found id then throw exception like post method
    if updateIndex == None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"your requested id {id} not found to update"

        )
    #! if id found then take json object and initiate to into updatePost variable then convert it to dictionary
    updatePost = updatePost.dict()
    #! take the id which is pathparametered
    updatePost['id'] = id
    #! then update the posts dictionary list as per index
    posts[updateIndex] = updatePost

    return {"data": updatePost}

    


# @app.post("/createposts")
# # here Body(...) takes all the field item from the post pody which is json object and automaticaly converted in a dict and assined to the payLoad variable.
# async def create_posts(payLoad: dict = Body(...)):
#     print (payLoad)
#     typ = type(payLoad)
#     typ = str(typ)
#     return {
#         "message" : payLoad, "type" : typ
#     }

# @app.get("/transport")
# async def read_root():
#     itemprofit.main()
#     return {
#         "default variable": "message success"
#     }


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

######## go to console and type uvicorn main:app --reload
#! when we move to our main file in app package we start our server
#! just type  uvicorn app.main:app --reload