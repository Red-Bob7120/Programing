// auth.js (인증 관련 로직)
import { auth, database } from './firebase-config.js';
import { createUserWithEmailAndPassword, signInWithEmailAndPassword, signInWithPopup, GoogleAuthProvider } from "https://www.gstatic.com/firebasejs/9.2.0/firebase-auth.js";
import { ref, set, get, child } from "https://www.gstatic.com/firebasejs/9.2.0/firebase-database.js";
import { signOut } from "https://www.gstatic.com/firebasejs/9.2.0/firebase-auth.js";

// Google Auth Provider 초기화
const provider = new GoogleAuthProvider();

// 데이터 저장 함수
export const saveUserData = async (userId, name, email) => {
    try {
        await set(ref(database, 'users/' + userId), {
            username: name,
            email,
            createdAt: new Date().toISOString()
        });
        console.log('저장 성공');
    } catch (err) {
        console.error('저장 실패:', err);
        throw new Error(err.message);
    }
};

// 회원가입 로직
export const registerUser = async (name, email, password) => {
    try {
        const userCredential = await createUserWithEmailAndPassword(auth, email, password);
        const userId = userCredential.user.uid;
        await saveUserData(userId, name, email);
        console.log('회원가입 성공');
        alert('회원가입에 성공했습니다!'); // 성공 알림 추가
        return userCredential.user;
    } catch (err) {
        console.error('회원가입 실패:', err.message);
        throw new Error(err.message);
    }
};

// 로그인 로직
export const loginUser = async (email, password) => {
    try {
        const userCredential = await signInWithEmailAndPassword(auth, email, password);
        console.log('로그인 성공');
        return userCredential.user;
    } catch (err) {
        console.error('로그인 실패:', err.message);
        throw new Error(err.message);
    }
};

// Google 로그인 로직
export const googleLogin = async () => {
    try {
        const result = await signInWithPopup(auth, provider);
        const user = result.user;
        if (user) {
            await saveUserData(user.uid, user.displayName || user.email, user.email);
            console.log('Google 로그인 성공');
            return user;
        } else {
            throw new Error('유저 정보가 없습니다.');
        }
    } catch (err) {
        console.error('Google 로그인 실패:', err.message);
        throw new Error(err.message);
    }
};

export const initAuthStateListener = () => {
    auth.onAuthStateChanged((user) => {
        const authButtons = document.getElementById('auth-buttons');
        const userInfo = document.getElementById('user-info');
        const logoutBtn = document.getElementById('logout-btn');
        
        if (user) {
            // 로그인 상태
            authButtons.style.display = 'none';
            userInfo.style.display = 'inline';
            logoutBtn.style.display = 'inline';
            userInfo.textContent = `${user.email}님 환영합니다!`;
        } else {
            // 로그아웃 상태
            authButtons.style.display = 'block';
            userInfo.style.display = 'none';
            logoutBtn.style.display = 'none';
        }
    });
};


// 로그아웃 함수 추가
export const logout = async () => {
    try {
        await signOut(auth);
        console.log('로그아웃 성공');
        window.location.href = 'index.html';
    } catch (err) {
        console.error('로그아웃 실패:', err.message);
        alert('로그아웃 실패: ' + err.message);
    }
};