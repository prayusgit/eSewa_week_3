from fastapi import FastAPI

from .controllers import transaction, user


app = FastAPI()

app.include_router(transaction.router)
app.include_router(user.router)
