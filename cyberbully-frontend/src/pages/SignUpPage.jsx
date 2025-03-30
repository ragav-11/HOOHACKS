import React, { useState, useEffect } from 'react';
import { auth } from '../firebase';
import { createUserWithEmailAndPassword, sendEmailVerification } from 'firebase/auth';
import bulldog from '../assets/bulldog.png';

const SignUpPage = ({ onSignUpComplete }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  useEffect(() => {
    const isSignedUp = localStorage.getItem('hasSignedUp');
    if (isSignedUp === 'true') {
      onSignUpComplete(); // Auto-transition if already signed up
    }
  }, [onSignUpComplete]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (password !== confirmPassword) {
      setErrorMessage("Passwords don't match!");
      return;
    }

    try {
      const userCredential = await createUserWithEmailAndPassword(auth, email, password);
      await sendEmailVerification(userCredential.user);
      console.log("User created:", userCredential.user);
      localStorage.setItem('hasSignedUp', 'true');
      onSignUpComplete();
    } catch (error) {
      console.error("Error signing up:", error);
      setErrorMessage(error.message || 'Error signing up, please try again!');
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gradient-to-r from-blue-400 to-indigo-600">
      <div className="w-full max-w-md p-6 bg-white rounded-xl shadow-xl space-y-6">
      <h2 className="text-3xl font-bold text-center text-gray-800 flex items-center justify-center gap-3">
        <img src={bulldog} alt="Bulldog logo" className="w-10 h-10" />
        Create Your Account
      </h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label htmlFor="email" className="block text-sm font-medium text-gray-700">Email</label>
            <input
              type="email"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="mt-1 block w-full p-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-400"
              placeholder="you@example.com"
              required
            />
          </div>

          <div>
            <label htmlFor="password" className="block text-sm font-medium text-gray-700">Password</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="mt-1 block w-full p-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-400"
              placeholder="••••••••"
              required
            />
          </div>

          <div>
            <label htmlFor="confirm-password" className="block text-sm font-medium text-gray-700">Confirm Password</label>
            <input
              type="password"
              id="confirm-password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              className="mt-1 block w-full p-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-400"
              placeholder="••••••••"
              required
            />
          </div>

          {errorMessage && (
            <p className="text-red-500 text-sm text-center">{errorMessage}</p>
          )}

          <button
            type="submit"
            className="w-full bg-blue-500 text-white py-3 rounded-md hover:bg-blue-600 transition duration-200"
          >
            Sign Up
          </button>
        </form>
      </div>
    </div>
  );
};

export default SignUpPage;