def partidas_ranqueadas(vitorias,derrotas):
    rankeadas = vitorias - derrotas
    return rankeadas

saldo_vitorias = partidas_ranqueadas(200,30)

if saldo_vitorias <= 10:
    nivel = "Ferro"
elif saldo_vitorias <= 20:
    nivel = "Bronze"
elif saldo_vitorias <= 50:
    nivel = "Prata"
elif saldo_vitorias <= 80:
    nivel  = "Ouro"
elif saldo_vitorias <= 90:
    nivel = "Diamante"
elif saldo_vitorias <= 100:
    nivel = "Lendário"
else:
    nivel = "Imortal"

print(f"O Herói tem de saldo de {saldo_vitorias} está no nível de {nivel}")    
