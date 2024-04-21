import Link from 'next/link';
import Image from 'next/image';
import React from 'react';
import { BsFillCreditCard2FrontFill } from "react-icons/bs";

const Navbar: React.FC = () => {
  return (
    <nav className="bg-white shadow-lg">
      <div className="max-w-6xl px-4">
        <div className="flex justify-between">
          <div className="flex space-x-4">
            {/* Logo and home link */}
            <div>
            <Link href="/" className="flex items-center py-5 px-2 text-gray-700 hover:text-gray-900">
                <span className="iconWithText">
                  <BsFillCreditCard2FrontFill className="icon"/>
                  <h1 className="title">CardRec</h1>
                </span>
              </Link>
            </div>
          </div>

          {/* Primary Nav Links */}
          <div className="flex items-center space-x-1">
            <Link href="/" className="py-5 px-3 text-gray-700 hover:text-gray-900">Chat</Link>
            <Link href="/history" className="py-5 px-3 text-gray-700 hover:text-gray-900">History</Link>
            <Link className="py-5 px-3 text-gray-700 hover:text-gray-900" href="/login">Login</Link>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
