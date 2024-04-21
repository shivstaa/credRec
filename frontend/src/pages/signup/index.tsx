import { useRouter } from 'next/router';
import { useState } from 'react';
import { createUserWithEmailAndPassword } from 'firebase/auth';
import { auth } from '../../../firebase'; 

interface FirebaseError {
    code: string;
    message: string;
  }
  
  const SignupPage: React.FC = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const router = useRouter();
  
    const handleSignup = async (event: React.FormEvent) => {
      event.preventDefault();
      if (password !== confirmPassword) {
        alert("Passwords do not match!");
        return;
      }
      try {
        await createUserWithEmailAndPassword(auth, email, password);
        router.push('/'); // Redirect after successful signup
      } catch (error) {
        const firebaseError = error as FirebaseError;
        alert("Signup failed! " + firebaseError.message);
      }
    };
  
    return (
      <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
        <form onSubmit={handleSignup} className="p-6 bg-white shadow-md rounded space-y-4">
          <h1 className="text-lg font-bold text-center">Sign Up</h1>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="p-2 w-80 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Email"
            required
          />
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="p-2 w-80 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Password"
            required
          />
          <input
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            className="p-2 w-80 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Confirm Password"
            required
          />
          <button type="submit" className="w-80 p-2 bg-blue-500 text-white rounded hover:bg-blue-600">
            Sign Up
          </button>
        </form>
      </div>
    );
  };
  
  export default SignupPage;