import Link from 'next/link';
import React, { useState } from 'react';
import { BsFillCreditCard2FrontFill } from "react-icons/bs";
import { useAuth } from "./AuthContext";
import { auth } from '../../firebase'; // Ensure this path is correct!
import { signOut } from "firebase/auth";
import Grid from '@mui/material/Grid';
import { Box } from '@mui/material';
import { ThemeProvider } from '@emotion/react';
import theme from '@/components/Theme';

const Navbar: React.FC = () => {
  const { user, authenticated } = useAuth();
  const [dropdownOpen, setDropdownOpen] = useState(false);  // State to manage dropdown visibility

  const handleLogout = () => {
    signOut(auth).catch(error => console.error('Logout failed', error));
  };

  const toggleDropdown = () => setDropdownOpen(!dropdownOpen);  // Toggle function

  return (
    <ThemeProvider theme={theme}>
          <nav className="bg-purple-800 shadow-lg text-white	">
      <div className="w-full px-4">
        <div className="flex justify-between">
          <Box className="flex items-center">
            <Link href="/" className="flex items-center py-5 px-2 text-white hover:text-gray-900">
              <BsFillCreditCard2FrontFill className="icon"/>
              <h1 className="title" >CardRec</h1>
            </Link>
          </Box>
          <div className="flex items-center"> {/* New flex container */}
    <Grid container>
      <Grid className="flex items-center justify-end">
        <Link href="/" className="py-5 px-3 text-white hover:text-gray-900">Chat</Link>
      </Grid>
      <Grid item className="flex items-center justify-end">
        <Link href="/history" className="py-5 px-3 text-white hover:text-gray-900">History</Link>
      </Grid>
      <Grid item className="flex items-center justify-end">
        <Box display="flex" justifyContent="flex-end">
          {authenticated ? (
            <div className="relative">
              <button onClick={toggleDropdown} className="py-5 px-3 text-white hover:text-900">
                {user?.email}
              </button>
              {dropdownOpen && (
                <div className="absolute right-0 bg-white shadow-md mt-2">
                  <button className="block px-4 py-2 text-sm text-red-600 hover:bg-gray-100" onClick={handleLogout}>
                    Logout
                  </button>
                </div>
              )}
            </div>
          ) : (
            <Link href="/login" className="py-5 px-3 text-white hover:text-gray-900">Login</Link>
          )}
        </Box>
      </Grid>
    </Grid>
  </div>
</div>
</div>
    </nav>
    </ThemeProvider>
  );
};

export default Navbar;
