import React, { useState } from 'react';
import Image from 'next/image';
import { Inter } from 'next/font/google';
import { generateTransactions } from '../../fakedata';


const inter = Inter({ subsets: ['latin'] });

export default function Home() {
  const [isEnabled, setIsEnabled] = useState(false);
  const [responseMessage, setResponseMessage] = useState('');

  const handleToggle = async () => {
    setIsEnabled(current => !current);
    if (!isEnabled) {
      const transactions = generateTransactions();
      try {
        const response = await fetch('http://localhost:5000/api/receive-transactions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(transactions),
        });
        const data = await response.json();
        setResponseMessage(data.message); // Set the response message from the backend
      } catch (error) {
        console.error('Error sending data:', error);
        setResponseMessage('Failed to process transactions.');
      }
    } else {
      setResponseMessage(''); // Clear message when toggled off
    }
  };

  return (
    <main>
      <h1>Enable Transaction Data</h1>
      <label>
        Toggle Financial Data:
        <input type="checkbox" checked={isEnabled} onChange={handleToggle} />
      </label>
      {responseMessage && <div><p>Response:</p><p>{responseMessage}</p></div>} {/* Display the response message */}
    </main>
  );
}