from pydantic import BaseModel, ConfigDict


class CancionSchema(BaseModel):
    id: int
    titulo: str
    minutos: int
    segundos: int
    interprete: str

    model_config = ConfigDict(from_attributes=True)
