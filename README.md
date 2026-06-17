
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

/
├── parte1-filosofos/
│ ├── FilosofosIngenuo.[java/py]
│ └── FilosofosHierarquia.[java/py]
├── parte2-semaforo/
│ ├── ContadorSemSincronizacao.[java/py]
│ └── ContadorComSemaforo.[java/py]
├── parte3-deadlock/
│ ├── DeadlockIngenuo.[java/py]
│ └── DeadlockCorrigido.[java/py]
├── images/
│ ├── parte1_logs.png
│ ├── parte2_tabela.png
│ └── parte3_logs.png
└── README.md

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



Estrutura do Repositório:

PARTE 1 - JANTAR DOS FILÓSOFOS

Descrição Técnica:

INSTRUÇÕES DE COMPILAÇÃO E EXECUÇÃO

Compilação

Execução

Prints/logs de execução

PARTE 2 - THREADS E SEMÁFOROS

Descrição Técnica:

INSTRUÇÕES DE COMPILAÇÃO E EXECUÇÃO

Compilação

Execução

Prints/logs de execução


## Modulo 3 - Deadlock
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


Estrutura mínima sugerida: pastas parte1
-
filosofos/, parte2
-
semaforo/, parte3
-
deadlock/,
cada uma com seu(s) arquivo(s) fonte; arquivo README.md na raiz.

O README deve conter: nome do grupo e dos integrantes, linguagem escolhida, instruções
de compilação e execução, relatório técnico de cada parte, prints/logs de execução e o link
do vídeo no YouTube.

Histórico de commits
 
deve refletir a participação de todos os integrantes (cada aluno usando
sua própria conta do GitHub). Repositórios com commits concentrados em um único autor
poderão ser penalizados.DEADLOCK

Descrição Técnica:

INSTRUÇÕES DE COMPILAÇÃO E EXECUÇÃO

Compilação

Execução

Prints/logs de execução


PARTICIPAÇÃO DOS INTEGRANTES

Cada integrante participou do desenvolvimento do trabalho utilizando sua respectiva conta do Github, realizando commits relacionado a sua parte do trabalho.  






