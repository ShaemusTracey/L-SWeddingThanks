import os
import random
import string
import csv

# --- CONFIG ---
GUEST_CSV = "Guests.csv"       # Input CSV with a column "Name"
OUTPUT_FOLDER = "guests"       # Folder where guest folders will be created
MAPPING_CSV = "guest-links.csv" # Mapping file

# --- Helper to generate random folder names ---
def random_folder_name(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# --- Create output folder if it doesn't exist ---
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# --- Read guest names ---
guest_names = []
with open(GUEST_CSV, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if "Name" in row and row["Name"].strip():
            guest_names.append(row["Name"].strip())

# --- Generate folders and mapping ---
with open(MAPPING_CSV, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Guest Name", "Folder Name"])  # Header

    for guest in guest_names:
        folder_name = random_folder_name()
        guest_folder_path = os.path.join(OUTPUT_FOLDER, folder_name)
        os.makedirs(guest_folder_path, exist_ok=True)
        writer.writerow([guest, folder_name])
        print(f"Created folder for {guest}: {folder_name}")

print("\nAll guest folders generated successfully!")
print(f"Mapping saved in {MAPPING_CSV}")
