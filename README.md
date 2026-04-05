# pe-viewer

Python으로 직접 만들어보는 미니 PE Viewer / Parser 프로젝트입니다.

## 목표

- PE 헤더 구조를 직접 읽으면서 흐름을 이해하기
- 바이트 단위 파싱을 통해 PE 파일이 어떻게 구성되는지 익히기
- Import Table 원리와 주소 매핑 방식을 직접 확인하기

## 제작 범위

- DOS Header
  - `MZ` 시그니처 확인
  - `e_lfanew` 읽기
- NT Headers
  - `PE\0\0` 시그니처 확인
  - File Header / Optional Header 확인
- Section Table
  - 섹션 이름, RVA, RAW, 크기 정보 출력
- Address Mapping
  - RVA <-> RAW offset 매핑 확인
- Import Table
  - Import Directory 위치 찾기
  - DLL 이름과 함수 이름 확인
  - IT가 어떤 식으로 연결되는지 파악

## 어디까지 만들기

이 프로젝트의 1차 목표는 전체 PE 포맷을 전부 구현하는 것이 아니라,
PE Header 구조와 Import Table 동작 원리를 직접 따라가며 이해할 수 있는 수준의 뷰어를 만드는 것입니다.

우선은 아래 범위까지 제작하는 것을 목표로 합니다.

- DOS Header
- NT Headers
- Section Table
- RVA/RAW 매핑
- Import Table

리소스, 재배치, TLS, Export Table 등은 이후 확장 대상으로 남겨둡니다.

## 실행

```bash
python anview.py
```
