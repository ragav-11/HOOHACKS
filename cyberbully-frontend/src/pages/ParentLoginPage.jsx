import React, { useState } from 'react';
import { signInWithEmailAndPassword } from "firebase/auth";
import { auth } from '../firebase';

const ParentLoginPage = ({ onLogin }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const handleLogin = async () => {
    setErrorMessage('');
    try {
      const userCredential = await signInWithEmailAndPassword(auth, email, password);
      console.log("Logged in user:", userCredential.user);
      alert('Logged in successfully');
      onLogin();
    } catch (error) {
      console.error("Error logging in:", error);
      setErrorMessage('Invalid credentials or error logging in. Please try again.');
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gradient-to-br from-blue-100 to-indigo-100 px-4">
      <div className="w-full max-w-md p-8 bg-white rounded-xl shadow-xl">
        <h2 className="text-4xl font-bold text-center text-gray-800 mb-6">👨‍👩‍👧 Parent Login</h2>

        <form onSubmit={(e) => e.preventDefault()} className="space-y-4">
          <div>
            <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-1">Email</label>
            <input
              type="email"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-400 focus:border-indigo-400 transition"
              placeholder="you@example.com"
              required
            />
          </div>

          <div>
            <label htmlFor="password" className="block text-sm font-medium text-gray-700 mb-1">Password</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-400 focus:border-indigo-400 transition"
              placeholder="••••••••"
              required
            />
          </div>

          {errorMessage && (
            <p className="text-red-500 text-sm">{errorMessage}</p>
          )}

          <button
            type="button"
            onClick={handleLogin}
            className="w-full bg-indigo-500 text-white py-3 rounded-lg hover:bg-indigo-600 transition duration-200 font-semibold"
          >
            Login
          </button>
        </form>
      </div>
    </div>
  );
};

export default ParentLoginPage;