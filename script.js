let hand = [];
let boardGroups = []; // 보드의 그룹을 저장하는 배열

// 손패 업데이트
function updateHand() {
    const handInput = document.getElementById('hand-input').value;
    hand = handInput.split(',').map(tile => tile.trim());
    displayTiles('hand-cards', hand);
}

// 보드에 타일 추가
function updateBoard() {
    const boardInput = document.getElementById('board-input').value;
    const newGroup = boardInput.split(',').map(tile => tile.trim()); // 새로운 그룹 생성
    boardGroups.push(newGroup); // 새로운 그룹을 보드 그룹에 추가
    displayBoardGroups(); // 보드 그룹을 표시
}

// 보드 그룹 표시 함수
function displayBoardGroups() {
    const container = document.getElementById('board-groups');
    container.innerHTML = ''; // 기존 보드 그룹 지우기

    boardGroups.forEach(group => {
        const groupDiv = document.createElement('div');
        groupDiv.className = 'board-group';

        group.forEach(tile => {
            const tileDiv = document.createElement('div');
            tileDiv.className = `tile ${tile[0]}`; // 색상 클래스 적용
            tileDiv.innerText = tile;
            groupDiv.appendChild(tileDiv);
        });

        container.appendChild(groupDiv);
    });
}

// 타일 표시 함수 (손패 및 최적화 결과)
function displayTiles(containerId, tiles) {
    const container = document.getElementById(containerId);
    container.innerHTML = ''; // 기존 타일 지우기

    tiles.forEach(tile => {
        const tileDiv = document.createElement('div');
        tileDiv.className = `tile ${tile[0]}`;
        tileDiv.innerText = tile;
        container.appendChild(tileDiv);
    });
}

// 최적화 분석 함수
async function analyzeBoard() {
    const flatBoard = boardGroups.flat(); // 보드 그룹들을 단일 배열로 변환
    const response = await fetch('/suggest', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ hand, board: flatBoard }) // 보드와 손패 전송
    });

    const data = await response.json();
    const bestMove = data.best_move;
    displayTiles('optimized-result', bestMove || []);
}
