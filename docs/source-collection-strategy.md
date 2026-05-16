# 기술 블로그 수집 전략

이 문서는 TechCase에서 추가로 수집할 기업 기술 블로그 후보를 확인하고, source별 수집 전략을 분류한 기록입니다.

확인 기준:

- 공식 기업 기술 블로그 또는 공식 채용/엔지니어링 블로그인지 확인합니다.
- RSS/Atom feed가 바로 사용 가능한지 확인합니다.
- RSS만으로 충분한지, 상세 글 fetch나 HTML 목록 crawler가 필요한지 분리합니다.
- 불확실한 source는 바로 수집하지 않고 `deferred`로 둡니다.

## 전략 기준

```text
collection_strategy
- rss: RSS/Atom feed를 직접 수집
- rss_with_article_fetch: RSS로 목록을 가져온 뒤 글 상세 페이지에서 본문 추가 수집
- html_list: RSS 없이 목록 페이지를 파싱해서 수집
- sitemap: sitemap 기반으로 글 URL 수집
- deferred: 공식 블로그이지만 수집 방식 검증 필요

pagination_strategy
- none: feed 한 번만 요청
- wordpress_paged: WordPress RSS 페이지네이션
- page_number: 목록 페이지 번호 기반
- cursor: cursor 또는 API 기반
- sitemap: sitemap 기반

content_strategy
- feed_only: feed의 summary/content를 그대로 사용
- article_fetch: 글 상세 페이지에서 본문을 추가 수집
- deferred: 본문 확보 방식 미정
```

## 이미 수집 중인 Source

| 회사 | Source | Feed | 전략 | 비고 |
| --- | --- | --- | --- | --- |
| AWS | AWS Architecture Blog | `https://aws.amazon.com/blogs/architecture/feed/` | `rss / none / feed_only` | 현재 수집 중 |
| AWS | AWS Database Blog | `https://aws.amazon.com/blogs/database/feed/` | `rss / none / feed_only` | 현재 수집 중 |
| AWS | AWS Compute Blog | `https://aws.amazon.com/blogs/compute/feed/` | `rss / none / feed_only` | 현재 수집 중 |
| AWS | AWS Big Data Blog | `https://aws.amazon.com/blogs/big-data/feed/` | `rss / none / feed_only` | 현재 수집 중 |
| AWS | AWS DevOps Blog | `https://aws.amazon.com/blogs/devops/feed/` | `rss / none / feed_only` | 현재 수집 중 |
| Toss | Toss Tech | `https://toss.tech/rss.xml` | `rss / none / feed_only` | 현재 수집 중 |
| NAVER | NAVER D2 | `https://d2.naver.com/d2.atom` | `rss / none / feed_only` | 현재 수집 중 |
| Kakao | Kakao Tech | `https://tech.kakao.com/feed/` | `rss / none / feed_only` | 현재 수집 중 |
| Woowa Brothers | Woowa Tech Blog | `https://techblog.woowahan.com/feed/` | `rss / wordpress_paged / feed_only` | WordPress 페이지네이션으로 과거 글까지 수집 |

## 한국어 기술 블로그 후보

### 바로 RSS 수집 가능한 후보

| 회사 | Source | Site | Feed | 확인 결과 | 추천 전략 |
| --- | --- | --- | --- | --- | --- |
| 당근 | 당근 테크 블로그 | `https://medium.com/daangn` | `https://medium.com/feed/daangn` | 200, entry 10개 | `rss / none / feed_only` |
| LY Corporation | LY Corporation Tech Blog | `https://techblog.lycorp.co.jp/ko` | `https://techblog.lycorp.co.jp/ko/feed/index.xml` | 200, entry 50개 | `rss / none / feed_only` |
| 카카오페이 | 카카오페이 기술 블로그 | `https://tech.kakaopay.com` | `https://tech.kakaopay.com/rss.xml` | 200, entry 159개 | `rss / none / feed_only` |
| 쏘카 | SOCAR Tech Blog | `https://tech.socarcorp.kr` | `https://tech.socarcorp.kr/feed.xml` | 200, entry 10개 | `rss / none / feed_only` |
| 컬리 | 컬리 기술 블로그 | `https://helloworld.kurly.com` | `https://helloworld.kurly.com/rss.xml` | 200, entry 119개 | `rss / none / feed_only` |
| 여기어때 | 여기어때 기술블로그 | `https://techblog.gccompany.co.kr` | `https://techblog.gccompany.co.kr/feed` | 200, entry 10개 | `rss / none / feed_only` |
| 요기요 | YOGIYO Tech Blog | `https://techblog.yogiyo.co.kr` | `https://techblog.yogiyo.co.kr/feed` | 200, entry 10개 | `rss / none / feed_only` |
| 무신사 | MUSINSA Tech Blog | `https://techblog.musinsa.com` | `https://techblog.musinsa.com/feed` | 200, entry 10개 | `rss / none / feed_only` |
| 29CM | 29CM TEAM | `https://medium.com/29cm` | `https://medium.com/feed/29cm` | 200, entry 10개 | `rss / none / feed_only` |
| 데브시스터즈 | Devsisters 기술 블로그 | `https://tech.devsisters.com` | `https://tech.devsisters.com/rss.xml` | 200, entry 66개 | `rss / none / feed_only` |

