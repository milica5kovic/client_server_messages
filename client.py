import socket

adresa = ('localhost', 2024)
def povezi_se_na_server(adresa):
    klijentski_soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    klijentski_soket.connect(adresa)
    
    return klijentski_soket

def primi_poruku(klijentski_soket):
    poruka = klijentski_soket.recv(1024).decode()
    print(f'Poruka od servera glasi: {poruka} ')
    
    
    
    
    
klijentski_soket = povezi_se_na_server(adresa)
primi_poruku(klijentski_soket)
    