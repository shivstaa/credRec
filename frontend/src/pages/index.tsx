import React, { useEffect, useState } from 'react';
import Cookies from 'js-cookie';
import { generateTransactions } from '../../fakedata';

export default function Home() {
  const [isEnabled, setIsEnabled] = useState<boolean>(() => Cookies.get('isEnabled') === 'true');
  const [responseMessage, setResponseMessage] = useState<string>('');
  const [creditCardRecommendations, setCreditCardRecommendations] = useState<string>('');

  useEffect(() => {
    Cookies.set('isEnabled', String(isEnabled), { expires: 31 });
  }, [isEnabled]);

  const handleToggle = async () => {
    setIsEnabled(current => !current);
    if (!isEnabled) {
      const transactions = generateTransactions();
      try {
        const response = await fetch('http://localhost:5000/api/receive-transactions', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(transactions),
        });
        const data = await response.json();
        if (data && data.valid) {
          setCreditCardRecommendations(data.response);
        } else {
          setCreditCardRecommendations('');
        }
        setResponseMessage(data.message);
      } catch (error) {
        console.error('Error sending data:', error);
        setResponseMessage('Failed to process transactions.');
      }
    } else {
      setResponseMessage('');
      setCreditCardRecommendations('');
    }
  };

  return (
    <main className="p-4">
      <h1 className="text-2xl font-bold mb-4">Enable Transaction Data</h1>
      <div>
        <label className="flex items-center cursor-pointer">
          <div className="relative">
            <input type="checkbox" checked={isEnabled} onChange={handleToggle} className="sr-only" />
            <div className={`block w-14 h-8 rounded-full ${isEnabled ? 'bg-blue-500' : 'bg-gray-600'}`}></div>
            <div className={`dot absolute left-1 top-1 bg-white w-6 h-6 rounded-full transition-transform duration-300 ease-in-out ${isEnabled ? 'transform translate-x-full' : ''}`}></div>
          </div>
          <div className="ml-3 text-gray-700 font-medium">Toggle Financial Data</div>
        </label>
      </div>
      {responseMessage && (
        <div className="mt-4">
          <p>Response:</p>
          <p>{responseMessage}</p>
        </div>
      )}
      {creditCardRecommendations && (
        <div className="mt-4 bg-gray-100 p-4 rounded-lg">
          <p className="font-bold">Credit Card Recommendations:</p>
          <p className="whitespace-pre-wrap">{creditCardRecommendations}</p>
        </div>
      )}
    </main>
  );
}
