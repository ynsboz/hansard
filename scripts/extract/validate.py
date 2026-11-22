from datetime import datetime
from typing import Annotated
from pydantic import AfterValidator, BaseModel, Field, NaiveDatetime
import json, sys

x = r"""{"first_name":"Al","last_name":"Capone","age":48,"city":"Chicago"}"""
# print(x)
y = json.loads(x)
# print(type(y))
# print(y)


class Familia(BaseModel):
    first_name: str
    last_name: str
    age: int = Field(gt=0)
    city: str


f = Familia.model_construct(**y)
# print(type(Familia))
# print(Familia.model_dump_json(f))
x = r"""{"first_name":"Al","last_name":"Capone","age":-1,"city":"Chicago"}"""
# v = Familia.model_validate_json(x)
# print(type(v))
# print(v)


class Debate(BaseModel):
    id: int = Field(alias="Id")
    external_id: str = Field(alias="ExtId")
    title: str = Field(alias="Title")
    location: str = Field(alias="Location")
    held_date: NaiveDatetime = Field(alias="ContentLastUpdated")
    updated_at: NaiveDatetime = Field(alias="ContentLastUpdated")
    # child_debates: str  # e.g. DAF51343-D1FD-423F-90F8-D413B08478FE has child debates


class Contribution(BaseModel):
    id: int = Field(alias="ItemType")
    member_id: str = Field(alias="MemberId")
    member_name: str = Field(alias="AttributedTo")
    contribution: str = Field(alias="Value")
    started_at: NaiveDatetime | None = Field(alias="Timecode")
    external_id: str = Field("ExternalId")


r = open("data/debates/debate/DAF51343-D1FD-423F-90F8-D413B08478FE.json")
j = json.load(r)

d = Debate(**j["Overview"])
print(d)
