import requests

print("=========================")
print("Website Inspector CLI")
print("=========================\n")

target_url = input("Masukkan URL:\n").strip()
print()

if target_url == "":
    print(f"URL tidak boleh kosong.")
else:
    response = requests.get(target_url)
    print(f"Status Code :\n{response.status_code}")