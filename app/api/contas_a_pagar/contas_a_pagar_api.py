from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.drivers.database import get_db_session

router = APIRouter(prefix='/conta-a-pagar-api', tags=['Contas à pagar'])


@router.get('/listar', summary='Listar as contas que precisam ser pagas')
def listar_contas(db_session: Session = Depends(get_db_session)):
    
    return {'message', 'funcionou endpoint'}