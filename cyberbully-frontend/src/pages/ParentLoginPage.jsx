// src/pages/ParentLoginPage.jsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { signInWithEmailAndPassword } from "firebase/auth";
import { auth } from '../firebase'; // import your Firebase auth instanc

const ParentLoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const navigate = useNavigate();

  const handleLogin = async () => {
  //   const savedEmail = localStorage.getItem('userEmail');
  //   const savedPassword = localStorage.getItem('userPassword');

  //   // Check if the entered credentials match the stored credentials
  //   if (email === savedEmail && password === savedPassword) {
  //     setErrorMessage('');
  //     alert('Logged in successfully');
  //     navigate('/parent-dashboard');  // Navigate to the Parent Dashboard after successful login
  //   } else {
  //     setErrorMessage('Invalid credentials');
  //   }
  // };
    setErrorMessage('');
    try {
      // Use Firebase Authentication to sign in the user
      const userCredential = await signInWithEmailAndPassword(auth, email, password);
      // If successful, you can access userCredential.user for further processing
      console.log("Logged in user:", userCredential.user);
      alert('Logged in successfully');
      navigate('/parent-dashboard');  // Navigate to the Parent Dashboard after successful login
    } catch (error) {
      console.error("Error logging in:", error);
      setErrorMessage('Invalid credentials or error logging in. Please try again.');
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <div className="w-full max-w-md p-8 bg-white rounded-lg shadow-md">
        <h2 className="text-3xl font-semibold text-center mb-6">Parent Login</h2>
        <form onSubmit={(e) => e.preventDefault()}>
          <div className="mb-4">
            <label htmlFor="email" className="block text-sm font-medium text-gray-700">Email</label>
            <input
              type="email"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="mt-1 block w-full p-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
              required
            />
          </div>

          <div className="mb-4">
            <label htmlFor="password" className="block text-sm font-medium text-gray-700">Password</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="mt-1 block w-full p-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
              required
            />
          </div>

          {errorMessage && <p className="text-red-500 text-sm">{errorMessage}</p>}

          <button
            type="button"
            onClick={handleLogin}  // Trigger login on click
            className="w-full bg-blue-500 text-white py-3 rounded-md hover:bg-blue-600 transition duration-200"
          >
            Login
          </button>
        </form>
      </div>
    </div>
  );
};

export default ParentLoginPage;
