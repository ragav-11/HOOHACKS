import React, { useEffect, useState } from 'react';
import SignUpPage from './pages/SignUpPage';
import MainPopupView from './pages/MainPopupView';

function App() {
  const [hasSignedUp, setHasSignedUp] = useState(null); // null = loading

  useEffect(() => {
    const signedUp = localStorage.getItem('hasSignedUp') === 'true';
    setHasSignedUp(signedUp);
  }, []);

  if (hasSignedUp === null) {
    // Prevent flickering on load
    return <div className="p-4 text-center">Loading...</div>;
  }

  return hasSignedUp ? (
    <div className="h-[500px] w-[400px]">
      <MainPopupView />
    </div>
  ) : (
    <div className="h-[500px] w-[400px]">
      <SignUpPage onSignUpComplete={() => setHasSignedUp(true)} />
    </div>
  );
}

export default App;