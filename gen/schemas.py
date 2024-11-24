from pydantic import BaseModel
from typing import List, Dict


# class TextGenerationRequest(BaseModel):
#     prompt: str
#     max_length: int = 50
#     num_return_sequences: int = 1

class TextGenerationResponse(BaseModel):
    generated_texts: Dict[str, List[str]]
    
class TextGenerationRequest(BaseModel):
    prompt: str
    max_length: int = 200
    num_return_sequences: int = 1
    temperature: float = 1.0
    top_p: float = 0.9
    top_k: int = 50
