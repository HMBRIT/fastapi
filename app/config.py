from ast import Pass
import os
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy import create_engine

######### FIXIT DEVELOPMENT SERVER ######
FIXIT_DEVELOPMENT_SERVER = os.getenv('FIXIT_ENGINE_DEVELOPMENT')
FIXIT_DEVELOPMENT_SERVER = create_engine(FIXIT_DEVELOPMENT_SERVER)

######### FIXIT PRODUCTION SERVER ######
FIXIT_PRODUCTION_SERVER = os.getenv('FIXIT_ENGINE_PRODUCTION')
FIXIT_PRODUCTION_SERVER = create_engine(FIXIT_PRODUCTION_SERVER)


############## HMBR DEVELOPMENT SERVER ###########
HMBR_DEVELOPMENT_SERVER = os.getenv('HMBR_ENGINE_DEVELOPMENT')
HMBR_DEVELOPMENT_SERVER = create_engine(HMBR_DEVELOPMENT_SERVER)

######### HMBR PRODUCTION SERVER ######
HMBR_PRODUCTION_SERVER = os.getenv('HMBR_ENGINE_PRODUCTION')
HMBR_PRODUCTION_SERVER = create_engine(HMBR_PRODUCTION_SERVER)


FIXIT_ID = os.getenv('FIXIT_ID')
CENTRAL_ID = os.getenv('CENTRAL_ID')
ECOMMERCE_ID = os.getenv('ECOMMERCE_ID')

HMBR_ID = os.getenv('HMBR_ID')
KARIGOR_ID = os.getenv('KARIGOR_ID')
CHEMICAL_ID = os.getenv('CHEMICAL_ID')
THREADTAPE_ID = os.getenv('THREADTAPE_ID')
PLASTIC_ID = os.getenv('PLASTIC_ID')
ZEPTO_ID = os.getenv('ZEPTO_ID')
GROCERY_ID = os.getenv('GROCERY_ID')
PAINTROLLER_ID = os.getenv('PAINTROLLER_ID')
SCRUBBER_ID = os.getenv('SCRUBBER_ID')
PACKAGING_ID = os.getenv('PACKAGING_ID')

######### EMAIL ID #######
IT_MAIL = os.getenv('IT')
DIRECTOR_MAIL = os.getenv('DIRECTOR')
MOTIUR_MAIL =os.getenv('MOTIUR')
ADMIN_MAIL = os.getenv('ADMIN')
CENTRAL_MAIL = os.getenv('CENTRAL')
PYTHON_MAIL = os.getenv('PYTHON')
############# python password ########
PYTHON_PASS = os.getenv('PYTHON_PASS')
