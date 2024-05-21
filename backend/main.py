from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from backend.utils import generate_path, get_map_data, get_points, process_points

app = FastAPI()
templates = Jinja2Templates(directory="frontend/templates")
app.mount("/static", StaticFiles(directory="frontend/static"), name="frontend_static")

@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    # paths:  dict = generate_path(process_points(), get_map_data())
    # points: dict = get_points()
    # print("paths =",paths)
    # print("points =",points)
    # return templates.TemplateResponse("index.html", {"request": request, "map_data": map_data, "roads": roads})
    paths_data = generate_path(process_points(), get_map_data())
    points_data = get_points()
    return templates.TemplateResponse("index.html", {"request": request, "paths": paths_data, "points": points_data})