// auth.js (인증 관련 로직)
import { auth, database } from './firebase-config.js';
<<<<<<< HEAD
import { createUserWithEmailAndPassword, signInWithEmailAndPassword, signInWithPopup, GoogleAuthProvider } from "https://www.gstatic.com/firebasejs/9.x.x/firebase-auth.js";
=======
import {
    createUserWithEmailAndPassword,
    signInWithEmailAndPassword,
    signInWithPopup,
    GoogleAuthProvider,
} from "https://www.gstatic.com/firebasejs/9.21.0/firebase-auth.js";
>>>>>>> 171f7e1 (수정)
import { ref, set, get, child } from "https://www.gstatic.com/firebasejs/9.21.0/firebase-database.js";

// Google Auth Provider 초기화
const provider = new GoogleAuthProvider();

// 데이터 저장 함수
export const saveUserData = (userId, name, email) => {
    set(ref(database, 'users/' + userId), {
        username: name,
        email,
        createdAt: new Date().toISOString() // 저장 데이터에 생성 시간 추가 
    }).then(() => console.log('저장 성공'))
      .catch(err => console.error('저장 실패:', err));
};

// 데이터 불러오기 함수
export const getUserData = (userId) => {
    get(child(ref(database), `users/${userId}`))
        .then(snapshot => {
            if (snapshot.exists()) {
                console.log(snapshot.val());
            } else {
                console.log("데이터 없음");
                alert("데이터가 없습니다.");
            }
        })
        .catch(err => {
            console.error('불러오기 실패:', err);
            alert('데이터 불러오기 실패: ' + err.message);
        });
};

// 로그인 로직 (app.js에서 호출)
export const loginUser = async (email, password) => {
    try {
        await signInWithEmailAndPassword(auth, email, password);
        console.log('로그인 성공');
        window.location.replace('dashboard.html'); // 로그인 성공 시 대시보드로 이동 
    } catch (err) {
        console.error('로그인 실패:', err.message);
        alert('로그인 실패: ' + err.message);
    }
};

// 회원가입 로직 (app.js에서 호출)
export const registerUser = async (email, password) => {
    try {
        await createUserWithEmailAndPassword(auth, email, password);
        const userId = auth.currentUser ? auth.currentUser.uid : null;
        if (userId) {
            saveUserData(userId, email, ""); // 회원가입 후 데이터 저장 
            window.location.replace('dashboard.html'); // 회원가입 후 대시보드로 이동 
        } else {
            console.error('유저 정보가 없습니다.');
        }
    } catch (err) {
        console.error('회원가입 실패:', err.message);
        alert('회원가입 실패: ' + err.message);
    }
};

// Google 로그인 로직
export const googleLogin = async () => {
    try {
        const result = await signInWithPopup(auth, provider);
        const user = result.user;
        const userId = user ? user.uid : null;
        if (userId) {
            saveUserData(userId, user.displayName, user.email); // Google 로그인 후 데이터 저장 
            window.location.replace('dashboard.html'); // Google 로그인 성공 시 대시보드로 이동 
        } else {
            console.error('유저 정보가 없습니다.');
        }
    } catch (err) {
        console.error('Google 로그인 실패:', err.message);
        alert('Google 로그인 실패: ' + err.message);
    }
};
