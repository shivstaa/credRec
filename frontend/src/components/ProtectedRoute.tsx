
import React, { ReactNode, useState, useEffect } from 'react';
import { useRouter } from "next/router";
import { useAuth } from "./AuthContext";


interface ProtectedRouteProps {
  children: ReactNode;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ children }) => {
  const { user, authenticated, loading } = useAuth();
  const router = useRouter();
  const [redirecting, setRedirecting] = useState(false);  // State to manage redirection delay

  useEffect(() => {
    // Check if the user is trying to access a restricted route other than the root
    if (!loading && !authenticated && router.pathname !== '/') {
      console.log("Not authenticated, preparing to redirect");
      setRedirecting(true);
      setTimeout(() => {
        console.log("Redirecting to login");
        router.push('/login');
      }, 3000);  // Delay the redirection to give feedback to the user
    } else {
      setRedirecting(false);  // Ensure redirecting is false when user is authenticated or on the root path
    }
  }, [authenticated, loading, router]);

  if (loading) {
    console.log("Still loading auth state");
    return <div>Loading...</div>;
  }

  if (redirecting) {
    console.log("Not authenticated and not on root path, redirecting soon");
    return <div>Redirecting to login...</div>;
  }

  return <>{children}</>;
};

export default ProtectedRoute;
