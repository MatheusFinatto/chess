<h1 align="center">🚀 Chess Artificial Intelligence - Final Thesis 🎓</h1>

<p align="center">
  This project is the result of my Computer Science Final Thesis. It is a <strong>Chess AI</strong> based on the <strong>Minimax</strong> algorithm with <strong>Alpha-Beta Pruning</strong>, integrated with:
</p>

<ul>
  <li>🌐 <strong>Lichess Bot</strong> to play against Stockfish directly on <a href="https://lichess.org/" target="_blank">Lichess</a>.</li>
  <li>👤 <strong>Front-End Interface</strong> for human matches and general user access.</li>
  <li>⚙️ <strong>Back-End</strong> to handle logic and integration (Python environment).</li>
</ul>

<hr />

<h2>📂 Project Structure</h2>
<ul>
  <li><strong><code>back/</code></strong>: Code for the back-end of the application.</li>
  <li><strong><code>front/</code></strong>: Code for the front-end interface.</li>
  <li><strong><code>lichess-bot/</code></strong>: Code for the bot that interacts with Lichess.</li>
</ul>

<hr />

<h2>💻 How to Run the Project</h2>
<p>(From a fresh Ubuntu VM with the repository cloned)</p>

<h3>1️⃣ Setting Up the Back-End</h3>
<pre>
<code>
cd back

sudo apt install python3.12-venv

python3 -m venv back

source ./back/bin/activate

pip install -r requirements.txt

python3 app.py
</code>
</pre>
<p>The server will be available to manage matches.</p>

<h3>2️⃣ Setting Up the Front-End</h3>
<pre>
<code>
cd front

sudo apt install npm

npm i

npm run dev
</code>
</pre>
<p>Open your browser and go to <a href="http://localhost:5173" target="_blank">localhost:5173</a> to access the interface.</p>

<h3>3️⃣ Setting Up the Lichess Bot</h3>
A login and password are required to start the bot in the Lichess environment!  
Therefore, this part is not publicly accessible.
<pre>
<code>
python3 -m venv bot

source ./bot/bin/activate

pip install -r requirements.txt

python lichess-bot.py
</code>
</pre>
<p>The bot will be activated and start playing on <a href="https://lichess.org/" target="_blank">Lichess</a>.</p>

<hr />

<h2>🧠 Technologies Used</h2>
<ul>
  <li><strong>Back-End:</strong> Python, Flask.</li>
  <li><strong>Front-End:</strong> React.js, Vite.</li>
  <li><strong>Algorithms:</strong> Minimax, Alpha-Beta Pruning.</li>
  <li><strong>Integrations:</strong> Lichess API.</li>
</ul>
