# 로고 자산 관리

TechCase는 검색 결과에서 글의 출처를 빠르게 구분할 수 있도록 회사 로고를 표시한다.

## 기본 원칙

- 공식 브랜드 리소스 페이지에서 제공하는 파일만 저장한다.
- 공식 파일이 없거나 사용 조건이 애매한 회사는 텍스트 기반 로고 배지를 사용한다.
- 로고는 출처 식별 목적으로만 사용하며, TechCase와 해당 회사의 제휴 관계를 의미하지 않는다.
- 로고의 색상, 비율, 형태를 임의로 변경하지 않는다.

## 현재 저장된 로고

| 회사 | 파일 | 공식 출처 | 비고 |
| --- | --- | --- | --- |
| NAVER | `apps/web/public/logos/naver.svg` | https://www.navercorp.com/company/brandGuide | 브랜드 지침 동의 후 다운로드되는 공식 리소스의 Primary Logo |
| Toss | `apps/web/public/logos/toss.png` | https://brand.toss.im/ | Toss 브랜드 리소스 센터의 Primary Logo |
| Kakao | `apps/web/public/logos/kakao.png` | https://www.kakaocorp.com/page/detail/11340 | 공식 CI 페이지 제공 파일. 해당 페이지에 상업적 이용 불가 문구가 있으므로 사용 범위 확인 필요 |

## 사용 방식

프론트엔드는 `company` 또는 `sourceSlug`를 기준으로 로고를 선택한다.

- 공식 로고 파일이 있으면 이미지 로고를 표시한다.
- 공식 로고 파일이 없으면 회사별 색상과 짧은 라벨을 사용하는 텍스트 배지를 표시한다.

이 구조를 유지하면 특정 회사의 로고 사용 조건이 맞지 않을 때 이미지 매핑만 제거하고 텍스트 배지로 되돌릴 수 있다.
