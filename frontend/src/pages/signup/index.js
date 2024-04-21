import SignUp from "@/components/SignUp";
import { Inter } from "next/font/google";
const inter = Inter({ subsets: ["latin"] });
export default function SignUpPage() {
  return (
    <main
      className={`flex min-h-screen flex-col items-center justify-between p-24 ${inter.className}`}
    >
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm lg:flex">
        <SignUp></SignUp>
      </div>
    </main>
  );
}
