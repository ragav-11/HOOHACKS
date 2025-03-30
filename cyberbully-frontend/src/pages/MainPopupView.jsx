import React, { useState, useEffect } from 'react';
import HomePage from './HomePage';
import ParentLoginPage from './ParentLoginPage';
import ParentDashboard from './ParentDashboard';

const MainPopupView = () => {
  const [selectedTab, setSelectedTab] = useState('home'); // 'home' or 'parent'
  const [parentLoggedIn, setParentLoggedIn] = useState(false);

  useEffect(() => {
    const isParentLoggedIn = localStorage.getItem('parentLoggedIn') === 'true';
    setParentLoggedIn(isParentLoggedIn);
  }, []);

  const handleParentLogin = () => {
    setParentLoggedIn(true);
    localStorage.setItem('parentLoggedIn', 'true');
  };

  const handleParentLogout = () => {
    setParentLoggedIn(false);
    localStorage.setItem('parentLoggedIn', 'false');
  };

  let content;
  if (selectedTab === 'home') {
    content = <HomePage toggleTab={setSelectedTab} />;
  } else {
    content = parentLoggedIn ? (
      <ParentDashboard onLogout={handleParentLogout} />
    ) : (
      <ParentLoginPage onLogin={handleParentLogin} />
    );
  }

  return (
    <div className="flex flex-col h-full">
      <div className="flex-grow overflow-y-auto">{content}</div>
      <div className="flex justify-around border-t bg-white p-2">
        <button
          onClick={() => setSelectedTab('home')}
          className={`w-1/2 py-2 font-semibold ${
            selectedTab === 'home'
              ? 'text-blue-600 border-b-4 border-blue-600'
              : 'text-gray-600'
          }`}
        >
          Home
        </button>
        <button
          onClick={() => setSelectedTab('parent')}
          className={`w-1/2 py-2 font-semibold ${
            selectedTab === 'parent'
              ? 'text-blue-600 border-b-4 border-blue-600'
              : 'text-gray-600'
          }`}
        >
          Parental Control
        </button>
      </div>
    </div>
  );
};

export default MainPopupView;