def search_patients_by_disease(patients, disease):
    result = [patient["Name"] for patient in patients if patient["Disease"].lower() == disease.lower()]
    return result

# Example input
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]

search_disease = "Flu"

# Operation
matched_patients = search_patients_by_disease(patients, search_disease)

# Output
print(f"Patients with {search_disease}: {matched_patients}")
