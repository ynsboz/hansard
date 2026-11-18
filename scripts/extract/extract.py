from typing import Any
import json
import requests
import os
import sys

ENVIRONMENT = "prod"  # test, prod
ROOT = os.getcwd()  # hansard/scripts/extract
debates_data_test = r"""{
  "Overview": {
    "Id": 5439086,
    "ExtId": "DEAEF138-3C36-4401-8113-BE62A760A307",
    "Title": "Prisons: Rehabilitative Programmes",
    "HRSTag": "hs_8Question",
    "Date": "2026-11-10T00:00:00",
    "Location": "Commons Chamber",
    "House": "Commons",
    "Source": 2,
    "VolumeNo": 793,
    "ContentLastUpdated": "2026-11-17T22:50:29.373",
    "DebateTypeId": 1,
    "SectionType": 1,
    "NextDebateExtId": "86E30977-1F17-4A5F-8CD7-F505C648E6B5",
    "NextDebateTitle": "Sexual Offending by Healthcare Professionals",
    "PreviousDebateExtId": "63FBEA79-DE34-48DE-A8E8-321B93F19143",
    "PreviousDebateTitle": "House of Commons"
  },
  "Navigator": [
    {
      "Id": 5439082,
      "Title": "Commons Chamber",
      "ParentId": null,
      "SortOrder": 1,
      "ExternalId": "e69e0fb9-be24-4d0a-a725-fbe7aae9ca95",
      "HRSTag": null,
      "HansardSection": null,
      "Timecode": null
    },
    {
      "Id": 5439084,
      "Title": "Oral Answers to Questions",
      "ParentId": 5439082,
      "SortOrder": 3,
      "ExternalId": "542A4B76-2856-4395-8C35-34BB4D0995DF",
      "HRSTag": "hs_3OralAnswers",
      "HansardSection": "AA-AD",
      "Timecode": null
    },
    {
      "Id": 5439085,
      "Title": "Justice",
      "ParentId": 5439084,
      "SortOrder": 4,
      "ExternalId": "0F858DBA-5B26-4B14-A27E-5C9A9740892B",
      "HRSTag": "hs_6bDepartment",
      "HansardSection": "AA-AD",
      "Timecode": null
    },
    {
      "Id": 5439086,
      "Title": "Prisons: Rehabilitative Programmes",
      "ParentId": 5439085,
      "SortOrder": 5,
      "ExternalId": "DEAEF138-3C36-4401-8113-BE62A760A307",
      "HRSTag": "hs_8Question",
      "HansardSection": "AA-AD",
      "Timecode": null
    }
  ],
  "Items": [
    {
      "ItemType": "Contribution",
      "ItemId": 51042819,
      "MemberId": 5336,
      "AttributedTo": "Helen Maguire (Epsom and Ewell) (LD)",
      "Value": "<Question HRSContentId=\"{B62A8301-C8E0-4C8D-B7AD-8CCA6163E4D2}\">1.  <QuestionText HRSContentId=\"{D6A4688D-135E-41BB-AB1B-0484881F3CAB}\">What steps he is taking to improve rehabilitative programmes in prisons. </QuestionText></Question>",
      "OrderInSection": 1,
      "Timecode": null,
      "ExternalId": "B62A8301-C8E0-4C8D-B7AD-8CCA6163E4D2",
      "HRSTag": "Question",
      "HansardSection": "AA-AD",
      "UIN": "901902",
      "IsReiteration": false
    },
    {
      "ItemType": "Contribution",
      "ItemId": 51042820,
      "MemberId": 4641,
      "AttributedTo": "The Lord Chancellor and Secretary of State for Justice (Alex Norris)",
      "Value": "Education, skills and work are central to rehabilitation. We are modernising prison education and creating a joined-up system that supports prisoners in progressing from basic literacy to skills training and work experience. We are also tackling the root causes of offending through offender behaviour programmes and substance misuse treatment.",
      "OrderInSection": 2,
      "Timecode": "2026-11-10T14:34:41",
      "ExternalId": "683576E6-AB4D-4CFB-B0E7-69E014E74DD7",
      "HRSTag": "hs_Para",
      "HansardSection": "AA-AD",
      "UIN": null,
      "IsReiteration": false
    },
    {
      "ItemType": "Contribution",
      "ItemId": 51042821,
      "MemberId": 5336,
      "AttributedTo": "Helen Maguire",
      "Value": "Many ex-prisoners experience challenges after prison, particularly when trying to reintegrate into society, which is really difficult to do. We know that 40% of prisoners reoffend within one year, and that reoffending costs £22.7 billion per year; at the same time, 97% of prison capacity is taken. Will the Secretary of State ensure that ex-prisoners are properly supported, so that they can positively integrate into society, and reoffending can be reduced?",
      "OrderInSection": 3,
      "Timecode": null,
      "ExternalId": "3896FA13-E6D7-4E2F-B7B3-A27C3BAE7B82",
      "HRSTag": "hs_Para",
      "HansardSection": "AA-AD",
      "UIN": null,
      "IsReiteration": false
    },
    {
      "ItemType": "Contribution",
      "ItemId": 51042822,
      "MemberId": 4641,
      "AttributedTo": "Alex Norris",
      "Value": "That is an important point. It is great to start Question Time on a note of unanimity, and I am sure that one view that we all hold in common in this place is that when people leave prison, we do not want them to return and reoffend. The key to that is a multi-agency approach locally, starting before individuals leave prison. We are working closely with local government partners to ensure more effective pre-release planning work.",
      "OrderInSection": 4,
      "Timecode": null,
      "ExternalId": "AE27C9DF-D869-48E4-9A76-349A9E06AF9C",
      "HRSTag": "hs_Para",
      "HansardSection": "AA-AD",
      "UIN": null,
      "IsReiteration": false
    },
    {
      "ItemType": "Contribution",
      "ItemId": 51042823,
      "MemberId": 467,
      "AttributedTo": "Mr Speaker",
      "Value": "I call the Chair of the Justice Committee.",
      "OrderInSection": 5,
      "Timecode": "2026-11-10T14:35:35",
      "ExternalId": "4DC78F06-95EB-4861-A0AB-EC3D95E85CA8",
      "HRSTag": "hs_Para",
      "HansardSection": "AA-AD",
      "UIN": null,
      "IsReiteration": false
    },
    {
      "ItemType": "Contribution",
      "ItemId": 51042824,
      "MemberId": 5143,
      "AttributedTo": "Catherine Atkinson (Derby North) (Lab)",
      "Value": "The public are safer when people leave prisons with the skills to find work and stay out of crime. Despite the Coates review calling for education to be put\r\n\r\n“at the heart of the prison regime”,\r\n\r\na decade later, cuts have halved the number of education hours in some of our prisons. Today, Ofsted and the chief inspector of prisons have both published a letter calling on Ministers to act on the review’s recommendations, and to tackle poor performance on purposeful activity in prisons. What is being done to ensure that prisoners receive the education that they need to find work and stay out of prison?",
      "OrderInSection": 6,
      "Timecode": "2026-11-10T14:35:54",
      "ExternalId": "38F1EAFD-2C78-4943-9768-22E0E69D3ACB",
      "HRSTag": "hs_Para",
      "HansardSection": "AA-AD",
      "UIN": null,
      "IsReiteration": false
    },
    {
      "ItemType": "Contribution",
      "ItemId": 51042825,
      "MemberId": 4641,
      "AttributedTo": "Alex Norris",
      "Value": "I am grateful for that question from the Chair of the Justice Committee, because that too is a crucial point. We are in a self-defeating cycle: the capacity problems in our prisons, which have been talked about in this Chamber for months, impair governors’ ability to move individuals around and get them to the right place, be it to substance abuse treatment, mental health <span id=\"3\" class=\"column-number\" data-column-number=\"3\"></span>treatment, educational classes or work training. That is why the steps that we have taken are so important. However, I recognise the vigour with which the Chair and the Committee make their comments, and I certainly intend to work closely with them to deliver on this.",
      "OrderInSection": 7,
      "Timecode": null,
      "ExternalId": "58BBA354-DC4D-4AD1-AE95-7854E995838B",
      "HRSTag": "hs_Para",
      "HansardSection": "AA-AD",
      "UIN": null,
      "IsReiteration": false
    },
    {
      "ItemType": "Contribution",
      "ItemId": 51042826,
      "MemberId": 4521,
      "AttributedTo": "Liz Saville Roberts (Dwyfor Meirionnydd) (PC)",
      "Value": "Diolch yn fawr iawn, Lefarydd. Tackling reoffending requires rehabilitation, but the Wales Governance Centre’s latest report shows that that is not happening well enough in Wales. Recall numbers are up 27%; rough sleeping on release is becoming the norm; and the rate of death by drug poisoning while under community supervision is considerably higher than in England. Addressing those issues requires a holistic approach, which is impossible when Westminster controls the levers when it comes to justice. Following the Secretary of State’s meeting with Welsh Government Ministers yesterday, does he agree that devolving justice is key to making justice work in Wales?",
      "OrderInSection": 8,
      "Timecode": "2026-11-10T14:37:24",
      "ExternalId": "9C175E52-2ABA-45A1-B0CC-A71A96E5B446",
      "HRSTag": "hs_Para",
      "HansardSection": "AA-AD",
      "UIN": null,
      "IsReiteration": false
    },
    {
      "ItemType": "Contribution",
      "ItemId": 51042827,
      "MemberId": 4641,
      "AttributedTo": "Alex Norris",
      "Value": "As the right hon. Lady says, I was in Wales yesterday, meeting the Welsh Government and talking about exactly these issues. As I said in my answer to the original question, we have to use all organisations—yes, His Majesty’s Prison and Probation Service, but also others, including local authorities, local health services and charities—effectively at a place-based level. That is what we said in the conversations that we had yesterday, and I very much look forward to building on them.",
      "OrderInSection": 9,
      "Timecode": "2026-11-10T14:37:51",
      "ExternalId": "6119D54B-383D-4FED-9C61-3327E39E8C92",
      "HRSTag": "hs_Para",
      "HansardSection": "AA-AD",
      "UIN": null,
      "IsReiteration": false
    },
    {
      "ItemType": "Contribution",
      "ItemId": 51042828,
      "MemberId": 5044,
      "AttributedTo": "Adam Thompson (Erewash) (Lab)",
      "Value": "I welcome the Government focusing prisons on rehabilitation, and on better education, training and support to help people turn their life around. I am particularly concerned about pregnant women leaving prison, many of whom have no secure accommodation, are vulnerable to being targeted by drug dealers and could even feel safer in prison than on the outside. How can we provide better support for pregnant women leaving prison?",
      "OrderInSection": 10,
      "Timecode": "2026-11-10T14:38:20",
      "ExternalId": "92386498-A6C3-4624-A615-633BC2CAA616",
      "HRSTag": "hs_Para",
      "HansardSection": "AA-AD",
      "UIN": null,
      "IsReiteration": false
    },
    {
      "ItemType": "Contribution",
      "ItemId": 51042829,
      "MemberId": 4641,
      "AttributedTo": "Alex Norris",
      "Value": "My hon. Friend touches on an important question for his community and the country more generally. For anybody—particularly pregnant women—to leave prison with security, they must have access to housing; that is the anchor. We are taking incredible steps forward in this place to ensure that everybody is offered somewhere to be from night one, and through our emergency accommodation, we can offer up to 84 days of support. There is much to do, particularly with pregnant women, to make sure that the other support systems then wrap around them, to give them the best possible chance of staying out of prison.",
      "OrderInSection": 11,
      "Timecode": null,
      "ExternalId": "B254B45A-C654-44BF-9D57-E93AEA64B097",
      "HRSTag": "hs_Para",
      "HansardSection": "AA-AD",
      "UIN": null,
      "IsReiteration": false
    }
  ],
  "ChildDebates": []
}"""

