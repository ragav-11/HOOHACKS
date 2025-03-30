// src/services/auth.js
export const signUp = async (email, password) => {
    try {
      // Use localStorage for now to store the user's credentials (for simplicity in this case)
      localStorage.setItem('userEmail', email);
      localStorage.setItem('userPassword', password);
    } catch (error) {
      throw new Error('Error saving credentials');
    }
  };
  