from fastapi import FastAPI
from app.api.forecast import router as forecast_router
from app.api.resource_planner import (router as planner_router,)
from app.api.feedback import (router as feedback_router,)
from app.api.coefficients import (router as coefficient_router,)

app = FastAPI(title="Restaurant Resource Planning System")

app.include_router(forecast_router)
app.include_router(planner_router)
app.include_router(feedback_router)
app.include_router(coefficient_router)

@app.get("/")
def health():
    return {
        "service": "Restaurant Resource Planning System",
        "status": "healthy"
    }