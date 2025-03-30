// src/firebase.js
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
    apiKey: "AIzaSyDAKfiNZAlgrjRUyFn9eksyizHCnA8FTKw",
    authDomain: "digitalwatchdog-1c2d9.firebaseapp.com",
    projectId: "digitalwatchdog-1c2d9",
    storageBucket: "digitalwatchdog-1c2d9.firebasestorage.app",
    messagingSenderId: "764210339721",
    appId: "1:764210339721:web:f619f2d045c84d804fcb58",
  };

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Get Firebase Auth instance
const auth = getAuth(app);

export { auth };