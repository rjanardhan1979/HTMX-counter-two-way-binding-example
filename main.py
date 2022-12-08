from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/index/", response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request, 'n_items': [0,1,2]}
    return templates.TemplateResponse("index.html", context)

#Counter Implementation
@app.get("/change/{btype}", response_class=HTMLResponse)
def change(request: Request, btype:str):
    query_params = list(request.query_params.keys())
    query_param_val = list(request.query_params.values())
    item = query_params[0]
    cval = int(query_param_val[0])
    if btype == 'add':
        htmlvar = "adds.html"
    else:
        htmlvar = "subtracts.html"    
    context = {'request': request, 'cval': cval, 'item': item}   
    return templates.TemplateResponse(htmlvar, context)


# Two way binding implementation
@app.get("/convert/", response_class=HTMLResponse)
def convert(request:Request):
    print(request.query_params)
    query_params = list(request.query_params.keys())
    query_param_val = list(request.query_params.values())    
    if query_param_val[0] == "":
        query_param_val[0] = 0 
    if query_params[0] == 'cm':
        factor = 1./2.54
        id = 'inches'
    else:
        factor = 2.54
        id = 'cm' 
    val = f'{factor*float(query_param_val[0]):.2f}'
    context = {'request': request, 'val': val, 'id': id, 'target': query_params[0]}
    return templates.TemplateResponse("convert.html", context)

    

    
    