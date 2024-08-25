
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, RedirectResponse
from uvicorn import run as app_run

from typing import Optional

from us_visa.constants import APP_HOST, APP_PORT
from us_visa.pipline.prediction_pipeline import USvisaData, USvisaClassifier
from us_visa.pipline.training_pipeline import TrainPipeline

app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")

# templates = Jinja2Templates(directory='templates')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# class DataForm:
#     def __init__(self, request: Request):
#         self.request: Request = request
#         self.continent: Optional[str] = None
#         self.education_of_employee: Optional[str] = None
#         self.has_job_experience: Optional[str] = None
#         self.requires_job_training: Optional[str] = None
#         self.no_of_employees: Optional[str] = None
#         self.company_age: Optional[str] = None
#         self.region_of_employment: Optional[str] = None
#         self.prevailing_wage: Optional[str] = None
#         self.unit_of_wage: Optional[str] = None
#         self.full_time_position: Optional[str] = None
        

#     async def get_usvisa_data(self):
#         form = await self.request.form()
#         self.continent = form.get("continent")
#         self.education_of_employee = form.get("education_of_employee")
#         self.has_job_experience = form.get("has_job_experience")
#         self.requires_job_training = form.get("requires_job_training")
#         self.no_of_employees = form.get("no_of_employees")
#         self.company_age = form.get("company_age")
#         self.region_of_employment = form.get("region_of_employment")
#         self.prevailing_wage = form.get("prevailing_wage")
#         self.unit_of_wage = form.get("unit_of_wage")
#         self.full_time_position = form.get("full_time_position")

@app.get("/", tags=["authentication"])
async def index(request: Request):
    return RedirectResponse(url="/docs")

@app.get("/ping")
async def ping():
    return {"status": "healthy"}


@app.get("/train")
async def trainRouteClient():
    try:
        train_pipeline = TrainPipeline()

        train_pipeline.run_pipeline()

        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")


@app.post("/invocations")
async def predictRouteClient(request: Request):
    try:
        input_data = await request.json()

        usvisa_data = USvisaData(
            continent=input_data.get("continent"),
            education_of_employee=input_data.get("education_of_employee"),
            has_job_experience=input_data.get("has_job_experience"),
            requires_job_training=input_data.get("requires_job_training"),
            no_of_employees=input_data.get("no_of_employees"),
            company_age=input_data.get("company_age"),
            region_of_employment=input_data.get("region_of_employment"),
            prevailing_wage=input_data.get("prevailing_wage"),
            unit_of_wage=input_data.get("unit_of_wage"),
            full_time_position=input_data.get("full_time_position"),
        )
        
        usvisa_df = usvisa_data.get_usvisa_input_data_frame()

        model_predictor = USvisaClassifier()

        value = model_predictor.predict(dataframe=usvisa_df)[0]

        status = None
        if value == 1:
            status = "Visa-approved"
        else:
            status = "Visa Not-Approved"

        status = "Visa-approved" if value == 1 else "Visa Not-Approved"

        # Return the prediction result as a JSON response
        return JSONResponse(content={"status": status, "prediction": value})
        
    except Exception as e:
        return JSONResponse(content={"status": False, "error": str(e)}, status_code=500)
    


if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)