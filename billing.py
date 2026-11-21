class CustomerProfile:
    def __init__(self, user_id, email, password_hash, city, loyalty_points):
        self.user_id = user_id
        self.email = email
        self.password_hash = password_hash
        self.city = city
        self.loyalty_points = loyalty_points


# Усунуто Stamp Coupling: приймаємо лише рядок city та weight_kg замість усього об'єкта CustomerProfile
def calculate_delivery_cost(city: str, weight_kg: float) -> float:
    base_rate = 50.0 if city == "Ivano-Frankivsk" else 110.0
    return base_rate + (weight_kg * 12.0)


# Усунуто Common Coupling (tax_rate передається як параметр) та Control Coupling (окрема функція замість mode_flag)
def process_standard_invoice(amount: float, city: str, weight_kg: float, tax_rate: float = 0.20) -> dict:
    delivery = calculate_delivery_cost(city, weight_kg)
    total = (amount * (1 + tax_rate)) + delivery
    return {"status": "PROCESSED", "total": round(total, 2)}


# Окрема функція для замовлень без податку (без мутації глобального стану)
def process_tax_exempt_invoice(amount: float, city: str, weight_kg: float) -> dict:
    delivery = calculate_delivery_cost(city, weight_kg)
    total = amount + delivery
    return {"status": "TAX_EXEMPT", "total": round(total, 2)}
