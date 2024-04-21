import React, { ReactNode } from 'react';
import { useRouter } from "next/router";
import { useAuth } from "./AuthContext";

interface ProtectedRouteProps {
  children: ReactNode;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ children }) => {
  const authContext = useAuth();
  const router = useRouter();

  React.useEffect(() => {
    console.log("Checking auth state for routing:", authContext);
    if (!authContext?.loading && !authContext?.authenticated) {
      console.log("Redirecting to login");
      router.push('/login');
    }
  }, [authContext, router]);

  if (authContext?.loading) {
    console.log("Still loading auth state");
    return <div>Loading...</div>;
  }

  if (!authContext?.authenticated) {
    console.log("Not authenticated, should redirect");
    return <div>Redirecting...</div>;
  }

  return <>{children}</>;
};

export default ProtectedRoute;
