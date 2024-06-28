import React, { useState } from 'react';

const Chat = () => {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");
  const [error, setError] = useState("");

  const handlePromptSubmit = async () => {
    try {
      const res = await fetch('http://127.0.0.1:5000/prompt', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt })
      });
      if (res.ok) {
        const data = await res.text(); // Cambiado de .json() a .text() para manejar respuestas en texto plano
        setResponse(data);
        setError("");
      } else {
        throw new Error('Error sending prompt');
      }
    } catch (error) {
      console.error('Error sending prompt:', error);
      setError("Error sending prompt");
    }
  };

  const handleSuggestionClick = (suggestion) => {
    setPrompt(suggestion);
  };

  return (
    <div style={{ margin: '20px' }}>
      <h2>Chat con la Constitución de Cádiz</h2>
      <p>Puedes hacerle preguntas sobre la Constitución de Cádiz. Aquí tienes algunas sugerencias:</p>
      <ul>
        <li onClick={() => handleSuggestionClick("¿Qué derechos establece la Constitución de Cádiz?")}>
          ¿Qué derechos establece la Constitución de Cádiz?
        </li>
        <li onClick={() => handleSuggestionClick("¿Cuáles son los principios fundamentales de la Constitución de Cádiz?")}>
          ¿Cuáles son los principios fundamentales de la Constitución de Cádiz?
        </li>
        <li onClick={() => handleSuggestionClick("¿Cómo se estructura el gobierno según la Constitución de Cádiz?")}>
          ¿Cómo se estructura el gobierno según la Constitución de Cádiz?
        </li>
      </ul>

      <input
        type="text"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Escribe tu pregunta aquí..."
      />
      <button onClick={handlePromptSubmit}>Enviar pregunta</button>

      <h3>Respuesta:</h3>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <p>{response}</p>
    </div>
  );
};

export default Chat;
