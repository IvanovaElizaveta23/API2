from pydantic import BaseModel


class Bird(BaseModel):
    class_number: str
    class_name: str
