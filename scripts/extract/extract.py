from typing import Any
import json
import requests
import os

ENVIRONMENT = "development"  # development, staging, production
ROOT = os.getcwd()  # hansard/scripts/extract

debates_data: dict = {}

if __name__ == "__main__":
    if "data" not in os.listdir(os.getcwd()):
        os.mkdir("data")
    os.chdir(ROOT + "/data")
    if "raw" not in os.listdir():
        os.mkdir("raw")
    os.chdir(ROOT + "/data/raw")
    if "debates" not in os.listdir():
        os.mkdir("debates")
    if "search" not in os.listdir():
        os.mkdir("search")
    os.chdir(ROOT + "/data/raw/search")
    if "debates" not in os.listdir():
        os.mkdir("debates")
    os.chdir(ROOT)
    search_debates_url = "https://hansard-api.parliament.uk/search/debates.json"
    search_params = {
        "house": "commons",
        "searchTerm": "",
        "startDate": "2025-11-15",
        "endDate": "2026-11-15",
        "orderBy": "SittingDateDesc",
    }
    for search_term in ["prison", "probation", "courts", "sentencing", "Justice"]:
        search_params["searchTerm"] = search_term
    debates_url = "https://hansard-api.parliament.uk/debates/debate/"
    if ENVIRONMENT == "development":
        response_test = r"""{"Results":[{"DebateSection":"Commons Chamber","SittingDate":"2026-11-10T00:00:00","House":"Commons","Title":"Prisons: Rehabilitative Programmes","Rank":160,"DebateSectionExtId":"DEAEF138-3C36-4401-8113-BE62A760A307"},{"DebateSection":"Commons Chamber","SittingDate":"2026-05-19T00:00:00","House":"Commons","Title":"Open Prisons: Policy on Convicted Paedophiles","Rank":160,"DebateSectionExtId":"70D0F80C-CA19-47A0-94C0-2348ACE03921"},{"DebateSection":"Commons Chamber","SittingDate":"2026-01-15T00:00:00","House":"Commons","Title":" Prisons: Illegal Drugs","Rank":160,"DebateSectionExtId":"93674DB8-309F-49D9-A2E7-5CB07A0E37FD"},{"DebateSection":"Commons Chamber","SittingDate":"2025-12-16T00:00:00","House":"Commons","Title":"Open Prisons: Rehabilitation Placements","Rank":160,"DebateSectionExtId":"83AE844D-2B1A-44B8-B7B1-204243F71D2C"},{"DebateSection":"Commons Chamber","SittingDate":"2025-11-20T00:00:00","House":"Commons","Title":" Reoffending: Rehabilitation in Prisons","Rank":160,"DebateSectionExtId":"107EB1EB-B422-4DA2-A373-2E08271BD820"}],"TotalResultCount":5}"""
        debates_data = json.loads(response_test)
    else:
        response = requests.get(search_debates_url, search_params)
        debates_data = json.loads(response.text)
    debate_section_external_ids = []
    results = debates_data["Results"]
    for result in results:
        path = ROOT + "/data/raw/debates/" + result["DebateSectionExtId"] + ".json"
        if not os.path.exists(path):
            with open(path, "a") as f:
                f.write(json.dumps(result))
