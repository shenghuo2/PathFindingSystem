from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from backend.utils import generate_path, generate_sublists, get_map_data, get_points, process_map_points, process_points
from backend.finding import get_relations, get_shortest_path
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
    paths_data = generate_path(process_map_points(), get_map_data())
    points_data = get_points()
    return templates.TemplateResponse("index.html", 
                                      {
                                        "request": request, 
                                        "paths": paths_data, 
                                        "points": points_data
                                       }
                                      )
class selectedPoints(BaseModel):
    selectedPoints:  list


@app.post('/finding', response_class=HTMLResponse)
async def finding(request: Request, data: selectedPoints):
    startPoint, endPoint = data.selectedPoints[0], data.selectedPoints[1]
    path: dict[str, list[str]] = get_relations()
    points = get_points()
    shortest_path, distance = get_shortest_path(startPoint, endPoint, path, points)
    result = generate_path(generate_sublists(shortest_path), get_map_data())
    return JSONResponse(content=result)
