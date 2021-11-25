import random

def main():
    G = nuova_griglia()
    G_UI = nuova_griglia()
    while(True):
        print('Griglia: ')
        stampa_griglia(G_UI)#TODO
        print('Inserisci le coordinate della prossima mossa:')
        r = int(input('Riga'))
        c = int(input('Colonna'))
        if G[r][c] == -1:
            print('Hai perso la partita c==3')
            griglia_sconfitta(G,G_UI)#TODO
            stampa_griglia(G_UI)#TODO
            break
        mossa(G,G_UI,r,c)#TODO
        if vittoria(G,G_UI):#TODO
            print("Hai vinto!!!  --c==3")
            break

def nuova_griglia():
    C = valore_parametro('C')#TODO
    R = valore_parametro('R')#TODO
    G = []
    for i in range(R):
        riga = [0]*C
        G.append(riga)
    inserisci_mine(G)#TODO
    inserisci_suggerimenti(G)#TODO
    return G

            