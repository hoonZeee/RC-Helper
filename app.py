from flask import Flask, request, jsonify, render_template
import random
from collections import defaultdict

app = Flask(__name__)

# 타일 생성
color_map = {"r": "Red", "b": "Blue", "y": "Yellow", "k": "Black"}
simple_tiles = [f"{color}{number}" for color in color_map for number in range(1, 14) for _ in range(2)]
simple_tiles += ["j", "j"]  # 조커 추가
random.shuffle(simple_tiles)

# 조커를 포함한 최적의 조합 찾기 함수
def find_max_run(color_groups, joker_count):
    runs = []

    # 색상별로 타일을 정리하여 최대 길이의 연속된 숫자를 찾음
    for color, numbers in color_groups.items():
        numbers.sort()
        run = []
        jokers_left = joker_count

        i = 0
        while i < len(numbers):
            # 연속된 숫자가 아닐 경우
            if run and numbers[i] != int(run[-1][1:]) + 1:
                # 조커를 사용할 수 있는지 확인
                if jokers_left > 0:
                    jokers_left -= 1
                    run.append("j")
                else:
                    # 현재 run이 최소 길이(3) 이상일 경우 runs에 추가
                    if len(run) >= 3:
                        runs.append(run)
                    # run 초기화
                    run = []
                    jokers_left = joker_count  # 조커 수 초기화

            # 연속된 숫자일 경우 run에 추가
            run.append(f"{color}{numbers[i]}")
            i += 1

        # 마지막 run도 길이가 3 이상일 경우 추가
        if len(run) >= 3:
            runs.append(run)

    # runs 중 가장 긴 run 조합을 선택 (최대 타일 수 사용)
    max_run = max(runs, key=len) if runs else []
    return max_run

# 최적의 수 제안 함수 (손패와 보드를 합쳐서 분석)
def suggest_best_move(hand, board):
    combined_tiles = hand + board  # 손패와 보드를 합침
    joker_count = combined_tiles.count("j")  # 조커 개수 계산

    # 색상별 숫자 그룹화
    color_groups = defaultdict(list)
    for tile in combined_tiles:
        if tile != "j":
            color = tile[0]
            number = int(tile[1:])
            color_groups[color].append(number)

    # runs와 groups 계산
    max_run = find_max_run(color_groups, joker_count)
    best_move = max_run if max_run else []

    return best_move

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest', methods=['POST'])
def suggest():
    data = request.json
    hand = data.get("hand", [])
    board = data.get("board", [])
    best_move = suggest_best_move(hand, board)
    return jsonify({"best_move": best_move})

if __name__ == '__main__':
    app.run(debug=True, port=3000)
