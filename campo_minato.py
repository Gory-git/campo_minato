import random

def main():
    G = nuova_griglia()
    G_UI = nuova_griglia_UI()
    while(True):
        print('Griglia: ')
        stampa_griglia(G_UI)
        print('Inserisci le coordinate della prossima mossa:')
        r = int(input('Riga'))
        c = int(input('Colonna'))
        if G[r][c] == -1:
            print('Hai perso la partita c==3')
            griglia_sconfitta(G,G_UI)
            stampa_griglia(G_UI)
            break
        mossa(G,G_UI,r,c)
        if vittoria(G,G_UI):#TODO
            print("Hai vinto!!!  --c==3")
            break

def nuova_griglia():
    C = valore_parametro('C')
    R = valore_parametro('R')
    G = []
    for i in range(R):
        riga = [0] * C
        G.append(riga)
    inserisci_mine(G)
    inserisci_suggerimenti(G)
    return G

def valore_parametro(parametro):
    #tante costanti scelte dal prof
    difficolta = 'bassa' #da impostare
    C = 8
    R = 8
    cella_mina = '*'
    cella_coperta = '.'

    difficolta_bassa = 0.14
    difficcolta_media = 0.22
    difficolta_alta = 0.41
    difficolta_estrema = 0.6

    if parametro == 'C':
        return C
    if parametro == 'R':
        return R
    if parametro == 'M':
        if difficolta == 'bassa':
            return int(R*C*difficolta_bassa)
        if difficolta == 'media':
            return int(R*C*difficcolta_media)
        if difficolta == 'alta':
            return int(R*C*difficolta_alta)
        if difficolta == 'estrema':
            return int(R*C*difficolta_estrema)
    if parametro == 'cella_coperta':
        return cella_coperta
    if parametro == 'cella_mina':
        return cella_mina

def inserisci_mine(G):
    C = valore_parametro('C')
    R = valore_parametro('R')
    M = valore_parametro('M')
    mine_inserite = 0
    i = 0
    while mine_inserite < M:
        j = 0
        while mine_inserite < M and j < C:
            if random.random()<M / (C * R) and G[i % R][j] != -1:
                G[i % R][j] = -1
                mine_inserite += 1
            j += 1
        i += 1

def inserisci_suggerimenti(G):
    C = valore_parametro('C')
    R = valore_parametro('R')
    for i in range(R):
        for j in range(C):
            if G[i][j] == -1:
                if i > 0 and j > 0 and G[i - 1][j - 1] != 1: #angolo in alto a sx
                    G[i - 1][j - 1] += 1
                if i > 0 and G[i - 1][j] != -1: #in alto centrale
                    G[i - 1][j] += 1
                if i > 0 and j + 1 < C and G[i - 1][j + 1] != -1: #angolo in alto a dx
                    G[i - 1][j + 1] += 1
                if j > 0 and G[i][j - 1] != -1: #sx
                    G[i][j - 1] += 1
                if j + 1 < C and G[i][j + 1]: #dx
                    G[i][j +1] += 1
                if i + 1 < R and j > 0 and G[i + 1][j - 1]: #angolo in basso a sx
                    G[i + 1][j - 1] += 1
                if i + 1 < R and G[i + 1][j] != -1: #in basso centrale
                    G[i + 1][j] += 1
                if i + 1 < R and j + 1 < C and G[i + 1][j + 1] != -1: #angolo in basso a dx
                    G[i + 1][j + 1] += 1

def nuova_griglia_UI():
    C = valore_parametro('C')
    R = valore_parametro('R')
    G_UI = []
    for i in range(R):
        riga = [valore_parametro('cella_coperta')] * C
        G_UI.append(riga)
    return G_UI

def stampa_griglia(griglia):
    for riga in griglia:
        for elemento in riga:
            print(str(elemento) + " ",end='')
        print()

def griglia_sconfitta(G,G_UI):
    R = valore_parametro('R')
    C = valore_parametro('C')
    for i in range(R):
        for j in range(C):
            if G[i][j] == -1:
                G_UI[i][j] = valore_parametro('cella_mina')

def mossa(G,G_UI,r,c):
    if G[r][c] > 0:
        G_UI[r][c] = G[r][c]
    else:
        scopri_adiacenti(G,G_UI,r,c)

def scopri_adiacenti(G,G_UI,r,c):
    if G_UI[r][c] != valore_parametro('cella_coperta'):
        return
    G_UI[r][c] = G[r][c]
    if G[r][c] > 0:
        return
    R = valore_parametro('R')
    C = valore_parametro('C')
    if r > 0 and c > 0:
        scopri_adiacenti(G,G_UI,r - 1,c - 1)
    if r > 0:
        scopri_adiacenti(G,G_UI,r - 1,c)
    if r > 0 and c + 1 < C:
        scopri_adiacenti(G,G_UI,r - 1,c + 1)
    if c > 0:
        scopri_adiacenti(G,G_UI,r,c - 1) 
    if c + 1 < C:
        scopri_adiacenti(G,G_UI,r,c + 1)
    if r + 1 < R and c > 0:
        scopri_adiacenti(G,G_UI,r + 1,c - 1)
    if r + 1 < R:
        scopri_adiacenti(G,G_UI,r + 1,c)
    if r + 1 < R and c + 1 < C:
        scopri_adiacenti(G,G_UI,r + 1,c + 1)


def vittoria(G,G_UI):
    R = valore_parametro('R')
    C = valore_parametro('C')
    for i in range(R):
        for j in range(C):
            if G_UI[i][j] == valore_parametro('cella_coperta') and G_UI[i][j] != -1:
                return False
    return True

main()