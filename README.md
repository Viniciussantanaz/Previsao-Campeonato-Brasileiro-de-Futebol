# Previsão do Campeonato Brasileiro de Futebol Masculino 

Para realizar essa tarefa usei as métricas Num.Finalizações, Num.Finalizações certas, Num.Finalizações cedidas, e Gols cedidos, dessas métricas foi tirado a média de cada time, obtendo a média do desempenho jogando em casa e fora de casa, Utilizei o método estatístico binomial.

$$
\binom{n}{k} = \frac{n!}{k!(n-k)!}
$$

A probabilidade binomial foi utilizada para calcular a probabilidade de Time A e Time B fazer de 1 a 6 gol em X.num de finalização,

Ex: Time A tem em média 16 finalizações por jogo e 8 são certas o Time B sofre em média 15 finalizações por jogo e em média ele sofre 1 gol por partida, ou seja, podemos concluir que a cada 15 finalizações o Time B sofre 1 gol. Com isso vamos calcular a probabilidade do time A fazer 1, 2, 3 até 6 gols (que foi o máximo de gols que um time conseguiu fazer no campeonato).

a probabilidade de vitória do time A, do time A ou de empate é independente, ou seja, se time A tiver 60% de vitória não significa que o time B terá 30% vitória e 10% de dar empate na partida, o objetivo é saber quem tem mais probabilidade de fazer 1 a 6 gols. O método para empate foi usada a seguinte fórmula
(A(1) * B(1)) + (A(2) * B(2)) + (A(3) * B(3))

A probabilidade do Time A fazer 1 gol Mult A probabilidade Time B fazer 1 gol + A probabilidade do Time A fazer 2 gols mult A probabilidade Time B fazer 2 gols ... 

para probabilidade de vitória de ambos times, como explicado a cima, foi usado A(1) + A(2) + A(3) ...


N = Num.Finalizações que time  A tem por partida 

P = A probabilidade do time A fazer o gol

K = Num de sucesso que o time A pode ter (1 a 6)

 • P = (Média.FinaLizações certas timea A / Média.Finalizações tiem A) * (Média.Gols cedidos time B / Média.Finalizações cedidas time B)

• N = Média Finalização Tima A

• K = 1...6
 
$$
\binom{n}{k} = \frac{n!}{k!(n-k)!}
$$

Os dados das finalizações foram importados com a biblioteca selenium e as tabelas de jogos e do campeonato do Wikipedia.com

### Meu Resutado
![Imagem do WhatsApp de 2024-10-20 à(s) 22 33 07_4f4e6d4c](https://github.com/user-attachments/assets/1d2092de-b14f-4b3f-94d8-d757ead22398)

#### Obs. Os dados dados foram coletados antes do fim da 30° rodada, dia 19/10/2024 e os testes realizados no mesmo dia, para obter novos resultados basta executar o arquivo main.py para coletar as finalizações dos times e o arquivo previsao_campeonato.ipynb para obter um novo resultado.

### Ferramentas utilizadas

![NumPy](https://img.shields.io/badge/NumPy-1.20%2B-blue?logo=numpy&logoColor=white)

![SciPy](https://img.shields.io/badge/SciPy-1.7%2B-blue?logo=scipy&logoColor=white)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
