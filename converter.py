from pydantic import BaseModel


class Phone(BaseModel):
    city: str
    country: str
    number: str


class Contacts(BaseModel):
    email: str
    name: str
    phone: Phone


class Coordinates(BaseModel):
    latitude: float
    longitude: float


class Experience(BaseModel):
    id: str


class SalaryRange(BaseModel):
    vars()["from"]: int = 0
    vars()["to"]: int = 0


class Schedule(BaseModel):
    vars()["id"]: str = ""


class Data(BaseModel):
    address: str
    allow_messages: bool
    billing_type: str
    business_area: int
    contacts: Contacts
    coordinates: Coordinates
    description: str
    experience: Experience
    html_tags: bool
    image_url: str
    name: str
    salary: int
    salary_range: SalaryRange
    schedule: Schedule


def converting(data):
    d = {
    "address": data["address"]["value"],
    "allow_messages": True,
    "billing_type": "packageOrSingle",
    "business_area": 1,
    "contacts": {
        "email": data["contacts"]["email"],
        "name": data["contacts"]["fullName"],
        "phone": {
            "city":  data["contacts"]["phone"][-10:-7],
            "country": data["contacts"]["phone"][:-10],
            "number": data["contacts"]["phone"][-7:-4] + "-" + data["contacts"]["phone"][-4:-2] + "-" + data["contacts"]["phone"][-2:]
            }
        },
    "coordinates": {
        "latitude": data["address"]["lat"],
        "longitude": data["address"]["lng"]
        },
    "description": data["description"],
    "experience": {
        "id": "noMatter"
    },
    "html_tags": True,
    "image_url": "https://img.hhcdn.ru/employer-logo/3410666.jpeg",
    "name": data["name"],
    "salary": data["salary"]["to"],
    "salary_range": {
        "from": data["salary"]["from"],
        "to": data["salary"]["to"]
        },
    "schedule": {
        "id": data["employment"]
        }
    }
    return Data(**d)
