
from fastapi import FastAPI
from langchain.evaluation import load_evaluator
from langchain_community.embeddings import HuggingFaceEmbeddings
from pydantic import BaseModel




app = FastAPI()

class answers(BaseModel):
    student_ans: str
    reference_ans: str

embedding_model = HuggingFaceEmbeddings()
evaluator = load_evaluator("embedding_distance", embeddings=embedding_model)

@app.post("/")
async def similarity_endpoint(item:answers):
    pre = item['student_ans']
    ref = item['reference_ans']
    result = evaluator.evaluate_strings(prediction="g", reference="g")
    print(result)

    return {"result":result}






