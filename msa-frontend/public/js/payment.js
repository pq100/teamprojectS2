// 페이지 로드 시 주차 상태 조회
async function fetchParkingStatus() {
    try {
        const response = await fetch('http://localhost:8000/index/payment'); // 실제 API 엔드포인트로 변경 필요
        const data = await response.json();

        const parkingStatusContainer = document.getElementById('parking-status-container');
        parkingStatusContainer.innerHTML = ''; // 초기화

        data.forEach(slot => {
            const slotDiv = document.createElement('div');
            slotDiv.className = 'parking-slot ' + (slot.occupied ? 'occupied' : 'available');
            slotDiv.textContent = slot.occupied ? '이용 불가' : '이용 가능';
            parkingStatusContainer.appendChild(slotDiv);
        });
    } catch (error) {
        console.error('주차 상태 조회 중 오류 발생:', error);
    }
}

// 차량 조회 폼 제출 처리
document.getElementById('car-search-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const carNumber = document.getElementById('car-number').value;

    // 차량 조회 API 호출
    try {
        const response = await fetch(`http://localhost:8000/index/payment?car_number=${carNumber}`);
        const result = await response.json();

        const resultContainer = document.getElementById('car-search-result');
        resultContainer.innerHTML = ''; // 초기화

        if (result.length > 0) {
            resultContainer.textContent = `차량 ${carNumber}의 정보: ${JSON.stringify(result)}`;
        } else {
            resultContainer.textContent = `차량 ${carNumber}에 대한 정보가 없습니다.`;
        }
    } catch (error) {
        console.error('차량 조회 중 오류 발생:', error);
    }
});


// 결제 내역을 가져오는 함수
async function fetchPaymentHistory() {
    try {
        const response = await fetch('http://localhost:8000/payment/history'); // 실제 API 엔드포인트
        const data = await response.json();

        const paymentHistoryContainer = document.getElementById('payment-history-container');
        paymentHistoryContainer.innerHTML = ''; // 초기화

        data.forEach(payment => {
            const paymentDiv = document.createElement('div');
            paymentDiv.textContent = `결제 ID: ${payment.payid}, 차량 번호: ${payment.carnum}, 결제 금액: ${payment.payment}, 결제 날짜: ${payment.paydate}`;
            paymentHistoryContainer.appendChild(paymentDiv);
        });
    } catch (error) {
        console.error('결제 내역 조회 중 오류 발생:', error);
    }
}

window.onload = fetchPaymentHistory;
