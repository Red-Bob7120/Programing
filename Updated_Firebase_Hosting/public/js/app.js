import { loginUser } from './auth.js';

document.addEventListener('DOMContentLoaded', () => {

    // 네비게이션 기능
    const navLinks = document.querySelectorAll('nav a');
    const sections = document.querySelectorAll('main section');

    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            console.log('Clicked link:', targetId); // 추가된 로그
            sections.forEach(section => {
                section.classList.remove('active');
                console.log('Removed active from:', section.id); // 추가된 로그
            });
            const targetSection = document.getElementById(targetId);
            targetSection.classList.add('active');
            console.log('Added active to:', targetId); // 추가된 로그
        });
    });

    // 로그인 기능
    const loginForm = document.getElementById('loginForm');
    loginForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        console.log('로그인 시도:', email, password);
        

    document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');

    // 로그인 폼 제출 이벤트 처리
    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        try {
            await loginUser(email, password); 
            alert('로그인 성공!');
            window.location.href = 'index.html'; 
        } catch (error) {
            alert('로그인 실패: ' + error.message); 
        }
    });
});

    });
    AIzaSyDpZO8RI3dGyimBugK9D5DG59jzUSTdbgM
    // Google Maps 초기화 (API 키가 필요합니다)
    let map;
    function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
            center: {lat: 37.5665, lng: 126.9780},
            zoom: 8
        });
    }
    initMap();

    // 예산 관리 기능
    const budgetForm = document.getElementById('budgetForm');
    const expenseList = document.getElementById('expenseList');
    const totalBudget = document.getElementById('totalBudget');
    let budget = 0;

    budgetForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const amount = Number(document.getElementById('amount').value);
        const description = document.getElementById('description').value;
        budget += amount;
        totalBudget.textContent = budget;
        const li = document.createElement('li');
        li.textContent = `${description}: ${amount}원`;
        expenseList.appendChild(li);
        budgetForm.reset();
    });

    // 체크리스트 기능
    const checklistForm = document.getElementById('checklistForm');
    const checklistItems = document.getElementById('checklistItems');

    checklistForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const item = document.getElementById('item').value;
        const li = document.createElement('li');
        li.innerHTML = `
            <input type="checkbox">
            <span>${item}</span>
            <button class="delete">삭제</button>
        `;
        checklistItems.appendChild(li);
        checklistForm.reset();
    });

    checklistItems.addEventListener('click', function(e) {
        if (e.target.classList.contains('delete')) {
            e.target.parentElement.remove();
        }
    });

    // 날씨 정보 기능 (API 키가 필요합니다)
    const getWeatherBtn = document.getElementById('getWeather');
    const weatherInfo = document.getElementById('weatherInfo');

    getWeatherBtn.addEventListener('click', function() {
        const city = document.getElementById('city').value;
        // 여기에 실제 날씨 API 호출 로직을 구현해야 합니다.
        weatherInfo.textContent = `${city}의 날씨 정보를 가져오는 중...`;
    });
});