import requests
import json


if __name__ == "__main__":
    allDebatesUrl = "https://hansard-api.parliament.uk/search/debates.json"
    searchParams = {
        "house": "commons",
        "searchTerm": "",
        "startDate": "2025-11-15",
        "endDate": "2026-11-15",
        "orderBy": "SittingDateDesc",
    }
    for searchTerm in ["prison", "probation", "courts", "sentencing", "Justice"]:
        searchParams["searchTerm"] = searchTerm
        print(searchParams)
    # debatesResponse = requests.get(allDebatesUrl, params)
    # print(debatesResponse.text)
    debateSectionUrl = "https://hansard-api.parliament.uk/debates/debate/"
    debatesResponseRawJson = r"""{"Results":[{"DebateSection":"Commons Chamber","SittingDate":"2026-11-10T00:00:00","House":"Commons","Title":"Prisons: Rehabilitative Programmes","Rank":160,"DebateSectionExtId":"DEAEF138-3C36-4401-8113-BE62A760A307"},{"DebateSection":"Commons Chamber","SittingDate":"2026-05-19T00:00:00","House":"Commons","Title":"Open Prisons: Policy on Convicted Paedophiles","Rank":160,"DebateSectionExtId":"70D0F80C-CA19-47A0-94C0-2348ACE03921"},{"DebateSection":"Commons Chamber","SittingDate":"2026-01-15T00:00:00","House":"Commons","Title":" Prisons: Illegal Drugs","Rank":160,"DebateSectionExtId":"93674DB8-309F-49D9-A2E7-5CB07A0E37FD"},{"DebateSection":"Commons Chamber","SittingDate":"2025-12-16T00:00:00","House":"Commons","Title":"Open Prisons: Rehabilitation Placements","Rank":160,"DebateSectionExtId":"83AE844D-2B1A-44B8-B7B1-204243F71D2C"},{"DebateSection":"Commons Chamber","SittingDate":"2025-11-20T00:00:00","House":"Commons","Title":" Reoffending: Rehabilitation in Prisons","Rank":160,"DebateSectionExtId":"107EB1EB-B422-4DA2-A373-2E08271BD820"}],"TotalResultCount":5}"""
    debatesResponse = json.loads(debatesResponseRawJson)

    debateSectionExternalIds = []
    for result in debatesResponse["Results"]:
        print(result["DebateSectionExtId"])
