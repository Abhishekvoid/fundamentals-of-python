from fastapi import FastAPI, HTTPException, Depends
from models import Container, YardZone, ContainerStatus
from service import YardManagementService
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Container Yard Management API")
service = YardManagementService()

class CreateContainerRequest(BaseModel):
    container_number: str
    shipping_line: str
    yard_zone: str
    row: str
    stack_level: int

@app.post("/containers/", response_model=Container)
async def create_container(request: CreateContainerRequest):
    try:
        return await service.create_container(
            request.container_number,
            request.shipping_line,
            request.yard_zone,
            request.row,
            request.stack_level
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/containers/{container_id}", response_model=Container)
async def get_container(container_id: str):
    container = await service.container_repo.get(container_id)
    if not container:
        raise HTTPException(status_code=404, detail="Container not found")
    return container

@app.post("/containers/{container_id}/move")
async def move_container(
    container_id: str,
    new_zone: str,
    new_row: str,
    new_stack: int
):
    try:
        return await service.move_container(container_id, new_zone, new_row, new_stack)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/zones/{zone_code}/utilization")
async def get_zone_utilization(zone_code: str):
    return await service.get_zone_utilization(zone_code)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
