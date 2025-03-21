from datetime import datetime, date

'''
Função "segundas" conta quantos mesmo começaram em uma segunda-feira e retorna a quantidade
'''

def segundas(data_inicio, data_fim):

    d_i = date.fromisoformat(data_inicio)

    d_f = date.fromisoformat(data_fim)

    segundas = 0

    while d_i <= d_f:
        segunda = d_i

        if segunda.day > 1:
            segunda.day = 1
        
        segundas += 1 if segunda.weekday() == 0 else 0

        if(d_i.month < 12): 
            d_i = d_i.replace(month=d_i.month+1) 

        else: 
            d_i = d_i.replace(year=d_i.year+1, month=1) 
            
    return segundas



print(segundas('2024-01-01', '2024-12-31'))