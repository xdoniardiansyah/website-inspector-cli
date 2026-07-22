print("=========================")
print("Website Inspector CLI")
print("=========================\n")

clean_input = input("Masukkan URL:\n").strip()
print()

if clean_input == "":
    print(f"URL tidak boleh kosong.")
else:
    print(f"URL :\n{clean_input}")