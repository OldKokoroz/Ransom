
import os

filter_path = input("\nPath to filter files : ")

os.chdir(filter_path)

for file in os.listdir():
    if file == '.DS_Store':
        continue

    name, ext = os.path.splitext(file)

    filtered = name.split("-")
    filtered = [s.strip() for s in filtered]

    end_name = f"{filtered[2]}-{filtered[1]}-{filtered[0]}{ext}"
    os.rename(file, end_name)
