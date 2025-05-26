#!/usr/bin/env python3
import re
import sys
from pathlib import Path
from typing import List, Tuple
import requests
import json


def snake_case(name: str) -> str:
    """Convert a string to snake_case."""
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
    return name.lower().replace(' ', '_').replace('-', '_').replace('__', '_')


def get_problem_info(url: str) -> Tuple[str, str, str, str]:
    """
    LeetCode 문제 페이지에서 필요한 정보를 가져옵니다.
    반환값: (문제 제목, 문제 번호, 기본 코드, 메서드 이름)
    """
    # LeetCode GraphQL API endpoint
    api_url = "https://leetcode.com/graphql"
    
    # URL에서 문제 제목 추출
    title_slug = url.strip('/').split('/')[-1].split('?')[0]
    
    # GraphQL 쿼리
    query = """
    query getQuestionDetail($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            title
            codeSnippets {
                lang
                code
            }
            metaData
        }
    }
    """
    
    response = requests.post(api_url, json={
        'query': query,
        'variables': {'titleSlug': title_slug}
    })
    
    data = response.json()['data']['question']
    
    # Python 코드 스니펫 찾기
    python_code = next(
        (snippet['code'] for snippet in data['codeSnippets'] 
         if snippet['lang'] == 'Python3'),
        None
    )
    
    if not python_code:
        raise ValueError("Python3 code snippet not found")
    
    # 메서드 이름 추출
    meta_data = json.loads(data['metaData'])
    method_name = meta_data.get('name', '')
    
    return (
        data['title'],
        data['questionId'],
        python_code,
        method_name
    )


def create_problem_file(title: str, number: str, code: str) -> str:
    """문제 파일을 생성합니다."""
    file_name = snake_case(title)
    file_path = Path('problems') / f'{file_name}.py'
    
    # 필요한 import 문 추가
    if 'List' in code:
        code = 'from typing import List\n\n' + code
    
    content = f'''# https://leetcode.com/problems/{file_name}/
# {number}. {title}
{code}'''
    
    file_path.write_text(content)
    return file_name


def create_test_file(title: str, method_name: str) -> None:
    """테스트 파일을 생성합니다."""
    file_name = snake_case(title)
    test_file_path = Path('tests') / f'test_{file_name}.py'
    
    content = f'''from unittest import TestCase

from problems.{file_name} import Solution
from tests import PSTestCase


class TestCases(TestCase, PSTestCase):
    def setUp(self):
        self.solution_object = Solution()
    
    def solution(self, *args, **kwargs) -> any:
        return self.solution_object.{method_name}(*args, **kwargs)

    def test_example_1(self):
        # Given: Example 1
        # TODO: 테스트 케이스 작성
        pass

    def test_example_2(self):
        # Given: Example 2
        # TODO: 테스트 케이스 작성
        pass

    def test_example_3(self):
        # Given: Example 3
        # TODO: 테스트 케이스 작성
        pass
'''
    
    test_file_path.write_text(content)


def main():
    if len(sys.argv) != 2:
        print("Usage: python create_problem.py <leetcode_problem_url>")
        sys.exit(1)
    
    url = sys.argv[1]
    
    try:
        title, number, code, method_name = get_problem_info(url)
        
        # 문제 파일 생성
        file_name = create_problem_file(title, number, code)
        print(f"Created problem file: problems/{file_name}.py")
        
        # 테스트 파일 생성
        create_test_file(title, method_name)
        print(f"Created test file: tests/test_{file_name}.py")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
