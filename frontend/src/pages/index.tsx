import React, { useState } from 'react';
import Image from 'next/image';
import { Inter } from 'next/font/google';


const inter = Inter({ subsets: ['latin'] });

export default function Home() {
  const [useFinancialData, setUseFinancialData] = useState(false);

  const handleToggle = async () => {
    setUseFinancialData(!useFinancialData); // Toggle the state
    const response = await fetch('/api/toggle-financial-data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ enabled: !useFinancialData }),
    });

    const data = await response.json();
    console.log(data); // Log the response from the server
  };

  return (
    <main
      className={`flex min-h-screen flex-col items-center justify-between p-24 ${inter.className}`}
    >
      <label htmlFor="toggleFinancialData" className="flex items-center cursor-pointer">
        <div className="relative">
          <input
            id="toggleFinancialData"
            type="checkbox"
            className="sr-only"
            checked={useFinancialData}
            onChange={handleToggle}
          />
          <div className="block bg-gray-600 w-14 h-8 rounded-full"></div>
          <div className={`dot absolute left-1 top-1 bg-white w-6 h-6 rounded-full transition ${useFinancialData ? 'translate-x-full' : ''}`}></div>
        </div>
        <div className="ml-3 text-gray-700 font-medium">
          Use Financial Data
        </div>
      </label>
    </main>
  );
}
