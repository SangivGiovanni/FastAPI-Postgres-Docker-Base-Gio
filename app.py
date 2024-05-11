from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import db.models as models
from db.database import SessionLocal, engine
from sqlalchemy.orm import Session


app = FastAPI()

# Mount the 'static' folder as a static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# templates object to be called when returning html
templates = Jinja2Templates(directory="templates")

# Establish a connection to the PostgreSQL database
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse, name="home")
async def homepage(request:Request):
    page = "Home"
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "page": page,
        }
    )


@app.get("/about", response_class=HTMLResponse, name="about")
async def about(request:Request):
    page = "About"
    return templates.TemplateResponse(
        "about.html",
        {
            "request": request,
            "page": page
        }
    )


@app.get("/insights", response_class=HTMLResponse, name="insights")
async def insights(request:Request, db: Session = Depends(get_db)):
    page = "Insights"
    blogs = db.query(models.Blogs).all()
    return templates.TemplateResponse(
        "insights.html",
        {
            "request": request,
            "page": page,
            "blogs": blogs
        }
    )


@app.get("/services", response_class=HTMLResponse, name="services")
async def services(request:Request):
    page = "Services"
    return templates.TemplateResponse(
        "services.html",
        {
            "request": request,
            "page": page
        }
    )


@app.get("{blog_title}", response_class=HTMLResponse, name="blog")
async def blog(request:Request, blog_title: str, db: Session = Depends(get_db)):
    db_record = db.query(models.Blogs).filter(models.Blogs.title == blog_title).first()
    title = db_record.title
    blog = db_record.content
    return templates.TemplateResponse(
        "blog.html", {
            "request": request,
            "title": title,
            "blog": blog,
        }
    )
