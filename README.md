# Zabu Bot - Discord Bot

Zabu Bot é um bot para Discord com diversas funcionalidades, incluindo gerenciamento de servidor, sistema de boas-vindas, e cálculos básicos. Ele também oferece a habilidade de responder a mensagens personalizadas e mostrar cores em hexadecimal.

## Funcionalidades

- **Sistema de boas-vindas**: Envia uma mensagem de boas-vindas personalizada ao usuário que entrar no servidor e uma mensagem de despedida quando sair.
- **Gerenciamento de servidor**: Sincroniza comandos e notifica quando novos canais são criados.
- **Comandos de cálculos**: Permite fazer operações matemáticas básicas como soma, subtração, multiplicação e divisão.
- **Comando de cores**: Retorna o código hexadecimal de cores pré-definidas.
- **Comando de fala**: Faz o bot falar o que você escrever.
- **Saudações personalizadas**: O bot responde a um simples "Olá!" com uma mensagem amigável.

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/guigasdev/zabu-bot-discord.git
   cd zabu-bot-discord
   ```

2. Crie um ambiente virtual e ative-o:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Substitua o valor do token no arquivo `main.py` pela chave do seu bot:

   ```python
   bot.run('SEU_TOKEN_AQUI')
   ```

5. Execute o bot:

   ```bash
   python main.py
   ```

## Comandos Disponíveis

### Comandos Globais

- **!sincronizar**: Sincroniza os comandos no servidor (apenas o criador pode utilizar).
- **Boas-vindas**: Envia uma mensagem de boas-vindas quando um novo membro entra no servidor.
- **Despedida**: Notifica quando um membro sai do servidor.

### Comandos de Cálculo

- `/somar num1 num2`: Soma dois números.
- `/subtrair num1 num2`: Subtrai dois números.
- `/multiplicar num1 num2`: Multiplica dois números.
- `/dividir num1 num2`: Divide dois números.

### Cores em Hexadecimal

- `/cor`: Retorna o valor hexadecimal de uma cor específica.

### Comandos Interativos

- `/falar frase`: O bot repete a frase que você escreveu.
- `/ola`: O bot te cumprimenta de forma amigável.

## Estrutura do Projeto

- **main.py**: Arquivo principal que inicializa o bot e sincroniza os comandos.
- **cogs/**: Diretório que contém os módulos (`cogs`) com comandos específicos, como cálculos, cores e saudações.
- **media/**: Pasta onde ficam armazenadas as imagens usadas nas mensagens de boas-vindas e despedidas.

## Requisitos

- **Python 3.8+**
- **Bibliotecas**: Especificadas no arquivo `requirements.txt`

## Como Contribuir

1. Faça um fork do repositório.
2. Crie uma branch para sua modificação: `git checkout -b minha-modificacao`.
3. Faça o commit de suas alterações: `git commit -m 'Minha modificação'`.
4. Envie para o GitHub: `git push origin minha-modificacao`.
5. Abra um Pull Request.
