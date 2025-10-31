"""Lista de exercícios de Python"""

#copie e cole esse texto no seu repositório e embaixo resolva as questões

"""
1) Crie um programa de apresentação pessoal que pede um input pro usuário e exiba uma frase como: "Olá, Ana! Você tem 22 anos e mora em Guarapari."
Entenda o conceito de variáveis e quais são os inputs a serem feitos."""


#code aqui


"""
2) Faça uma calculadora simples
Peça 2 números inteiros e mostre a soma, a subtração, a multiplicação e a divisão.

Ex: Calculadora(2, 3)
resposta: 
Soma: 5 
Subtração: -1 
Multiplicação: 6 
Divisão: 0.66 """


#code aqui


"""
3) Contando letras: Peça uma palavra e mostre
a) quantas letras ela tem
b) quantas vezes aparece a letra “a”
c) a palavra toda em maiúsculas

Ex input: "Maria"
resposta:
Tamanho: 5
A letra 'a' aparece 2 vezes
MARIA

"""

#code aqui


"""
4) Formatação de nome: Receba o nome completo do usuário
exiba apenas o primeiro nome e o último nome, formatados corretamente.

Ex input: maria lucia das dores silva
resposta:
Primeiro nome: Maria
Último nome: Silva
"""

#code aqui


"""
5) Lista de compras: Crie uma lista com 5 itens e exiba:
a) o primeiro e o último item
b) a lista em ordem alfabética

ex: lista = ["arroz", "pão", "leite", "feijão", "queijo"]  
resposta: 
Primeiro item: arroz
Último item: queijo
Lista em ordem alfabética: ['arroz', 'feijão', 'leite', 'pão', 'queijo']
"""

#code aqui


"""
6) Crie um dicionário com o nome de 3 alunos e suas notas.
Mostre apenas os nomes dos alunos aprovados (nota ≥ 7).

ex input: alunos = {
    "Ana": 8.5,
    "Bruno": 6.0,
    "Carla": 9.0
}
resposta:
Alunos aprovados:
- Ana
- Carla

"""

#code aqui


"""
7) Peça que o usuário digite 5 números e armazene em um conjunto (set) 
mostre o conjunto final, sem números repetidos.

ex input: 
Digite o 1º número: 4
Digite o 2º número: 7
Digite o 3º número: 4
Digite o 4º número: 9
Digite o 5º número: 7
resposta:
Conjunto final (sem repetição): {9, 4, 7}
"""

#code aqui


"""
8) Peça o ano de nascimento do usuário e informe se ele é menor de idade ou maior de idade, também verifique se ele é idoso(+60)
ex input: Digite o ano do seu nascimento: 1960
resposta:
Você tem 65 anos.
Você é idoso.
"""

#code aqui


"""
9) Crie um programa com um menu em loop (while True) que mostre:
1. Dizer “Olá, bem-vindo!”
2. Mostrar um número aleatório de 1 a 5
3. Fazer a conta da função de calculadora(exercicio 2) com 2 números(peça eles com input).
4. Verifique se a pessoa é maior de idade dentro do loop(chame a função do exercício 9)
5. Sair

O menu só deve encerrar quando a opção 5 for escolhida."""


#code aqui


"""
10) O computador escolhe um número de 1 a 10 e o jogador tenta adivinhar usando while.
Você pode dar dicas pro usuário para ele saber se o número é mais alto ou mais baixo.

ex: Tente adivinhar o número que estou pensando (entre 1 e 10)!
Digite seu palpite: 5
Muito baixo! Tente novamente.
Digite seu palpite: 10
Muito alto! Tente novamente.
Digite seu palpite: 7
Você acertou! O número era 7.

"""


#code aqui


"""
11) Escreva uma função media(n1, n2) que receba duas notas (float) e retorne a média.
Depois, usando a média, mostre se o aluno foi:
- Aprovado (média ≥ 7)
- Em recuperação (5 ≤ média < 7)
- Reprovado (média < 5)

Exemplo:
Entrada: 8.0 e 6.0
Saída:
Média: 7.0
Situação: Aprovado
"""


#code aqui


"""
12) Crie uma função quadrado(n) que retorne n*n.
Crie também soma_quadrados(a, b) que use quadrado(a) e quadrado(b)
para retornar a soma dos quadrados de a e b.

Exemplo:
Entrada: a=3, b=4
Saída: Soma dos quadrados: 25
"""


#code aqui


"""
13) Escreva uma função recursiva fatorial(n) que retorne n! (fatorial de n).
Considere 0! = 1 e 1! = 1. Trate entradas negativas com uma mensagem.

Exemplo:
Entrada: 5
Saída: 120
"""


#code aqui


"""
14) Peça 3 nomes ao usuário (um por input) e grave cada um em uma nova linha
no arquivo 'nomes.txt' usando with open(..., 'w', encoding='utf-8').
Ao final, exiba uma mensagem confirmando a gravação.
"""


