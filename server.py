import socket

def hendluj_klijente(serverski_soket, sifra):
    tacna_sifra = False
    while True:
        if not tacna_sifra:
            klijent_soket, klijent_adresa = serverski_soket.accept()
            poruka_dobrodoslice = ('Dobrodošli! Server 2024. ')
            klijent_soket.send(poruka_dobrodoslice.encode())
            
            primljena_sifra = klijent_soket.recv(1024).decode()
        
            if primljena_sifra != sifra:
                klijent_soket.send('fail'.encode())
                print('Klijent nije ukucao tacnu sifru! ')
                klijent_soket.close()
            else:
                klijent_soket.send('success'.encode())
                print('Ukucana je dobra sifra!')
                tacna_sifra = True
                
        else:
            primljena_poruka = klijent_soket.recv(1024).decode()
            print(f'Klijent salje: {primljena_poruka}')
            if primljena_poruka == exit:
                print('Klijent je prekinuo komunikaciju.')
                klijent_soket.close()
                #vracamo da je sifra netacna
                tacna_sifra = False
                
            else:
                klijent_soket.send(primljena_poruka.upper().encode())
                print(f'Odgovor: {primljena_poruka.upper()}')
            
        


def pokreni_server():
    adresa = ('localhost', 2024)
    sifra = 'raf'
    
    # pravimo TCP konekciju
    serverski_soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverski_soket.bind(adresa)
    serverski_soket.listen()
    print(f'[LISTENING......] na portu {adresa[1]} ')
    
    hendluj_klijente(serverski_soket, sifra)
    
    
    
pokreni_server()
    
        