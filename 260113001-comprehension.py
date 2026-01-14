# Comprehension 

## git 계정 입력
## touchadd, commit(conventional)
## push origin main
## gitignore 파일 지정
## pre-commit.yaml 에 sample-config입력 후 설치
## stem, main branch

# Comprehension 예시 작성
# 기존의 묶음자료형에 대해 일괄적으로 작업을 수행해 새로운 묶음자료형을 만드는 것

# Before comprehension

nums = [1,2,3,4,5]
result = []

for i in nums:
    result.append(i*2)

print(result)

# With comprehension

nums = [1,2,3,4,5]
result = [i*2 for i in nums]
print(result)

# pros
# - 새 묶음자료형이 어떻게 생성된것인지 기록을 남길 수 있어 Pythonic 하다.
