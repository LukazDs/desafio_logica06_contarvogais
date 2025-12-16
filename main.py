def contarVogais():
    
    palavra = input('Digite uma palavra: ')
    vogais = 'aeiou'
    
    vogaisComputadas = ''
    
    for letra in palavra:
        
        if letra in vogais:
            
            if letra not in vogaisComputadas:
                
                vogaisComputadas += f' {letra} '
        
    print(f'\nA palavra {palavra} tem as seguintes vogais:{vogaisComputadas}')
    
contarVogais()
