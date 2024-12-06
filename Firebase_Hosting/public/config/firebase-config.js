import { initializeApp } from "https://www.gstatic.com/firebasejs/9.21.0/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/9.21.0/firebase-auth.js";
import { getDatabase } from "https://www.gstatic.com/firebasejs/9.21.0/firebase-database.js";

// Firebase 설정 객체
const firebaseConfig = {
  apiKey: "AIzaSyBdTMSJuAXluGdrQk6aAxPTszRme0YbKfA",
  authDomain: "jsproject-e6692.firebaseapp.com",
  //firebase 데이터 베이스
  projectId: "jsproject-e6692",
  storageBucket: "jsproject-e6692.appspot.com", 
  appId: "1:847960636309:web:06e0cdc6327acbcf66949c",
  measurementId: "G-DK3XLS078M"
};

// Firebase 초기화
const app = initializeApp(firebaseConfig);

// Firebase 인증 객체
export const auth = getAuth(app); 

// Firebase 데이터베이스 객체
export const database = getDatabase(app); 
