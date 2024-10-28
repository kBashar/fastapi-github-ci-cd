from fastapi import FastAPI

app = FastAPI()

get_name_description = """

### Parameters

no parameter

"""


@app.get(
        "/",
        summary="Returns a name",
        description=get_name_description
)
async def get_name():
    return {"name": "Jubayer"}
