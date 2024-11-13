def guess_number():
    secret_number = 9
    guess = 0
    guess_limit = 3
    
    
    while guess < guess_limit:
        user = int(input("masukkan anggka > "))
        if user == secret_number:
            print("selamat, anda berhasil menemukan")
            break
        else:
            print("salah!")
            guess += 1
            
    else:
        print(f"Gagal, angkanya adalah {secret_number}")
        