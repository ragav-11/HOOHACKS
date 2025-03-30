// src/App.js
import React from 'react';
import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import SignUpPage from './pages/SignUpPage';
import HomePage from './pages/HomePage';
import ParentLoginPage from './pages/ParentLoginPage';
import ParentDashboard from './pages/ParentDashboard';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<SignUpPage />} />
        <Route path="/home" element={<HomePage />} />
        <Route path="/parent-login" element={<ParentLoginPage />} />
        <Route path="/parent-dashboard" element={<ParentDashboard />} />
      </Routes>
    </Router>
  );
};

export default App;