### 별도 수집기 검토가 필요한 후보

| 회사 | Source | Site | 확인 결과 | 추천 전략 | 다음 확인 |
| --- | --- | --- | --- | --- | --- |
| 쿠팡 | Coupang Engineering Blog | `https://www.coupang.jobs/en/life-at-coupang/engineering-blog/` | 공식 엔지니어링 블로그 확인, RSS 자동 탐색 실패 | `html_list / page_number / article_fetch` | 목록 DOM 구조와 페이지네이션 방식 확인 |
| 넥슨 | Nexon Intelligence Labs | `https://www.intelligencelabs.tech` | 공식 기술 사이트 확인, RSS 자동 탐색 실패 | `html_list / page_number / article_fetch` 또는 `deferred` | 글 목록과 상세 페이지 구조 확인 |

## 영어 기술 블로그 후보

### 바로 RSS 수집 가능한 후보

| 회사 | Source | Site | Feed | 확인 결과 | 추천 전략 |
| --- | --- | --- | --- | --- | --- |
| Netflix | Netflix Tech Blog | `https://netflixtechblog.com` | `https://netflixtechblog.com/feed` | 200, entry 10개 | `rss / none / feed_only` |
| Airbnb | Airbnb Tech Blog | `https://medium.com/airbnb-engineering` | `https://medium.com/feed/airbnb-engineering` | 200, entry 10개 | `rss / none / feed_only` |
| Cloudflare | Cloudflare Engineering | `https://blog.cloudflare.com/tag/engineering/` | `https://blog.cloudflare.com/tag/engineering/rss/` | 200, entry 14개 | `rss / none / feed_only` |
| GitHub | GitHub Engineering | `https://github.blog/engineering/` | `https://github.blog/engineering/feed/` | 200, entry 10개 | `rss / none / feed_only` |
| Stripe | Stripe Blog | `https://stripe.com/blog` | `https://stripe.com/blog/feed.rss` | 200, entry 10개 | `rss / none / feed_only` |
| Slack | Engineering at Slack | `https://slack.engineering` | `https://slack.engineering/feed/` | 200, entry 8개 | `rss / none / feed_only` |
| Datadog | Datadog Engineering Blog | `https://www.datadoghq.com/blog/engineering/` | `https://www.datadoghq.com/blog/engineering/index.xml` | 200, entry 92개 | `rss / none / feed_only` |
| Pinterest | Pinterest Engineering Blog | `https://medium.com/pinterest-engineering` | `https://medium.com/feed/pinterest-engineering` | 200, entry 10개 | `rss / none / feed_only` |
| Dropbox | Dropbox Tech Blog | `https://dropbox.tech` | `https://dropbox.tech/feed` | 200, entry 10개 | `rss / none / feed_only` |
| Lyft | Lyft Engineering | `https://eng.lyft.com` | `https://eng.lyft.com/feed` | 200, entry 10개 | `rss / none / feed_only` |

### 별도 수집기 검토가 필요한 후보

| 회사 | Source | Site | 확인 결과 | 추천 전략 | 다음 확인 |
| --- | --- | --- | --- | --- | --- |
| Coupang | Coupang Engineering Blog | `https://www.coupang.jobs/en/life-at-coupang/engineering-blog/` | RSS 없음 | `html_list / page_number / article_fetch` | 한국어/영어 중복 URL 처리 |
| Shopify | Shopify Engineering | `https://shopify.engineering` | 일반 RSS 후보 URL에서 feed entry 0개 또는 404 | `html_list / page_number / article_fetch` 또는 `deferred` | 사이트 구조와 robots 정책 확인 |
| LinkedIn | LinkedIn Engineering | `https://www.linkedin.com/blog/engineering` | RSS 자동 탐색 실패 | `html_list / page_number / article_fetch` 또는 `deferred` | 접근 제한과 수집 정책 확인 |
| Uber | Uber Engineering | `https://www.uber.com/blog/engineering/` | RSS 후보 URL 404 | `html_list / page_number / article_fetch` 또는 `deferred` | 지역 redirect와 목록 구조 확인 |

## 우선순위

1. RSS가 바로 확인된 한국어 source를 먼저 추가합니다.
2. RSS가 바로 확인된 영어 source를 그 다음 추가합니다.
3. RSS source 추가 후 `crawl:rss`, `keywords:extract`, `llm:summarize`, `search:reindex` 순서로 데이터 품질을 확인합니다.
4. 쿠팡, 넥슨, Shopify, LinkedIn, Uber처럼 RSS가 확인되지 않은 source는 `html_list` 수집기를 만든 뒤 추가합니다.

## 다음 구현 후보

가장 작은 다음 작업은 RSS source 후보를 seed에 추가하는 것입니다.

우선 추가 추천:

```text
당근
LY Corporation
카카오페이
쏘카
컬리
여기어때
요기요
무신사
29CM
데브시스터즈
Datadog
Dropbox
Cloudflare
GitHub
```

Medium 기반 블로그는 RSS에서 기본적으로 최신 10개만 확인되는 경우가 많습니다. 과거 글 전체 수집이 중요해지면 Medium archive 또는 HTML 목록 수집 전략을 별도로 설계합니다.
