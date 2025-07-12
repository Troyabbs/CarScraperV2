from models.car import Car
import re

def inverse_normalisation(value, min_val, max_val):
    return 1 - (value - min_val) / (max_val - min_val)

def calculate_score(car: Car, min_price: int, max_price: int, min_km: int, max_km: int):
    price_number = int(re.sub("[^0-9]", "", car.price))
    km_number = int(re.sub("[^0-9]", "", car.mileage))
    price_score = inverse_normalisation(price_number, min_price, max_price) * 40
    km_score = inverse_normalisation(km_number, min_km, max_km) * 40
    location_score = 20 if "auckland" in car.location.lower() else 0
    return round(price_score + km_score + location_score, 1)