from dataclasses import dataclass, field

@dataclass
class Car:
    title: str
    location: str
    mileage: str
    price: str
    url: str
    score: float = field(default=0.0)
    