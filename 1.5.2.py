import os

#ez a parancsok meghatarozása
parancsok_kiirasa = '   cp: parancsok kiiratása;'
hello_kiirasa = '   hello: ezzel a bemutatkozó szöveget írja ki a gép;'
kilepes_kiirasa = '   exit: kilépés a programból;'
adatok_kiirasa = '   ap: ezzel az adatokat írod ki;'
nev_kiirasa = '   ni: ezzel az adatok közé felvesszük a nevedet;'
becenev_kiirasa = '   nni: ezzel az adatok közé felvesszük a becenevedet;'
clear_kiirasa = '   [adatmeghatározás] \clear:  ezzel az adatok közül tudsz törölni(akármit!);'
fajlok_kinyitasa = '   oF: a fájlkezelő megnyitására alkalmas ez a parancs'

#ide fognak kerülni a vátozók többsége
vanAdatN = False
vanAdatNN = False

#ez a filekezelő definicíója
def File():
    utvonal = input('Add meg a fájl elérési útvonalat! ')
    os.chdir(utvonal)
    filecmd = input(utvonal)
    while filecmd != 'Ef':
        if filecmd == 'md':
            mn  = input('Add meg a mappa nevét! ')
            os.makedirs(utvonal + mn) 
        elif filecmd == 'um':
            utvonal = input('Add meg az elérési útvonalat! ')
            os.chdir(utvonal)
        elif filecmd == 'Ef':
            parancs = input('Add meg a következő parancsot')
        elif filecmd == 'rd':
            tm = input('Add meg a mappa nevét! ')
            os.removedir
        elif filecmd == 'Otxt':
            tn = input('add  meg a nevét! ')
            tf = open(utvonal + tn)
            print(tf)
        else:
            print('Helytelen Parancs!!')
        filecmd = input(utvonal)
#ide meg a meghatározások
def cp():
    #CommandPrint meghatározása
    parancsok_szama = ['parancsok: ', parancsok_kiirasa, hello_kiirasa, kilepes_kiirasa, adatok_kiirasa, nev_kiirasa, becenev_kiirasa,  clear_kiirasa,  fajlok_kinyitasa]
    for pindex in range(len(parancsok_szama)):
        print(parancsok_szama[pindex])
#ciklus____________________________________________
def ciklus():
    print('Ez egy parancs kezelő program. Minden parancs levan programozva, szabálytalan prancsért hibaüzenetet kapsz!')
    print('-----------------------------------------------------------------')
    print('írd be az eslő parancsodat legyen ez a hello')
    parancs = input('írd be a parancsodat!: ')
    while parancs != 'exit':
        #ez az alap parancs ezzel lehet a parancsokat kiiratni
        if parancs == 'cp':
            cp()
        #ezzel a bemutatkozó szöveget lehet kiiratni
        elif parancs == 'hello':
            print('hello ez a PapageiCommand 1.3.2-es verziója! Ha nem Tudnád mik a prancsok írd be a cp parancsot!')
        #ezzel a nevet lehet megadni
        elif parancs == 'ni':
            Name = input('Ird be a nevedet! ')
            vanAdatN = True
        #ezzel a becenevet
        elif parancs == 'nni':
            Nickname = input('Ird be a becenevedet! ')
            vanAdatNN = True
        #ide fog kerülni a File-ok------------------------------------------------------------------------
        elif parancs == 'oF':
            File()
        #itt a vége lesz----------------------------------------------------------------------------------
        #ezzel az adatokat
        elif parancs == 'ap':
            if vanAdatN:
                print('Név: ', Name)
            if vanAdatNN:
                print('Becenév: ', Nickname)            
            if not vanAdatN and vanAdatNN:
                print('Nem nem adtál meg nevet')
            if not vanAdatNN and vanAdatN:
                print('Nem adtál meg becenevet')
            if not vanAdatN and not vanAdatNN:
                print('Egy adatot sem adtál meg. Miért iratod ki?!')
        elif parancs == 'ap \clear' and vanAdatN and vanAdatNN:
            vanAdatN = False
            vanAdatNN = False
            print('Loading...')
            print('clearO...')
            print('az adatok törölve')
        elif parancs == 'ni \clear' and vanAdatN:
            vanAdatN = False
            print('Loading...')
            print('clearO...')
            print('a Név törölve')
        elif parancs == 'nni \clear' and vanAdatNN:
            vanAdatNN = False
            print('Loading...')
            print('clearO...')
            print('a becenév törölve')
        #itt egy error üzenet kiiratása lesz számon
        else:
            print('ERROR! A Parancs nem bináris!')
        parancs = input('írd be a következő parancsodat!: ')
        #1. eddigi parancsok száma 6
        #2. eddig már eljutottam tehát lesz valami
#ciklus vége_______________________________________
Jelszo = input('Add meg a jelszót!')

if Jelszo == '123':
    ciklus()

proba = 0
lehetoseg = 3
if Jelszo =='vk':
    VK = input("Ird be a veszjelszot(2jegyu szam)")
    if VK == '69':
        ciklus()
if Jelszo != '123' or Jelszo != 'vk':
    while Jelszo != '123' and proba != 3:
        print('Helytelen jelszó!')
        print(lehetoseg, 'próbálkozási lehetőséged maradt')
        proba += 1
        lehetoseg -= 1
        Jelszo = input()
if Jelszo == '1231':
        ciklus()
if proba >= 3:
    print('Átlépted a 3 próbálkozási lehetőséget!')
print('Viszontlátásra!')
