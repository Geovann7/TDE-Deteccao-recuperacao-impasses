
# TDE-Deteccao-recuperacao-impasses

**Disciplina:** Performance em Sistemas Ciberfísicos<br>
**Professor:** Andrey Cabral Meira

**Link do Vídeo:**

https://youtu.be/4UsPLPPX68A

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



**-----------------------**<br>

**Linguagem escolhida para o desenvolvimento do trabalho:** Python<br>

**Estrutura do Repositório:**<br>



<img width="248" height="293" alt="image" src="https://github.com/user-attachments/assets/d7d61eab-43b6-463f-ab0a-74829af6d17d" />


A pasta parte1-filosofos contém os códigos referentes ao problema do jantar dos filósofos. Com a versão em deadlock e a versão corrigida sem deadlock.<br>

A pasta2-semaforo contém os códigos referentes ao uso de threads com e sem semáforo.<br>

A pasta3-deadlock contém os códigos referentes à simulação de deadlock com locks e à versão corrigida.<br>

O arquivo README.md está localizado na raiz do repositório e contém as informações do grupo, instruções de execução, relatórios técnicos, prints de execução e o link do vídeo do youtube.<br>


<br><br>

**-----------------------**<br>
**Instruções de Compilação e Excução**

1- Navegue até a pasta desejada utilizando o terminal:<br>
Exemplo: **cd parte1-filosofos**<br>

2 - Execute o código desejado<br>
Exemplo: **python3 FilosofosTravado.py**

**O mesmo padrão se aplica para as pastas parte2-semaforo e parte3-deadlock**



**-----------------------**



## Módulo 1 - JANTAR DOS FILÓSOFOS

**Descrição**<br>
O Jantar dos Filósofos modela 5 filósofos sentados em mesa circular, alternando entre pensar e comer. Para comer, cada filósofo precisa pegar os dois garfos adjacentes (esquerdo e direito), compartilhados com os vizinhos.

**Solução adotada: hierarquia de recursos**

Cada garfo recebe um índice único (0 a 4). Todos os filósofos pegam sempre o garfo de menor índice primeiro, depois o de maior. Isso elimina a espera circular, a condição de Coffman que causaria o deadlock.<br>
menor = min(garfo_esquerda, garfo_direita)
maior = max(garfo_esquerda, garfo_direita)
garfos[menor].acquire()
garfos[maior].acquire()

<br><br>

**Saída do código do arquivo "FilosofosSemTravar.py", onde não ocorre deadlock:**<br><b>
<img width="456" height="460" alt="Captura de tela 2026-06-17 011913" src="https://github.com/user-attachments/assets/f4d02c3b-98bc-4e5d-b780-fd1b9a13f2d0" />

**Isso elimina a espera circular, a condição de Coffman que causaria o deadlock.**
<br>





<br><br>
**Cenário com Deadlock**<br>
No arquivo filosofostravado.py, foi implementada a versão ingênua do problema do Jantar dos Filósofos. Nessa versão, existem 5 filósofos e 5 garfos. Cada filósofo alterna entre pensar, ficar com fome e tentar comer.<br>

Para comer, cada filósofo tenta pegar primeiro o garfo da esquerda e depois o grafo da direita:<br>

garfos[garfo_esquerda].acquire()<br>
time.sleep(1)<br>
garfos[garfo_direita].acquire()<br>

O deadlock pode acontecer quando todos os filósofos pegam o garfo da esquerda ao mesmo tempo. Depois disso, cada um tenta pegar o garfo da direita, mas esse garfo já está sendo usado pelo filósofo vizinho. A condição presente nesse caso é a espera circular, pois cada filósofo segura um garfo e espera pelo garfo que está com outro filósofo.<br>

**Pseudocódigo da versão ingênua**<br>

Início<br>

Criar 5 filósofos<br>
Criar 5 garfos<br>

Para cada filósofo:<br>
Pensar<br>
ficar com fome<br>

Definir garfo da esquerda<br>
Definir garfo da direita<br>

Comer<br>

Soltar garfo da direita<br>
Soltar garfo da esquerda<br>

Volta a pensar<br>
Fim<br>

Nessa versão, o progresso não é garantido, pois as threads podem ficar presas em deadlock. Quando isso acontece, nenhum filósofo consegue continuar comendo, porque todos ficam esperando pelo segundo garfo.<br>

<br><br>

A saída do código do arquivo filosofostravado.py, onde pode ocorrer deadlock:<br>

<img width="1265" height="440" alt="Captura de tela 2026-06-17 161844" src="https://github.com/user-attachments/assets/d80a520b-79eb-48d8-a4d2-57faf63c50bf" />


## Módulo 2 - THREADS E SEMÁFOROS
**Cenário sem sincronização**<br>
**Problema:** 8 threads incrementam 200.000 vezes cada uma uma variável global contador, sem nenhum mecanismo de controle de acesso. O valor esperado é T × M = 8 × 200.000 = 1.600.000, mas a operação de incremento não é interrompivel, podendo causar condição de corrida (Race Condition).

**Saída do código do arquivo "ThreadsSemSemafaro.py", com 3 execuções:**

<img width="319" height="317" alt="WhatsApp Image 2026-06-17 at 14 36 42 (1)" src="https://github.com/user-attachments/assets/31d9b0fc-afe4-4012-b8e6-3e36ae53c356" />

Teste	/ Esperado	/ Obtido	/ Tempo (s) <br>
1/	1.600.000	/ 1.600.000	/ 0,060 <br>
2/	1.600.000	/ 1.600.000	/ 0,055 <br>
3/	1.600.000	/ 1.600.000	/ 0,072

<br><br>
**Cenário com semáforo**<br>
Para solucionar o problema, utiliza-se um semáforo binário (threading.Semaphore(1)), garantindo que apenas uma thread por vez acesse e modifique a variável compartilhada.

**Saída do código do arquivo "ThreadsComSemafaro2.py", com 3 execuções:**

<img width="319" height="317" alt="WhatsApp Image 2026-06-17 at 14 36 42 (3)" src="https://github.com/user-attachments/assets/c58bb724-b158-4640-b5bd-dca628bfdb55" />

Teste	/ Esperado	/ Obtido	/ Tempo (s) <br>
1/	1.600.000	/ 1.600.000	/ 1,32 <br>
2/	1.600.000	/ 1.600.000	/ 1,16 <br>
3/	1.600.000	/ 1.600.000	/ 1,19

<br><br>
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




