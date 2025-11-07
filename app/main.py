from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.contas_a_pagar import contas_a_pagar_api

# produção e homologação
app = FastAPI(docs_url=None, redoc_url=None)

# dev
# app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contas_a_pagar_api.router)
