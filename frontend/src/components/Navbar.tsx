import Link from 'next/link';
import React from 'react';
import { BsFillCreditCard2FrontFill } from "react-icons/bs";
import { useAuth } from "./AuthContext";
import { auth } from '../../firebase'; // Ensure this path is correct!
import { signOut } from "firebase/auth";

const Navbar: React.FC = () => {
  const { user, authenticated } = useAuth();

  const handleLogout = () => {
    signOut(auth).catch(error => console.error('Logout failed', error));
  };

  return (
    <nav className="bg-white shadow-lg">
      <div className="max-w-6xl px-4">
        <div className="flex justify-between">
          <div className="flex space-x-4">
            <Link href="/" className="flex items-center py-5 px-2 text-gray-700 hover:text-gray-900">
              <BsFillCreditCard2FrontFill className="icon"/>
              <h1 className="title">CardRec</h1>
            </Link>
          </div>
          <div className="flex items-center space-x-1">
            <Link href="/" className="py-5 px-3 text-gray-700 hover:text-gray-900">Chat</Link>
            <Link href="/history" className="py-5 px-3 text-gray-700 hover:text-gray-900">History</Link>
            {authenticated ? (
              <div className="relative">
                <button className="py-5 px-3 text-gray-700 hover:text-gray-900">{user?.email}</button>
                <div className="absolute right-0 bg-white shadow-md mt-2">
                  <button className="block px-4 py-2 text-sm text-red-600 hover:bg-gray-100" onClick={handleLogout}>
                    Logout
                  </button>
                </div>
              </div>
            ) : (
              <Link href="/login" className="py-5 px-3 text-gray-700 hover:text-gray-900">Login</Link>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
