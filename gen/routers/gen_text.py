from fastapi import APIRouter, Query
from gen import schemas
from gen.repository import gen

router = APIRouter(
    prefix='/generate-text',
    tags=['Generate Text']
)

@router.post("/", response_model=schemas.TextGenerationResponse)
async def generate(request: schemas.TextGenerationRequest):
    response = await gen.async_gen_text(request)
    return response


# @router.post("/", response_model=schemas.TextGenerationResponse)
# async def generate_text(request: schemas.TextGenerationRequest):
#     return gen.gen_text(request)

