# Import fastApi
from fastapi_offline import FastAPIOffline


from fastapi import APIRouter

# This is where api-routes are imported.
#from routes.users import router,heartbeatroute
from routes.users import *
from routes.heartbeat import *


# Create the Application
app = FastAPIOffline(    
    title="FastApi starter template",
    description="",
    summary="A template with everything you need to start with fastapi in a meaningfull way.",
    version="0.0.1",
    )

# Include the routes
app.include_router(users_router)
# optionally add a prefix.
app.include_router(heartbeat_router,prefix="/anotherprefix")



# the default route
@app.get("/")
async def root():    
    return {"message": "Hello World"}