if __name__ == "__main__":
    if "data" not in os.listdir(os.getcwd()):
        os.mkdir("data")
    os.chdir(ROOT + "/data")
    if "debates" not in os.listdir():
        os.mkdir("debates")
    os.chdir(ROOT + "/data/debates")
    if "debate" not in os.listdir():
        os.mkdir("debate")
    os.chdir(ROOT + "/data")
    if "search" not in os.listdir():
        os.mkdir("search")
    os.chdir(ROOT + "/data/search")
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
    debates_data: dict = {}
    debate_section_ext_ids: list = []
    if ENVIRONMENT == "prod":
        for search_term in ["prison", "probation", "courts", "sentencing", "Justice"]:
            search_params["searchTerm"] = search_term
            response = requests.get(search_debates_url, search_params)
            debates_data = json.loads(response.text)
            results = debates_data["Results"]
            for result in results:
                debate_section_ext_ids.append(result["DebateSectionExtId"])
                path = (
                    ROOT
                    + "/data/search/debates/"
                    + result["DebateSectionExtId"]
                    + ".json"
                )
                if not os.path.exists(path):
                    with open(path, "a") as f:
                        f.write(json.dumps(result))
    else:
        response_test = r"""{"Results":[{"DebateSection":"Commons Chamber","SittingDate":"2026-11-10T00:00:00","House":"Commons","Title":"Prisons: Rehabilitative Programmes","Rank":160,"DebateSectionExtId":"DEAEF138-3C36-4401-8113-BE62A760A307"},{"DebateSection":"Commons Chamber","SittingDate":"2026-05-19T00:00:00","House":"Commons","Title":"Open Prisons: Policy on Convicted Paedophiles","Rank":160,"DebateSectionExtId":"70D0F80C-CA19-47A0-94C0-2348ACE03921"},{"DebateSection":"Commons Chamber","SittingDate":"2026-01-15T00:00:00","House":"Commons","Title":" Prisons: Illegal Drugs","Rank":160,"DebateSectionExtId":"93674DB8-309F-49D9-A2E7-5CB07A0E37FD"},{"DebateSection":"Commons Chamber","SittingDate":"2025-12-16T00:00:00","House":"Commons","Title":"Open Prisons: Rehabilitation Placements","Rank":160,"DebateSectionExtId":"83AE844D-2B1A-44B8-B7B1-204243F71D2C"},{"DebateSection":"Commons Chamber","SittingDate":"2025-11-20T00:00:00","House":"Commons","Title":" Reoffending: Rehabilitation in Prisons","Rank":160,"DebateSectionExtId":"107EB1EB-B422-4DA2-A373-2E08271BD820"}],"TotalResultCount":5}"""
        debates_data = json.loads(response_test)
        results = debates_data["Results"]
        for result in results:
            debate_section_ext_ids.append(result["DebateSectionExtId"])
            path = (
                ROOT + "/data/search/debates/" + result["DebateSectionExtId"] + ".json"
            )
            if not os.path.exists(path):
                with open(path, "a") as f:
                    f.write(json.dumps(result))
    debates_debate_url = "https://hansard-api.parliament.uk/debates/debate/"
    if ENVIRONMENT == "prod":
        for debate_section_ext_id in debate_section_ext_ids:
            response = requests.get(
                debates_debate_url + debate_section_ext_id + ".json"
            )
            debates_data = json.loads(response.text)
            path = ROOT + "/data/debates/debate/" + debate_section_ext_id + ".json"
            if not os.path.exists(path):
                with open(path, "a") as f:
                    f.write(json.dumps(debates_data))
    else:
        debates_data = json.loads(debates_data_test)
        path = ROOT + "/data/debates/debate/DEAEF138-3C36-4401-8113-BE62A760A307.json"
        if not os.path.exists(path):
            with open(path, "a") as f:
                f.write(json.dumps(debates_data))
