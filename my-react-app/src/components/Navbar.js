import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css'; // Asegúrate de tener este archivo de estilos

const Navbar = () => {
  return (
    <nav className="navbar">
      <ul className="navbar-menu">
        <li>
          <Link to="/" className="navbar-link">
            <i className="fas fa-home"></i> Home
          </Link>
        </li>
        <li>
          <Link to="/models" className="navbar-link">
            <i className="fas fa-file-upload"></i> Manuscritos
          </Link>
        </li>
        <li>
          <Link to="/chat" className="navbar-link">
            <i className="fas fa-comments"></i> Chat
          </Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
