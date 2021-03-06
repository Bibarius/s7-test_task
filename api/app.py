from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schemas import SkiRequest
from utils import book_ski
from aiohttp import ClientConnectionError
import uvicorn

app = FastAPI()

@app.exception_handler(KeyError)
@app.exception_handler(ClientConnectionError)
async def booking_service_error(request, exception):
    return JSONResponse(
        status_code=200,
        content={
            "error": {
                "code": "conversation.not.found",
                "message": "Давайте начнем новый поиск и обновим результаты.",
            },
            "shoppingCart": None,
        }
    )


@app.post("/add_ski_to_reservation")
async def transporting_ski_request(request: SkiRequest):
    return await book_ski(request)


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
