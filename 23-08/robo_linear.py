                             # # # ROBÔ LINEAR # # #

# RL2 é um robô que se move apenas em linha reta, sobre um trilho. Ele é utilizado dentro de uma
# fábrica para realizar diversas tarefas, como distribuir peças e ferramentas para os trabalhadores.
# O RL2 tem apenas dois comandos:
# F: Move o robô 1 metro para a frente;
# T: Move o robô 1 metro para trás;
# Após receber e executar um comando, o robô permanece parado até receber o próximo comando.

 #  #  #  #  #  #  #  #  #  #  #  IMPLEMENTAÇÃO  #  #  #  #  #  #  #  #  #  #  #

frente = []
tras = []

while True:                                                                  # Laço para repetir o programa.
    x = input('Digite F para mover o RL2 1 metro para frente;\n'
              'Digite T para mover o RL2 1 metro para trás;\n'
              'Digite E para encerrar:\n')
    while x != 'F' and x != 'T' and x != 'E':                                # Laço para validar a entrada.
        print('Entrada inválida!')
        x = input('Digite F para mover o RL2 1 metro para frente;\n'
                  'Digite T para mover o RL2 1 metro para trás;\n'
                  'Digite E para encerrar:\n')
    if x == 'F':                                                             # Condição para mover o robô para frente.
        frente.append(x)
        print('Posição atual: {:+.1f}m.\n'.format(len(frente) - len(tras)))
    if x == 'T':                                                             # Condição para mover o robô para trás.
        tras.append(x)
        print('Posição atual: {:+.1f}m.\n'.format(len(frente) - len(tras)))
    if x == 'E':                                                             # Condição de parada do programa.
        print('Posição atual: {:+.1f}m.\n'.format(len(frente) - len(tras)))
        break

# Questão 1: A distância entre a posição inicial e final do robô será dada pela diferença entre o número de comandos
#            F e T. A cada entrada do usuário, é dada a posiçao do robô em relaão a sua posição inicial (0m).

# Questão 2: A posição final será igual a inicial sempre que o número de comandos F for igual ao número de comandos T e
#            será mostrada como 0m na tela.