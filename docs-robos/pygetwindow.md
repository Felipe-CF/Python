# pygetwindow

A biblioteca pygetwindow é usada para interagir com janelas abertas no sistema operacional. Com ela, você pode obter informações sobre janelas, ativá-las, movê-las, redimensioná-las e manipulá-las de outras formas.

## Obter todas as janelas abertas

```
    import pygetwindow as gw

    janelas = gw.getAllWindows()

    print(janelas)  
    # Retorna uma lista de objetos representando as janelas abertas
```

## Obter a janela ativa (em foco no momento)

```
    import pygetwindow as gw

    janela_ativa = gw.getActiveWindow()
    
    print(janela_ativa.title) if janela_ativa else print("Nenhuma janela ativa.")

```

## Obter uma janela específica pelo título

```
    import pygetwindow as gw

    # Substitua pelo título correto
    janela = gw.getWindowsWithTitle("Bloco de Notas")  

    if janela:
        print("Encontrada:", janela[0].title)


```

## Mover, redimensionar, minimizar, maximizar e restaurar

```
janela_ativa.moveTo(100, 100)  # Move a janela ativa para (100, 100)

janela_ativa.resizeTo(800, 600)  # Define o tamanho para 800x600 pixels

janela_ativa.resizeTo(800, 600)  # Define o tamanho para 800x600 pixels

janela_ativa.minimize()  # Minimiza

janela_ativa.maximize()  # Maximiza

janela_ativa.restore()   # Restaura ao tamanho normal

```

## Onde usar pygetwindow?

* Automação de tarefas com pyautogui

* Controle de janelas em sistemas sem precisar de interações manuais

* Organização de várias janelas abertas








