back:
cd back
pip install -r requirements.txt
python3 app.py

front:
cd front
npm i
npm run dev

lichess bot:

python3 -m venv venv # If this fails you probably need to add Python3 to your PATH.
virtualenv venv -p python3
source ./venv/bin/activate
python3 -m pip install -r requirements.txt

virtualenv venv -p python3
source ./venv/bin/activate

ideias:

- teste vs varios níveis de stockfish com varios niveis de profundidade do bot
- mapeamento de tempo por jogada por nivel de profundidade
- embate entre 2 bots com profundidades diferentes
- estimativa de elo rating baseado no nivel de oponente que consegue vitórias
- testar novas abordagens para tentar derrotar oponentes mais fortes
  - levar em conta estrutura de peoes;
  - levar em conta controle do centro;
  - levar em conta mobilidade das peças;
  - fazer memoização de tabelas para evitar recálculos (ex em memoization-example.py)
  - implementar bibliotecas de aberturas
  - implementar tablebase de finais

parametros: análise do lichess (stockfish 17)
