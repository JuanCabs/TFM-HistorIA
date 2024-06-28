// src/Home.js
import React from 'react';
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCogs, faComments } from '@fortawesome/free-solid-svg-icons';
import modelo1 from './assets/modelo1.png';
import modelo2 from './assets/modelo2.png';

const Home = () => {
  return (
    <div className="container">
      <h1>Bienvenido a HistorIA.es</h1>
      <h2>Elige un formato para interactuar con la IA</h2>
      <div className="button-container">
        <div>
          
          <FontAwesomeIcon icon={faCogs} className="model-image" />
          <Link to="/models">
            <button>
              Resúmenes de manuscritos de Castellano
            </button>
          </Link>
        </div>
        <div>
        <FontAwesomeIcon icon={faComments} className="model-image" />
          <Link to="/chat">
            <button>
              Chatea con la constitución de cádiz
            </button>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Home;
