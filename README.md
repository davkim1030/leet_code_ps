# Summary
- LeetCode 문제 풀이 저장소입니다.
- 다양한 LeetCode 알고리즘 문제를 Python으로 풀이합니다.
- 문제별로 코드와 테스트 파일이 정리되어 있습니다.

# Setup Dependencies
- Python 3.12.0 기준으로 작성됐습니다. 먼저 의존성을 설치해줍니다.
    ```bash
    pip install -r requirements.txt
    ```

# Generate Problem and Test File Format
- leetcode 문제와 테스트 코드를 형식을 생성해줍니다. 다음 형식의 명령어로 실행합니다. `python create_problem.py [leetcode_problem_url]`
- 예시)
    ```bash
    python create_problem.py https://leetcode.com/problems/two-sum/
    ```

# Run Tests
- `pytest`로 실행시킵니다.
    ```bash
    pytest tests
    ```
- Example Result
    ```text
    ==================== test session starts =====================
    platform darwin -- Python 3.12.0, pytest-8.3.5, pluggy-1.5.0  
    collected 17 items                                            
                                                              
    tests/test_add_two_numbers.py ....                      [ 23%]
    tests/test_longest_substring_without_repeating.py ....  [ 47%]
    tests/test_median_of_two_sorted_arrays.py ...           [ 64%]
    tests/test_remove_element.py ..                         [ 76%]
    tests/test_two_sum.py ....                              [100%]
    ===================== 17 passed in 0.02s =====================
    ```
