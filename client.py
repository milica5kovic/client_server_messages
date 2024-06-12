import socket

adresa = ('localhost', 2024)
def povezi_se_na_server(adresa):
    klijentski_soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    klijentski_soket.connect(adresa)
    
    return klijentski_soket

def primi_poruku(klijentski_soket):
    poruka = klijentski_soket.recv(1024).decode()
    print(f'Poruka od servera glasi: {poruka} ')
    
def napisi_poruku(klijentski_soket):
    while True:
        poruka = input('Posaljite poruku serveru: ')
        
        if poruka == 'exit':
            klijentski_soket.send(poruka.encode())
            print('Konekcija prekinuta. ')
            break
        else:
            klijentski_soket.send(poruka.encode())
            vracena_poruka = klijentski_soket.recv(1024).decode()
            print(vracena_poruka)
            
            
def ukucaj_sifru(klijentski_soket):
    sifra = input('Ukucajte tajnu sifru: ')
    klijentski_soket.send(sifra.encode())
    status = klijentski_soket.recv(1024).decode()
    if status == 'success':
        print('Sifra je tacna!')
        napisi_poruku(klijentski_soket)
        
    else:
        print('Sifra netacna!')
        
    
    
    
    
    
klijentski_soket = povezi_se_na_server(adresa)
primi_poruku(klijentski_soket)
ukucaj_sifru(klijentski_soket)
    