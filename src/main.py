from fastapi import FastAPI
import django
from django.contrib.auth import get_user_model
from django.core.serializers.python import Serializer

django.setup()
app = FastAPI()

@app.get("/")
def root():
    users = get_user_model().objects.all()
    return Serializer().serialize(users, fields=('email','username'))

