import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
    apiKey: "AIzaSyAEWjrUWiKDY4RXy1WbB2waoh03wHz9OC4",
    authDomain: "credrec-b6e05.firebaseapp.com",
    projectId: "credrec-b6e05",
    storageBucket: "credrec-b6e05.appspot.com",
    messagingSenderId: "83988035294",
    appId: "1:83988035294:web:9761c2b77518d45bca744f",
    measurementId: "G-FVRVYD8M6K"
  };

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

export { auth };
