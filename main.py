password = input("Parol kiriting: ")

if len(password) < 8:
    print("Juda qisqa!")
elif password.isdigit():
    print("Faqat raqam bo‘lmasin!")
elif password.isalpha():
    print("Raqam ham qo‘shing!")
else:
    print("Kuchli parol! ✅")
