tempoS = int(input('Segundos: '))
hora = tempoS // 3600
min = (tempoS % 3600) // 60
seg = (tempoS % 3600) % 60

print(f'{tempoS}s = {hora}h {min}min {seg}s')