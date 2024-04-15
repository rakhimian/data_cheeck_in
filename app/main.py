from fastapi import FastAPI
from .models import user as user_model
from . import database
from .routes import auth, user

user_model.Base.metadata.create_all(bind=database.engine)

summary = """
API для DataCheeckIn. 🚀
"""

description = """
В этой версии реализовано Аутентификация, работа с Демками и Шагами.
"""

app = FastAPI(
    title="DataCheeckIn",
    summary=summary,
    description=description,
    version="0.0.1",
    # terms_of_service="http://example.com/terms/",
    contact={
        "name": "Рахимян Тимерханов",
        # "url": "http://x-force.example.com/contact/",
        "email": "timerkhanov.ri@phystech.edu",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

app.include_router(auth.router)
app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "Welcome to DataCheeckIn"}
