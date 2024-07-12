from fastapi import FastAPI, HTTPException

# Crear una instancia de FastAPI
app = FastAPI()

# Lista de tareas simulada
tasks = [
    {"id": 1, "description": "Hacer la compra", "completed": False},
    {"id": 2, "description": "Pagar las facturas", "completed": False},
]

@app.get("/")
def read_root():
    return {"message": "Bienvenido al API del listado de tareas"}

# Endpoint para obtener todas las tareas
@app.get("/tasks")
async def read_tasks():
    return tasks

# Endpoint para obtener una tarea por su ID
@app.get("/tasks/{task_id}")
async def read_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# Endpoint para crear una nueva tarea
@app.post("/tasks")
async def create_task(description: str):
    new_task = {"id": len(tasks) + 1, "description": description, "completed": False}
    tasks.append(new_task)
    return new_task

# Endpoint para marcar una tarea como completada
@app.put("/tasks/{task_id}")
async def complete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return task
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# Endpoint para eliminar una tarea
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            return tasks.pop(index)
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
