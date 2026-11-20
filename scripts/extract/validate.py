from pydantic import BaseModel, Field
import json

x = r"""{"first_name":"Al","last_name":"Capone","age":48,"city":"Chicago"}"""
print(x)
y = json.loads(x)
print(type(y))
print(y)


class Familia(BaseModel):
    first_name: str
    last_name: str
    age: int = Field(gt=0)
    city: str


f = Familia.model_construct(**y)
print(type(Familia))
print(Familia.model_dump_json(f))
x = r"""{"first_name":"Al","last_name":"Capone","age":-1,"city":"Chicago"}"""
v = Familia.model_validate_json(x)
print(type(v))
print(v)
