from fastapi import FastAPI
from fastmcp import FastMCP

app = FastAPI()
mcp = FastMCP("PetsMegastore-MCP")

@app.get("/docs")
async def root():
    return app.openapi()

@mcp.tool
def add(a: int, b: int) -> int:
    "Add two numbers"
    return a + b

@app.post("/mcp")
async def handle_mcp(request: dict):
    return await mcp.handle(request)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
