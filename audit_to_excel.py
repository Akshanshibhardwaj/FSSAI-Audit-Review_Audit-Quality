import pandas as pd

# Aapka audit data
data = [
    {"Item": 1, "Section": "I - Design", "Status": "C"},
    {"Item": 2, "Section": "I - Design", "Status": "C"},
    {"Item": 3, "Section": "I - Design", "Status": "PC"},
    {"Item": 4, "Section": "I - Design", "Status": "C"},
    {"Item": 5, "Section": "I - Design", "Status": "C"},
    {"Item": 6, "Section": "I - Design", "Status": "PC"},
    {"Item": 7, "Section": "I - Design", "Status": "PC"},
    {"Item": 8, "Section": "I - Design", "Status": "C"},
    {"Item": 9, "Section": "I - Design", "Status": "C"},
    {"Item": 10, "Section": "I - Design", "Status": "C"},
    {"Item": 11, "Section": "I - Design", "Status": "PC"},
    {"Item": 12, "Section": "I - Design", "Status": "PC"},
    {"Item": 13, "Section": "I - Design", "Status": "C"},
    {"Item": 14, "Section": "I - Design", "Status": "C"},
    {"Item": 16, "Section": "II - Handling", "Status": "PC"},
    {"Item": 17, "Section": "II - Handling", "Status": "PC"},
    {"Item": 18, "Section": "II - Handling", "Status": "PC"},
    {"Item": 20, "Section": "II - Handling", "Status": "C"},
    {"Item": 21, "Section": "II - Handling", "Status": "C"},
    {"Item": 22, "Section": "II - Handling", "Status": "PC"},
    {"Item": 29, "Section": "II - Handling", "Status": "PC"},
    {"Item": 30, "Section": "II - Handling", "Status": "PC"},
    {"Item": 34, "Section": "II - Handling", "Status": "PC"},
    {"Item": 36, "Section": "II - Handling", "Status": "PC"},
    {"Item": 37, "Section": "III - Maint", "Status": "PC"},
    {"Item": 40, "Section": "III - Maint", "Status": "NC"},
    {"Item": 41, "Section": "III - Maint", "Status": "C"},
    {"Item": 42, "Section": "III - Maint", "Status": "PC"},
    {"Item": 43, "Section": "III - Maint", "Status": "PC"},
    {"Item": 45, "Section": "IV - Hygiene", "Status": "C"},
    {"Item": 46, "Section": "IV - Hygiene", "Status": "C"},
    {"Item": 47, "Section": "IV - Hygiene", "Status": "C"},
    {"Item": 50, "Section": "V - Training", "Status": "C"},
    {"Item": 51, "Section": "V - Training", "Status": "C"},
]

# 1. Data ko Pandas DataFrame mein convert karein
df = pd.DataFrame(data)

# 2. Excel File mein save karein
df.to_excel("FSSAI_Audit_Sheet.xlsx", index=False)

# 3. CSV File mein save karein
df.to_csv("FSSAI_Audit_Sheet.csv", index=False)

print("Success! Excel aur CSV files generate ho gayi hain.")
