
# TDE-Deteccao-recuperacao-impasses

**Disciplina:** Performance em Sistemas Ciberfísicos<br>
**Professor:** Andrey Cabral Meira

**Link do Vídeo:**

**-----------------------**

**Integrantes do Grupo:**

Gabriel Koji Takii<br>
Geovanna Vitória Brito Soares<br>
Leonardo Michel de Araujo Iankoska<br>
Rhadija Lopes de Souza<br>

**Número do grupo no Canvas:** TDE 10


**Nome de usuário de cada integrante do Github:**

Gabriel Koji Takii:                   GabrielTakii-Perfil<br>
Geovanna Vitória Brito Soares:        Geovann7<br>
Leonardo Michel de Araujo Iankoska:   Leonardoiankoska<br>
Rhadija Lopes de Souza:               Rhadijante13-byte<br>



**-----------------------**

**Linguagem escolhida para o desenvolvimento do trabalho:** Python

**Estrutura do Repositório:**



x<br>
x<br>
x<br>
x<br>
x<br>
x<br>
x<br>
x<br>
x<br>

**-----------------------**<br>
**Instruções de Compilação e Excução**

1- Navegue até a pasta desejada utilizando o terminal:<br>
Exemplo: **cd parte1-filosofos**<br>

2 - Execute o código desejado<br>
Exemplo: **python3 FilosofosTravado.py**

**O mesmo padrão se aplica para as pastas parte2-semaforo e parte3-deadlock**



**-----------------------**



## Módulo 1 - JANTAR DOS FILÓSOFOS

x<br>
x<br>
x<br>
x<br>
x<br>
x<br>
x<br>
x<br>
x<br>

**Descrição**<br>
O Jantar dos Filósofos modela 5 filósofos sentados em mesa circular, alternando entre pensar e comer. Para comer, cada filósofo precisa pegar os dois garfos adjacentes (esquerdo e direito), compartilhados com os vizinhos.

**Solução adotada: hierarquia de recursos**

Cada garfo recebe um índice único (0 a 4). Todos os filósofos pegam sempre o garfo de menor índice primeiro, depois o de maior. Isso elimina a espera circular, a condição de Coffman que causaria o deadlock.<br>
menor = min(garfo_esquerda, garfo_direita)
maior = max(garfo_esquerda, garfo_direita)
garfos[menor].acquire()
garfos[maior].acquire()

**Execução:**
terminal>   “python FilosofosSemTravar.py”
Para encerrar: Ctrl + C<br>

**Saída do código do arquivo "FilosofosSemTravar.py", onde não ocorre deadlock:**<br><b>
<img width="456" height="460" alt="Captura de tela 2026-06-17 011913" src="https://github.com/user-attachments/assets/f4d02c3b-98bc-4e5d-b780-fd1b9a13f2d0" />

**Isso elimina a espera circular, a condição de Coffman que causaria o deadlock.**
<br>

## Módulo 2 - THREADS E SEMÁFOROS

x<br>
x<br>
x<br>
x<br>
x<br>
x<br>
x<br>
x<br>
x<br>


## Módulo 3 - Deadlock
**Cenário com Deadlock**<br>
**Problema:** Existem duas threads e dois locks. A Thread 1 adquire A depois B, a Thread 2 adquire B depois A. Isso cria uma espera circular.

**Saída do código do arquivo "DeadlockTrava.py", onde vai ocorrer um deadlock:**

<img width="297" height="198" alt="Captura de tela de 2026-06-17 01-46-25" src="https://github.com/user-attachments/assets/dd91cb57-882e-4346-9a0c-b9bf1029de2b" />


<br><br>
**Cenário sem Deadlock**<br>
Para solucionar o problema, todas as threads devem adquirir o LOCK A antes do LOCK B

**Saída do código do arquivo "DeadlockSemTravar.py", onde não ocorre deadlock:**

 <img width="319" height="317" alt="Captura de tela de 2026-06-17 01-46-36" src="https://github.com/user-attachments/assets/0bca3290-e952-4a1b-8848-ae7f850816e9" />

**Condição de Coffman quebrada:** Espera circular, pois não é mais possivel formar um ciclo de espera entre os recursos




