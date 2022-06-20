hora = int(input('Horas: '))
min = int(input('Minutos: '))
seg = int(input('Segundos: '))
segTot = hora * 3600 + min * 60 + seg

print(f'{hora}h {min}min {seg}s = {segTot}s')
