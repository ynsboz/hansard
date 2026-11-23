from datetime import datetime
from typing import Annotated
from pydantic import AfterValidator, BaseModel, Field, NaiveDatetime, validator
import json, sys, os

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
    held_date: NaiveDatetime = Field(alias="Date")
    updated_at: NaiveDatetime = Field(alias="ContentLastUpdated")


class Contribution(BaseModel):
    id: int = Field(alias="ItemId")
    member_id: int | None = Field(alias="MemberId")
    member_name: str | None = Field(alias="AttributedTo")
    contribution: str = Field(alias="Value")
    started_at: NaiveDatetime | None = Field(alias="Timecode")
    external_id: str = Field("ExternalId")


# ChildDebates e.g. DAF51343-D1FD-423F-90F8-D413B08478FE has child debates

ROOT = os.getcwd()  # hansard/scripts/extract
child_debates = []
for external_id in os.listdir(ROOT + "/data/debates/debate/"):
    debate_json = open(ROOT + "/data/debates/debate/" + external_id)
    debate_dict = json.load(debate_json)
    debate_dict["parent_debate"] = None
    debate = Debate(**debate_dict["Overview"])
    for contribution_dict in debate_dict["Items"]:
        if contribution_dict["ItemType"] == "Contribution":
            contribution = Contribution(**contribution_dict)
            print(contribution)
    level_1 = debate_dict["ChildDebates"]
    level_2 = []
    while child_debates != []:
        for child in level_1["ChildDebates"]:
            child["parent_debate"] = debate.id
            debate = Debate(**child["Overview"])
            if child["ChildDebates"] != []:
                level_2 = child["ChildDebates"]

    # contribution = Contribution()
    # child_debates = debate_dict["ChildDebates"]
    # for child_debate in debate_dict["ChildDebates"]:
    #     print(child_debate)
