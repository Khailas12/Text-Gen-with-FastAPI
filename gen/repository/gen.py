from fastapi import HTTPException
from transformers import pipeline, set_seed
from gen import schemas
import asyncio
import re


# Initialize Hugging Face pipelines for multiple models
models = {
    "gpt2": pipeline("text-generation", model="gpt2"),
    "distilgpt2": pipeline("text-generation", model="distilgpt2")
}
set_seed(42)  # For reproducibility


async def async_gen_text(request: schemas.TextGenerationRequest):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, gen_text, request) # handle multiple requests concurrently

def gen_text(request: schemas.TextGenerationRequest):
    try:
        # Validate the prompt
        prompt = request.prompt.strip()
        if not prompt:
            raise HTTPException(status_code=400, detail="Prompt cannot be empty or just whitespace.")

        # Default values for optional parameters
        temperature = request.temperature or 1.0
        top_p = request.top_p or 0.9
        top_k = request.top_k or 50
        max_length = request.max_length or 100
        num_return_sequences = request.num_return_sequences or 1

        responses = {}

        # Iterate over the models and generate responses
        for model_name, generator in models.items():
            try:
                # Generate text for each model
                results = generator(
                    prompt,
                    max_length=max_length,
                    num_return_sequences=num_return_sequences,
                    temperature=temperature,
                    top_p=top_p,
                    top_k=top_k,
                    truncation=True  # Explicit truncation to handle long input
                )

                # Process results and sanitize text
                sanitized_texts = [
                    re.sub(r'\n+', ' ', result["generated_text"][len(prompt):].strip())
                    for result in results
                ]

                responses[model_name] = sanitized_texts

            except Exception as e:
                responses[model_name] = [f"Error generating text: {str(e)}"]
        return schemas.TextGenerationResponse(generated_texts=responses)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in text generation: {str(e)}")



# def gen_text(request: schemas.TextGenerationRequest):
#     try:
#         # Ensure the prompt is not empty
#         if not request.prompt.strip():
#             raise HTTPException(status_code=400, detail="Prompt cannot be empty or just whitespace.")

#         # Generate text using the selected models
#         responses = {}
        
#         for model_name, generator in models.items():
#             # Generate text for each model
#             results = generator(
#                 request.prompt,
#                 max_length=request.max_length,  
#                 num_return_sequences=request.num_return_sequences
#             )
            
#             # Sanitize the response to exclude the prompt in result
#             sanitized_texts = [
#                 result["generated_text"][len(request.prompt):].strip()
#                 for result in results
#             ]
            
#             # Add each model's output to the response dictionary
#             responses[model_name] = sanitized_texts
#         return schemas.TextGenerationResponse(generated_texts=responses)

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))



