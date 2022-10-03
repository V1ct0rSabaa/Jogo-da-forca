def jogar() -> None:
    texto_inicial: str = ("*" * 27) + "\nBem vindo ao jogo da forca!\n" + ("*" * 27)
    print(texto_inicial)
    dificuldade: int = 0
    niveis_dificuldade: tuple[str] = ("fácil", "médio", "difícil")
    while dificuldade == 0:
        texto = "Escolha o nível de dificuldade\n1- fácil\n2- médio\n3- difícil: "
        dificuldade = input(texto)
        try:
            dificuldade = int(dificuldade)
            if dificuldade > 3 or dificuldade < 1:
                dificuldade = 0
                print("Digite apenas números entre 1 e 3")
        except ValueError:
            print("Erro, digite apenas números inteiros")
            dificuldade = 0
            
    if dificuldade == 1:
        vidas = 5
        palavra_secreta: str = "python"
        palavra_mostrada: str = "*" * len(palavra_secreta)      
    elif dificuldade == 2:
        vidas = 7
        palavra_secreta: str = "shrubbery"
        palavra_mostrada: str = "*" * len(palavra_secreta)    
    elif dificuldade == 3:
        vidas: int = 8
        palavra_secreta: str = "biggusdickus"
        palavra_mostrada: str = "*" * len(palavra_secreta)
        
    acertou: bool = False
    print(f"Dificuldade definida: {niveis_dificuldade[dificuldade - 1]}")
    while vidas > 0 and not acertou:
        print(f"Palavra: {palavra_mostrada} chances restantes: {vidas}")
        tentativa = input("digite uma letra: ").lower()
        if not tentativa.isalpha():
            print("Digite apenas letras, não números nem outros caracteres")
        elif palavra_secreta.find(tentativa) == -1:
            vidas -= 1
            print(f"a palavra não contém a letra {tentativa}")
        elif len(tentativa) > 1:
            vidas -= 1
            print("Digite apenas uma letra por vez")
        else:
            if tentativa in palavra_secreta:
                for i in range(0, len(palavra_secreta)):
                    if tentativa == palavra_secreta[i]:
                        palavra_mostrada = palavra_mostrada[:i] + tentativa + palavra_mostrada[i+1:]
            if palavra_mostrada == palavra_secreta:
                    acertou = True
    if vidas == 0:
        print(f"Você perdeu, não conseguiu advinhar a palavra {palavra_secreta}")
    elif acertou:
        print(f"Parabéns você acertou, a palavra era {palavra_secreta}")

       
if (__name__ == "__main__"):
    jogar()