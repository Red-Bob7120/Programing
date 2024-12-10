//firebase 관련 firebase-config.js

import { initializeApp } from "https://www.gstatic.com/firebasejs/9.2.0/firebase-app.js";
import { getAuth, signInWithPopup, GoogleAuthProvider, signInWithEmailAndPassword, createUserWithEmailAndPassword } from 'https://www.gstatic.com/firebasejs/9.2.0/firebase-auth.js';
import { getDatabase, ref, set, get, child } from 'https://www.gstatic.com/firebasejs/9.2.0/firebase-database.js';

const firebaseConfig = {
    apiKey: "AIzaSyBdTMSJuAXluGdrQk6aAxPTszRme0YbKfA",
    authDomain: "jsproject-e6692.firebaseapp.com",
    projectId: "jsproject-e6692",
    storageBucket: "jsproject-e6692.appspot.com",
    appId: "1:847960636309:web:06e0cdc6327acbcf66949c",
    measurementId: "G-DK3XLS078M"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const database = getDatabase(app);

export { auth, database };

// 데이터 저장 함수
export const saveUserData = (userId, name, email) => {
    return set(ref(database, 'users/' + userId), {
        username: name,
        email,
        createdAt: new Date().toISOString()
    });
};

// Email 회원가입
export const signupEmail = async (email, password) => {
    try {
        const userCredential = await createUserWithEmailAndPassword(auth, email, password);
        const user = userCredential.user;
        await saveUserData(user.uid, email, email);
        return userCredential;
    } catch (error) {
        throw error;
    }
};

// Email 로그인
export const loginEmail = (email, password) => {
    return signInWithEmailAndPassword(auth, email, password);
};

// Google 로그인
const provider = new GoogleAuthProvider();
export const loginGoogle = async () => {
    try {
        const result = await signInWithPopup(auth, provider);
        const user = result.user;
        await saveUserData(user.uid, user.displayName || user.email, user.email);
        return result;
    } catch (error) {
        throw error;
    }
};

// 로그인 상태에 따라 변경
export const authStateListener = (callback) => {
    auth.onAuthStateChanged((user) => {
        callback(user);
    });
};

