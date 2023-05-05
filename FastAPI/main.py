from fastapi import FastAPI
from controller.items_controller import router as item_ctrl
from controller.homepage_controller import router as homepage
app = FastAPI()


app.include_router(homepage, tags=["Homepage"])
app.include_router(item_ctrl, tags=["Items"])
