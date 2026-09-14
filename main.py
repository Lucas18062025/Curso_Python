@app.get("/")
def root():
    ...

@app.get("/")   # ← esto rompe, ruta duplicada
def root():
    ...

@app.get("/estado_actual")
def estado_actual():
    ...
