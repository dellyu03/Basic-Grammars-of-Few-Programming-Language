# Conventional-commits

> based on ["위대한 IT 영어"](https://www.geekhaus.club/english)

> 추가  정보는 [conventional-commits.org 참고](https://www.conventionalcommits.org/en/v1.0.0/)

## 커밋 메시지를 작성하는 이유
- 효율적인 프로젝트 히스토리 점검
- 이슈 추적

> 영문으로 커밋 메시지를 작성해야 해외 개발자와 협업 할 수 있다.

커리어를 위해 글로벌 오픈소스에 기여하거나 해외 개발자와 협업을 위해선 전 세계적으로 통용되는 영어를 사용해 커밋 메시지를 작성해야 한다. 

<br>

## Conventional Commits
> 전 세계적으로 통용되는 커밋 메시지 관습

커밋 메시지 작성법을 통일하여 일관성을 유지, 효율적인 소통가능

<br>

## Conventional Commits의 구조
> Subject(Title, Body, Footer)

```
<type> [optional scope] : <description>
[optional body]
[optional footer(s)]
```

type과 description은 필수 명시

- type : 커밋과 관련된 작업의 성격
- scope : 해당 커밋의 수정 범위, 협업싯 서로의 업무 파악 가능
- description : 커밋의 작업 내용 요약
- body : 요약해서 전달하기 어려운 내용
- footer(s) :  어떤 이슈에서 왔는지와 같은 참조 정보들을 추가하는 용도

- ex)
```
fix: prevent racing of requests  // Title

Introduce a request id and a reference to latest request. Dismiss
incoming responses other than from latest request.
                                                        //body
Remove timeouts which were used to mitigate the racing issue but are
obsolete now.

Reviewed-by: Z      //footer(s)
Refs: #123         
```

### 1) Commit Types
> 해당 커밋이 하는 역할

#### Types
- **feat** : 코드에 새로운 기능 추가
- **fix** : 버그 수정
- **breaking change** : 이전 버전과 호환되지 않는 변경 내역(!로 표현 가능 
feat!)
- **docs** : 개발 문서 변경
- **style** : 들여쓰기, 세미콜론 등 코드 형식 및 스타일 변경
- **ci** : Cl/CD(Continuos Integration and Deployment) 관련 코드 변경
- **refactor** : 중복된 코드 제거, 변수명 변경, 코드 단순화 등 리팩터링 관련
- **test** : 테스트 관련 코드 변경
- **build** : 빌드 시스템 관련 코드 변경
- **perf** : 성능 개선 관련 코드 변경
- **chore** : 기타 코드 변경

### 2) Title 작성 원칙
> Conventional Commits의 Title을 작성하는 방법

ex) fix:remove deprecated features

#### 1. 동사 원형으로 시작
- 명령적 어조를 위해 대부분 동사 원형을 사용하지만 때에 따라 과거형 또는 3인칭 단수형을 사용하기도 함

`c.f` 자주 사용하는 동사

- handle : 처리하다
- optimize : 최적화하다
- implement : 구현, 적용하다
- refactor : 리팩터링하다
- revert : 되돌리다
- merge : 병합하다
- document : 문서를 작성하다
- bump : 버전을 올리다
- simplify : 단순화하다
- enable : 가능하게 하다
- wrap : 감싸다
- deploy : 배포하다
- modify : 변경하다

#### 2. 모두 소문자 혹은 첫글자만 대문자
- Conventional Commits는 소문자로 표기, 일반적인 커밋은 첫글자만 대문자로 표기함

#### 3. 관사 최소화
- 50글자 제한이 있어 핵심 키워드만 사용 (관사를 생략, 최소화)

#### 4. 마침표와 같은 구두점 생략
- 반드시 필요한 경우를 제외하고 생략

#### 5. 변경한 이유 설명은 Body에
- 타이틀은 50글자 제한이 있어 사유와 상세 설명은 본문에 담기

### 3) Body와 footer

#### 1. Body
> 코드 변경 사유, 상세 설명

#### 2. footer
- 참조 정보 어느 이슈에서 왔는지 등




