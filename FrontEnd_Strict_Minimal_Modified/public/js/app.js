//메인 로직 담당 app.js 파일
import { loginEmail, signupEmail,loginGoogle } from './firebase-config.js';
const buttons = document.getElementById('buttons');
import { logout } from './js/auth.js';

//Email 로그인, 회원가입 구현
buttons.addEventListener('click', (e) => {
    e.preventDefault();
    if (e.target.id == 'signin') {
      loginEmail(email.value, pw.value).then((result) => {
        console.log(result);
        const user = result.user;
        loginSuccess(user.email, user.uid);
      });
    } else if (e.target.id == 'signup') {
      signupEmail(email.value, password.value) //
        .then((result) => {
          const user = result.user;
          loginSuccess(user.email, user.uid);
        })
        .catch((error) => console.log(error));
    }
  });

  google.addEventListener('click', (e) => {
    loginGoogle().then((result) => {
      console.log(result);
      const user = result.user;
      loginSuccess(user.email, user.uid);
    });
  });
  //로그인 성공시 UI 변경
  const loginSuccess = (email, uid) => {
    const login_area = document.getElementById('login-area');
    login_area.innerHTML = `<h2>Login 성공!</h2><div>uid: ${uid}</div><div>email: ${email}</div>`;
  };


  import { auth } from './firebase-config.js';

  document.addEventListener('DOMContentLoaded', () => {
      const userInfo = document.getElementById('user-info');
      const authButtons = document.getElementById('auth-buttons');
      
      auth.onAuthStateChanged((user) => {
          if (user) {
              // 로그인 상태
              userInfo.textContent = `${user.email}님 환영합니다`;
              userInfo.style.display = 'inline';
              authButtons.style.display = 'none';
          } else {
              // 로그아웃 상태
              userInfo.style.display = 'none';
              authButtons.style.display = 'block';
          }
      });
  });

  document.getElementById('logout-btn').addEventListener('click', logout);
// Checklist functionality (minimal addition without touching the original structure)
document.addEventListener('DOMContentLoaded', () => {
    const checklistForm = document.getElementById('checklist-form');
    const checklistItems = document.getElementById('checklist-items');

    if (checklistForm && checklistItems) {
        checklistForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const item = document.getElementById('checklist-item').value;

            if (!item) {
                alert('Please enter an item!');
                return;
            }

            try {
                const userId = "exampleUserId"; // Replace with actual user ID logic
                const checklistRef = ref(database, `users/${userId}/checklist`);
                const newItemRef = push(checklistRef);
                await set(newItemRef, { item });
                checklistItems.innerHTML += `<li>${item}</li>`;
            } catch (error) {
                console.error('Error adding checklist item:', error);
                alert('Failed to add item.');
            }
        });
    }
});

// Trip saving functionality (minimal addition without touching the original structure)
document.addEventListener('DOMContentLoaded', () => {
    const saveTripButton = document.getElementById('save-trip-btn');
    const tripList = document.getElementById('trip-list');

    if (saveTripButton && tripList) {
        saveTripButton.addEventListener('click', async () => {
            const destination = document.getElementById('destination').value;
            const date = document.getElementById('travel-date').value;

            if (!destination || !date) {
                alert('Please enter a destination and a date!');
                return;
            }

            try {
                const userId = "exampleUserId"; // Replace with actual user ID logic
                const tripRef = ref(database, `users/${userId}/trips`);
                const newTripRef = push(tripRef);
                await set(newTripRef, { destination, date });
                tripList.innerHTML += `<li>${destination} - ${date}</li>`;
            } catch (error) {
                console.error('Error saving trip:', error);
                alert('Failed to save trip.');
            }
        });
    }
});
