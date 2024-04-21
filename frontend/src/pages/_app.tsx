import '@/styles/globals.css';
import type { AppProps } from "next/app";
import { useRouter } from 'next/router';
import { AuthProvider } from "../components/AuthContext";
import ProtectedRoute from "../components/ProtectedRoute";

function MyApp({ Component, pageProps }: AppProps) {
  const router = useRouter();
  const noAuthRequired = ['/login', '/signup']; // List all paths that don't require authentication

  // Render the component without ProtectedRoute for login and signup paths
  const isProtectedRoute = !noAuthRequired.includes(router.pathname);

  return (
    <AuthProvider>
      {isProtectedRoute ? (
        <ProtectedRoute>
          <Component {...pageProps} />
        </ProtectedRoute>
      ) : (
        <Component {...pageProps} />
      )}
    </AuthProvider>
  );
}

export default MyApp;
