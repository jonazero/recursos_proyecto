from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@app.post('/token')
# form_data depende de OAuth2PasswordRequestForm. Si existe un token, entonces devuelve la informacion a form_data
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access-token': form_data.username + 'token'}


@app.get('/')
async def index(token: str = Depends(oauth2_scheme)):
    return {'the token': token}
 