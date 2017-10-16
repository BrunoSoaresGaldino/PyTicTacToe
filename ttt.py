import random

def MostraTabuleiro( tabuleiro ):
    
    i = 0;
    
    print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
    
    print '  1   2   3\n'
    
    while( i < 9):
        
        
        print i+1,tabuleiro[i],'|',tabuleiro[i+1],'|',tabuleiro[i+2]
        
        if( i < 6):
        
            print '  ---------'
   
        i += 3
    
def MovimentoJogador( tabuleiro , simbolo ):
    
    linha = -1;
    
    coluna = -1;
    
    while(  linha-1 < 0 or linha-1 > 3  or coluna-1 < 0 or coluna-1 > 3 or tabuleiro[ (linha-1)*3 + coluna-1 ] != ' ' ):
        
        print
        
        try:
            
            linha = int ( raw_input('linha ?') )
        
        except: linha = -1
        
        print
        
        try:
        
            coluna = int( raw_input('coluna ?') )
        
        except:
            
            coluna = -1
        
    tabuleiro[ (linha-1)*3 + coluna-1 ] = simbolo
    
def CheckWin( tabuleiro ):
    
    i = 0
    
    while( i < 3):
        
        if( ( tabuleiro[ i*3 ] == tabuleiro[ i*3 + 1 ] ) and ( tabuleiro[ i*3] == tabuleiro[ i*3 + 2 ] ) and tabuleiro[ i*3 ] != ' ' ) :
            
            return tabuleiro[ i*3 ]
            
        i += 1
    
    i = 0
    
    while( i < 3 ):
        
        if( ( tabuleiro[i] == tabuleiro[ 3 + i ] )  and  ( tabuleiro[i] == tabuleiro[ 6 + i ] ) and  (tabuleiro[i] != ' ') ):
            
            return tabuleiro[i]
    
        i += 1
    
 
    if( ( tabuleiro[ 0 ] == tabuleiro[ 4 ] ) and ( tabuleiro[ 0 ] == tabuleiro[ 8 ] ) and ( tabuleiro[ 0 ] != ' ' ) ):
        
        return tabuleiro[ 0 ]
        
    if( ( tabuleiro[ 2 ] == tabuleiro[ 4 ] ) and ( tabuleiro[ 2 ] == tabuleiro[ 6 ] ) and ( tabuleiro[ 2 ] != ' ' ) ):
        
        return tabuleiro[ 2 ]
    
    i = 0
    
    while( i < 9 ):
        
        if( tabuleiro[ i ] == ' '):
            
            break
        
        if( i == 8):
            
            return 'e'
            
        i += 1
        
    return ' '


def MovimentoComputador( tabuleiro , simbolo ):

    i = 0
    j = 0
    
    simbolos = ['o','x']
    
    ch = ''
    
    cantos = [0, 2, 8, 6 ];
    
    casas = [ 0,1,2,2,1,0,0,2,1,3,4,5,5,4,3,3,5,4,6,7,8,8,7,6,6,8,7,0,3,6,6,3,0,0,6,3,1,4,7,7,4,1,1,7,4,2,5,8,8,5,2,2,8,5,0,4,8,8,4,0,0,8,4,2,4,6,6,4,2,2,6,4 ]
  
  
    if (simbolo == 'x'):
    
        simbolos[0] = 'x';
        simbolos[1] = 'o';
    

    j = 0
    
    while( j < 2 ):
    
        
        ch = simbolos[j];

        i = 0
        
        while( i < len( casas ) ):
            
            if( ( tabuleiro[ casas[i] ] == ch ) and ( tabuleiro[ casas[ i+1 ] ] == ch)):
                
                if( tabuleiro[ casas[ i+2 ] ] == ' '):
                
                   tabuleiro[ casas[ i+2 ]] = simbolo
                   
                   return
                    
                    
            i += 3
        j += 1


    if ( tabuleiro[ 4 ] == ' '):
    
        tabuleiro[ 4 ] = simbolo
        return
    
    
    if ( tabuleiro[ 4 ] == simbolo):
        
        i = 1
        
        while( i < 9 ):
            
            if( tabuleiro[ i ] == ' '):
            
                tabuleiro[ i ] = simbolo
                
                return
            
            
            i += 2
        

    i = random.choice(cantos)
    
    j = 0;

    while( ( tabuleiro[ i ] != ' ') and ( j < 4) ):
        
        j += 1
        
        i = random.choice(cantos)
    
    
    tabuleiro[ i ] = simbolo
    
    
tabuleiro = [ ' ',' ',' ',' ',' ',' ',' ',' ',' ' ]

simbolo = 'o'

simbolo_computador = 'x'

if( raw_input('Qual simbolo vc escolhe, x ou o ?') == 'x' ):
    
    simbolo = 'x'
    simbolo_computador = 'o'

MostraTabuleiro( tabuleiro )    

if( simbolo == 'x'):

    MovimentoJogador(tabuleiro , simbolo )

    MostraTabuleiro(tabuleiro)
    

while(True):
    
    
    
    MovimentoComputador( tabuleiro , simbolo_computador )
    
    MostraTabuleiro(tabuleiro)
    
    if( CheckWin( tabuleiro ) == simbolo_computador ):
        print 'lose'
        break
        
    elif( CheckWin( tabuleiro ) == 'e'):
        
        print 'draw'
        break
    
    
    MovimentoJogador(tabuleiro , simbolo )

    MostraTabuleiro(tabuleiro)
    
    if( CheckWin( tabuleiro ) == simbolo ):
        print 'win'
        break
        
    elif( CheckWin( tabuleiro ) == 'e'):
        
        print 'draw'