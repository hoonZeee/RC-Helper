# RC-Helper
루미큐브 승률 최적화 프로그램
--
### 참조한 알고리즘
   - Longest Increasing Subsequence
   - Interval Scheduling
   - Dynamic Programming(확장가능)

--
pip install -r requirements.txt

### algorithm
1. 입력: 손패(hand), 보드(board)
   - 두 배열을 결합하여 combined_tiles 생성
   - combined_tiles에서 조커("j") 개수 계산 (joker_count)

2. 색상별 숫자 그룹화
   - color_groups를 생성하여 각 타일을 색상별로 정리

3. 최대 길이의 연속된 타일(run) 찾기
   - runs 초기화
   - 각 색상 그룹에 대해:
     a. 숫자를 오름차순 정렬
     b. 빈 run 리스트와 jokers_left 초기화
     c. 타일 순회:
        - 연속된 숫자가 아니면:
          i. 조커 사용 가능하면 run에 추가
          ii. 아니면 run 길이가 3 이상인지 확인 후 runs에 저장
        - 연속된 숫자이면 run에 추가
     d. 마지막 run도 길이가 3 이상이면 runs에 저장

4. 최적의 조합(best_move) 선택
   - runs에서 가장 긴 조합을 선택

5. 출력: 최적의 조합(best_move)
