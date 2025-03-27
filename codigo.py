from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
import jwt

# Configuração do banco de dados
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelo de conta corrente
class ContaCorrente(Base):
    __tablename__ = 'contas_correntes'
    id = Column(Integer, primary_key=True, index=True)
    titular = Column(String, index=True)
    saldo = Column(Float, default=0.0)

# Configuração do FastAPI
app = FastAPI()

# Pydantic models
class ContaCorrenteModel(BaseModel):
    titular: str
    saldo: float

class Operacao(BaseModel):
    valor: float

# Configuração de autenticação JWT
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token", headers={"WWW-Authenticate": "Bearer"})

# Dependência do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criar tabela
Base.metadata.create_all(bind=engine)

# Rotas de autenticação
@app.post("/token")
async def login():
    user_data = {"sub": "usuario1"}
    access_token = create_access_token(data=user_data)
    return {"access_token": access_token, "token_type": "bearer"}

# Função para obter conta corrente
def get_conta_corrente(db, conta_id: int):
    return db.query(ContaCorrente).filter(ContaCorrente.id == conta_id).first()

# Rotas de operações bancárias
@app.post("/depositar/{conta_id}")
async def depositar(conta_id: int, operacao: Operacao, db: Depends(get_db), token: str = Depends(oauth2_scheme)):
    verify_token(token)
    conta = get_conta_corrente(db, conta_id)
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    conta.saldo += operacao.valor
    db.commit()
    db.refresh(conta)
    return {"message": f"Depósito de {operacao.valor} realizado com sucesso.", "saldo": conta.saldo}

@app.post("/sacar/{conta_id}")
async def sacar(conta_id: int, operacao: Operacao, db: Depends(get_db), token: str = Depends(oauth2_scheme)):
    verify_token(token)
    conta = get_conta_corrente(db, conta_id)
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    if conta.saldo < operacao.valor:
        raise HTTPException(status_code=400, detail="Saldo insuficiente")
    conta.saldo -= operacao.valor
    db.commit()
    db.refresh(conta)
    return {"message": f"Saque de {operacao.valor} realizado com sucesso.", "saldo": conta.saldo}
