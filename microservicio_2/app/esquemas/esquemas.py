from pydantic import BaseModel, ConfigDict


class CancionBase(BaseModel):
    titulo: str
    minutos: int
    segundos: int
    interprete: str
    puntajes: list[float]


class CancionSchema(CancionBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
