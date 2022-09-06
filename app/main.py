# Convention
# !all main Modules or Folders are UpperCamel Case like Routers, Analysis
# !all sub module or folder named are lower camel Case and after submodule name Add Parent Module name in Big letter like fixitAnalysis, hmbrAnalysis, fixitRoute etc
# !all files name should be snake cased and add parent branch name after underscore  like transport_hmbr_route, 

from typing import Optional, Union
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Body
from random import randrange
import time
from v1.Routers.hmbrRoute import hmbr_main_route 

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
CORSMiddleware,
allow_origins=["*"], # Allows all origins
allow_credentials=True,
allow_methods=["*"], # Allows all methods
allow_headers=["*"], # Allows all headers
)

app.include_router(hmbr_main_route.router)

