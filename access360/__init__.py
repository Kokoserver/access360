from fastapi import FastAPI
from mongoengine import connect, disconnect
from access360.settings import DEBUG

from access360.view import AccountView

app = FastAPI(title="Access360 Api",
              description="Access3060 is an e-learning for people with disabilities",
              debug=DEBUG
              )


@app.on_event("startup")
def Init_database():
    print("database connected successfully")
    connect(db="access360", alias="core")


@app.on_event("shutdown")
def Un_init_database():
    print("database disconnected successfully")
    disconnect()


app.include_router(AccountView.router)

