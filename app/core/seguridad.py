from datetime import datetime, timedelta, timezone
from http import HTTPStatus

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET_KEY = "secreto-cambiar-en-produccion"
ALGORITHM = "HS256"
EXPIRACION_MINUTOS = 30

security = HTTPBearer()


def crear_token(usuario_id: int) -> str:
    expira = datetime.now(timezone.utc) + timedelta(minutes=EXPIRACION_MINUTOS)
    datos = {"sub": str(usuario_id), "exp": expira}
    return jwt.encode(datos, SECRET_KEY, algorithm=ALGORITHM)


def verificar_token(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> int:
    try:
        payload = jwt.decode(
            credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM]
        )
        return int(payload["sub"])
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail="Token expirado"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail="Token inválido"
        )
