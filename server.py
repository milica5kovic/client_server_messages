import socket

def hendluj_klijente(serverski_soket, sifra):
    tacna_sifra = False
    while True:
        klijent_soket, klijent_adresa = serverski_soket.accept()
        poruka_dobrodoslice = ('Dobrodošli! Server 2024. ')
        klijent_soket.send(poruka_dobrodoslice.encode())
        klijent_soket.close()
        


def pokreni_server():
    adresa = ('localhost', 2024)
    sifra = 'raf'
    
    # pravimo TCP konekciju
    serverski_soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverski_soket.bind(adresa)
    serverski_soket.listen()
    print(f'[LISTENING......] na portu {adresa[1]} ')
    
    hendluj_klijente(serverski_soket, adresa)
    
    
    
pokreni_server()
    
        