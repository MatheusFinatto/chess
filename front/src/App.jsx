import { Chess } from "chess.js";
import { useState } from "react";
import { Chessboard } from "react-chessboard";

export default function PlayRandomMoveEngine() {
  const [game, setGame] = useState(new Chess());
  const [currentTimeout, setCurrentTimeout] = useState();

  function safeGameMutate(modify) {
    setGame((g) => {
      const update = { ...g };
      modify(update);
      return update;
    });
  }

  if (game.game_over() || game.in_draw())
    return (
      <>
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            height: "100vh",
            width: "100vw",
            justifyContent: "center",
            alignItems: "center",
            fontSize: "5rem",
          }}
        >
          Game over
          <button
            onClick={() => setGame(new Chess())}
            style={{
              fontSize: "2rem",
              borderRadius: "0.5rem",
              backgroundColor: "#282c34",
              color: "white",
              padding: "0.5rem 1rem",
              border: "none",
              cursor: "pointer",
              transition: "background-color 0.3s ease",
              position: "relative",
              top: 30,
            }}
          >
            Restart
          </button>
        </div>
      </>
    );

  async function calculateMove() {
    fetch("http://localhost:5000/move", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ fen: game.fen() }),
    }).then((response) => {
      console.log(
        "🚀 ~ file: App.jsx:61 ~ calculateMove ~ response:",
        response
      );

      response.json().then((data) => {
        console.log("🚀 ~ file: App.jsx:67 ~ response.json ~ data:", data);
        safeGameMutate((game) => {
          game.move(data.move);
        });
      });
    });
  }

  function makeMove() {
    const possibleMoves = game.moves();

    if (game.game_over() || game.in_draw() || possibleMoves.length === 0)
      return;

    calculateMove();
  }

  function onDrop(sourceSquare, targetSquare, piece) {
    const gameCopy = { ...game };
    const move = gameCopy.move({
      from: sourceSquare,
      to: targetSquare,
      promotion: piece[1].toLowerCase() ?? "q",
    });
    setGame(gameCopy);

    // illegal move
    if (move === null) return false;

    // store timeout so it can be cleared on undo/reset so computer doesn't execute move
    const newTimeout = setTimeout(makeMove, 200);
    setCurrentTimeout(newTimeout);
    return true;
  }

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        marginTop: "2rem",
      }}
    >
      <div
        style={{
          width: "95%",
          height: "95%",
          maxHeight: "1000px",
          maxWidth: "1000px",
        }}
      >
        <Chessboard position={game.fen()} onPieceDrop={onDrop} />
        <br />
        <div
          style={{
            textAlign: "center",
            display: "flex",
            gap: "1rem",
            justifyContent: "center",
          }}
        >
          <button
            onClick={() => setGame(new Chess())}
            style={{
              fontSize: "2rem",
              borderRadius: "0.5rem",
              backgroundColor: "#282c34",
              color: "white",
              padding: "0.5rem 1rem",
              border: "none",
              cursor: "pointer",
              transition: "background-color 0.3s ease",
            }}
          >
            Restart
          </button>
          <button
            onClick={() => {
              safeGameMutate((game) => {
                game.undo();
                game.undo();
              });
              clearTimeout(currentTimeout);
            }}
            style={{
              fontSize: "2rem",
              borderRadius: "0.5rem",
              backgroundColor: "#282c34",
              color: "white",
              padding: "0.5rem 1rem",
              border: "none",
              cursor: "pointer",
              transition: "background-color 0.3s ease",
            }}
          >
            Undo
          </button>
        </div>
      </div>
    </div>
  );
}