#code aqui


"""
15) Leia o arquivo 'nomes.txt' criado no exercício anterior e exiba o conteúdo
na tela, uma linha por vez, numerando os nomes:
Exemplo de saída:
1) Ana
2) Bruno
3) Carla
"""


#code aqui


"""
16) Peça o nome e a nota de 3 alunos e salve no arquivo 'notas.txt' no formato:
Ana: 8.5
Bruno: 7.2
Carla: 9.0
Dica: use with open(..., 'w', encoding='utf-8') e f-strings.
"""


#code aqui


"""
17)Importe o módulo math e mostre:
a) a raiz quadrada de um numero dado por um input(verificar se dá para fazer raiz quadrada nesse numero)
b) o valor de π (math.pi) até certa casa decimal dada por input
c) o resultado de math.ceil() e math.floor() de 2 numeros dados por input

Exemplo de saída:
Raiz de 25: 5.0
Pi com 4 casas: 3.1415
ceil(4.3): 5
floor(4.3): 4
"""


#code aqui


"""
18) Crie um programa com menu (loop while) que permita:
1) Cadastrar nome e idade em 'cadastros.txt' (uma pessoa por linha: "Nome - Idade")
2) Listar todos os cadastros (ler e imprimir o arquivo)
3) Encerrar o sistema

Use funções para organizar (ex.: cadastrar(), listar(), menu()) e with open para manipular o arquivo.
"""


#code aqui


"""
19) Agenda simples com dicionários aninhados + persistência
Estrutura em memória:
contatos = {
    "nome": {"telefone": "...", "email": "..."}
}

Crie um menu com as opções:
1) Adicionar contato (nome, telefone, email)
2) Buscar contato por nome
3) Editar contato (alterar telefone e/ou email)
4) Listar todos os contatos
5) Salvar em arquivo 'agenda.txt' (formato livre) e carregar do arquivo
6) Sair

Dica: use formato de texto simples.
"""

#code aqui


"""
20) Crie um programa que peça dois números e mostre o resultado da divisão.
Use try/except para tratar o erro de divisão por zero.

Exemplo:
Entrada: 10 e 0
Saída:
Erro: não é possível dividir por zero!
"""


#code aqui


"""
21) Peça que o usuário insira dois números inteiros.
Trate possíveis erros:
- ValueError (caso digite letras)
- ZeroDivisionError
- qualquer outro erro genérico (Exception)

Exemplo:
Entrada: a e 3
Saída: Erro: valor inválido.
"""


#code aqui


"""
22) Crie um programa que:
- peça um número inteiro
- tente converter o valor (int), se não for int, levanta um erro
- mostre “Conversão bem-sucedida!” no else
- exiba “Programa encerrado” no finally

Exemplo:
Entrada: 25
Saída:
Conversão bem-sucedida!
Programa encerrado.
"""


#code aqui


"""
23) Crie uma função verificar_idade(idade) que levante uma exceção ValueError
caso a idade seja negativa.

Dica: use raise ValueError("mensagem")

Exemplo:
Entrada: -3
Saída: Erro: idade não pode ser negativa.
"""


#code aqui


"""
24) Acesse a página https://www.letras.mus.br/the-warning/ ou a página letras de outra banda
Use requests para baixar o conteúdo HTML e exiba o código da página.

Dica: import requests; requests.get(url).text
"""


#code aqui


"""
25) Usando BeautifulSoup, mostre o título da página da banda The Warning ou da banda escolhida por você.
"""


#code aqui


"""
26) Acesse a página de uma música no letras de alguma música que goste.
e extraia apenas o texto da letra (ignore menus, links, etc.).
Mostre apenas os primeiros 300 caracteres.

Dica: use soup.find() ou soup.find_all() com a tag correta.
tag <div> com atributo id="lyrics"
"""

#code aqui


"""
27) Baixe a letra da música que tenha muitas palavras repetidas. Conte quantas vezes aparecem essas palavras
Mostre o total de cada palavra.

Dica: use .lower() e .count("palavra")

Ex: música dumb dumb
"""


#code aqui


"""
28)Crie um programa que:

Peça ao usuário o nome, idade e cidade de 5 pessoas.
Guarde essas informações em um DataFrame do pandas com as colunas:
Nome, Idade, Cidade.
Mostre o DataFrame completo e, depois, exiba apenas a coluna de idades.

Lembre-se de levantar erros e pedir para a pessoa digitar novamente a idade se ela colocar outra coisa que não seja int.

"""


#code aqui


"""
29) Usando o DataFrame anterior, mostre:
- média das idades
- idade máxima e mínima
"""


#code aqui


"""
30) Combine as duas matérias:
- Extraia o título das músicas da banda The Warning
- Crie um DataFrame com esses títulos
- Salve em um arquivo "musicas.csv"
"""
#code aqui
