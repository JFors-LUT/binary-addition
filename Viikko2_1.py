#V2T1 

def bittisumma(a, b):

    while b != 0:

        # toteuta biteillä laskettu summauksen logiikka tähän
        # lasketaan summa XOR ilman bittien kantamista 
        raaka_summa = a ^ b

        # lasketaan AND bitit joista kannettava 1, kannetaan bitit siirtämällä ne yhden vasemmalle  
        kanto = (a & b) 
        kanto = kanto << 1

        # annetaan a ja b uudet lasketut arvot 
        a = raaka_summa
        b = kanto

    return a

if __name__ == "__main__":

    # testi
    a = 3   
    b = 5
    summa = bittisumma(a, b)
    print(f"The sum of {a} and {b} is {summa}")
