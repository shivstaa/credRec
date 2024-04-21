import React, { ReactNode, useState } from 'react';
import { useRouter } from "next/router";
import { useAuth } from "./AuthContext";

interface ProtectedRouteProps {
  children: ReactNode;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ children }) => {
  const authContext = useAuth();
  const router = useRouter();
  const [redirecting, setRedirecting] = useState(false);  // State to manage redirection delay

  React.useEffect(() => {
    console.log("Checking auth state for routing:", authContext);
    if (!authContext?.loading && !authContext?.authenticated) {
      console.log("Not authenticated, preparing to redirect");
      setRedirecting(true);  // Set redirecting to true to show the redirect message
      setTimeout(() => {
        console.log("Redirecting to login");
        router.push('/login');
      }, 3000);  // Wait for 3 seconds before actually redirecting
    }
  }, [authContext, router]);

  if (authContext?.loading) {
    console.log("Still loading auth state");
    return <div>Loading...</div>;
  }

  if (redirecting) {
    console.log("Not authenticated, should redirect");
    return <div>Redirecting...</div>;  // Display this while waiting to redirect
  }

  return <>{children}</>;
};

export default ProtectedRoute;
