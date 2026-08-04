from faker import Faker
import pandas as pd
import random

fake = Faker("en_IN")

customers = []

occupations = [
    "Software Engineer",
    "Teacher",
    "Doctor",
    "Student",
    "Business",
    "Accountant",
    "Sales Executive",
    "Farmer",
    "Lawyer",
    "Data Analyst"
]

risk_categories = ["Low", "Medium", "High"]

for customer_id in range(1, 5001):

    customers.append({
        "customer_id": customer_id,
        "full_name": fake.name(),
        "gender": random.choice(["Male", "Female"]),
        "age": random.randint(18, 70),
        "city": fake.city(),
        "state": fake.state(),
        "occupation": random.choice(occupations),
        "annual_income": random.randint(200000, 2500000),
        "joining_date": fake.date_between(start_date="-10y", end_date="today"),
        "risk_category": random.choices(
            risk_categories,
            weights=[70, 20, 10]
        )[0]
    })

df = pd.DataFrame(customers)

from pathlib import Path

output_folder = Path(__file__).parent.parent / "datasets"
output_folder.mkdir(exist_ok=True)

df.to_csv(output_folder / "customers.csv", index=False)

print("Customers dataset created successfully!")