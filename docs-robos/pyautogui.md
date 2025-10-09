# PyAutoGui

## O que é?

O PyAutoGUI é uma biblioteca Python para automação de tarefas envolvendo a interface gráfica do usuário (GUI). Com ela, você pode controlar o mouse e o teclado, além de realizar diversas interações automáticas com a interface do sistema operacional, como mover o mouse, clicar, digitar texto, tirar screenshots e até mesmo localizar elementos na tela.


## Principais Funcionalidades

### Controle do Mouse:

> mover

    pyautogui.moveTo(100, 200)  # Move o mouse para a posição (100, 200)

    pyautogui.move(10, 10)  # Move o mouse em relação à posição atual


> clique

    pyautogui.click(200, 300)  # Clica na posição (200, 300)

    pyautogui.doubleClick()  # Clique duplo

    pyautogui.rightClick()  # Clique com o botão direito


> arrastar

    # Arrasta para a posição (400, 500) em 1 segundo
    pyautogui.dragTo(400, 500, duration=1)  


### Controle do Teclado:

> digitar

    pyautogui.write('Olá, Mundo!')  # Digita "Olá, Mundo!"

    pyautogui.write('Python é incrível!', interval=0.1)  # Intervalo entre teclas


> pressionar teclas

    pyautogui.press('enter')  # Pressiona a tecla Enter

    pyautogui.hotkey('ctrl', 'c')  # Pressiona a combinação de teclas Ctrl + C


### Prints:

    screenshot = pyautogui.screenshot()

    screenshot.save('screenshot.png')  # Salva a captura de tela em um arquivo


### Localizar Elementos na Tela:

O PyAutoGUI pode localizar elementos específicos na tela, como ícones ou imagens, facilitando a automação de cliques em elementos visuais.

    # Encontra a imagem e retorna o centro dela
    position = pyautogui.locateCenterOnScreen('image.png')  


### Segurança:

Caso precise interromper a execução do script, o PyAutoGUI oferece a funcionalidade de failsafe, onde mover o mouse para o canto superior esquerdo da tela pode parar a execução do script.

    pyautogui.FAILSAFE = True  # Ativa o failsafe


`O que é o failsafe?`

O failsafe no PyAutoGUI é uma medida de segurança que permite interromper a execução de um script caso o mouse se mova para o canto superior esquerdo da tela. Ou seja, se você estiver rodando um script e ele começar a fazer algo que você não quer, basta mover o mouse rapidamente para o canto superior esquerdo da tela, e o script será interrompido automaticamente.

`Como funciona?`

Quando o failsafe está ativado (que é o padrão), se o mouse for movido para a posição (0, 0) (canto superior esquerdo da tela), o PyAutoGUI levantará uma exceção pyautogui.FailSafeException e interromperá a execução do script.

`Como ativar ou desativar?`

**Ativado por padrão**: O failsafe é ativado por padrão. Ou seja, sempre que o mouse for movido para o canto superior esquerdo, o script será interrompido.

**Desativado**: Caso você queira desativar o failsafe, você pode fazer isso definindo a variável pyautogui.FAILSAFE como False.


### Teclas de Atalho

Todas as combinações suportadas pelo Windows podem ser usadas aqui através do `pyautogui.hotkey()`, onde cada tecla é passada como parametro

    pyautogui.hotkey()

### Funções Auxiliares

* Verificação de Tamanho da Tela: Para saber a resolução da tela.

```
width, height = pyautogui.size()  

```

* Posição do Mouse: Você pode obter a posição atual do mouse

```
x, y = pyautogui.position()

```