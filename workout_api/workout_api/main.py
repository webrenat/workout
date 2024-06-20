from fastapi import FastAPI
# from routers import api_router
from workout_api.routers import api_router

app = FastAPI(title='WorkoutAPI')
app.include_router(api_router)