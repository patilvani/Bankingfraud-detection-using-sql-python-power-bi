import mysql.connector

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vanisai@6630",
    database="bankingfraud"
)

cursor = conn.cursor()

locations = [
    ("Hyderabad", "Telangana", "India"),
    ("Bengaluru", "Karnataka", "India"),
    ("Chennai", "Tamil Nadu", "India"),
    ("Mumbai", "Maharashtra", "India"),
    ("Delhi", "Delhi", "India"),
    ("Pune", "Maharashtra", "India"),
    ("Kolkata", "West Bengal", "India"),
    ("Ahmedabad", "Gujarat", "India"),
    ("Jaipur", "Rajasthan", "India"),
    ("Lucknow", "Uttar Pradesh", "India"),
    ("Visakhapatnam", "Andhra Pradesh", "India"),
    ("Vijayawada", "Andhra Pradesh", "India"),
    ("Coimbatore", "Tamil Nadu", "India"),
    ("Kochi", "Kerala", "India"),
    ("Bhopal", "Madhya Pradesh", "India"),
    ("Nagpur", "Maharashtra", "India"),
    ("Patna", "Bihar", "India"),
    ("Bhubaneswar", "Odisha", "India"),
    ("Surat", "Gujarat", "India"),
    ("Mysuru", "Karnataka", "India")
]

query = """
INSERT INTO locations (city, state, country)
VALUES (%s, %s, %s)
"""

cursor.executemany(query, locations)

conn.commit()

print("20 location records inserted successfully!")

cursor.close()
conn.close()