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
| 하이퍼커넥트 | Hyperconnect Tech Blog | `https://hyperconnect.github.io` | `https://hyperconnect.github.io/feed.xml` | 200, entry 10개 | `rss / none / feed_only` |
| 왓챠 | Watcha Tech Blog | `https://medium.com/watcha` | `https://medium.com/feed/watcha` | 200, entry 10개 | `rss / none / feed_only` |
| NHN Cloud | NHN Cloud Meetup | `https://meetup.nhncloud.com` | `https://meetup.nhncloud.com/rss` | 200, entry 10개 | `rss / none / feed_only` |

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

## 수집 진행 기록

2026-05-16에 한국어 우선순위 source 10곳을 seed에 추가하고 실제 수집을 완료했습니다.

| Source | 수집 결과 |
| --- | ---: |
| `29cm-team` | 10 |
| `daangn-tech-blog` | 10 |
| `devsisters-tech-blog` | 66 |
| `gc-company-tech-blog` | 10 |
| `kakaopay-tech-blog` | 159 |
| `kurly-tech-blog` | 119 |
| `ly-corporation-tech-blog` | 50 |
| `musinsa-tech-blog` | 10 |
| `socar-tech-blog` | 10 |
| `yogiyo-tech-blog` | 10 |

총 454개 article을 신규 수집했습니다.

2026-05-17에 한국어 source 우선 확장 방침에 따라 7곳을 추가로 seed에 등록하고 수집했습니다.

| Source | 수집 결과 |
| --- | ---: |
| `coupang-engineering-blog` | 10 |
| `gmarket-tech-blog` | 10 |
| `lunit-team-blog` | 10 |
| `naver-cloud-platform-tech-blog` | 10 |
| `netmarble-tech-blog` | 15 |
| `wantedlab-tech-blog` | 10 |
| `zigbang-tech-blog` | 10 |

총 75개 article을 신규 수집했습니다.

Medium 기반 source는 최신 10개 중심으로 내려오는 경우가 많습니다. Medium archive HTML은 Cloudflare challenge가 걸릴 수 있어 서버 crawler에서 안정적으로 접근하기 어렵습니다. 과거 글 전체 수집이 필요하면 공식 API 또는 허용 가능한 archive 접근 방식을 별도로 검토합니다.

G마켓은 RSS 페이지네이션이 실제로는 같은 최신 글만 반복해서 내려왔지만, `sitemap.xml`에 글 URL이 충분히 포함되어 있었습니다. 따라서 `sitemap / article_fetch` 전략으로 전환했습니다.

넷마블은 RSS 페이지네이션이 동작하는 것을 확인했으므로 `rss / wordpress_paged / feed_only` 전략으로 전환했습니다.

추가 수집 결과:

| Source | 전략 | 수집 결과 |
| --- | --- | ---: |
| `gmarket-tech-blog` | `sitemap / none / article_fetch` | 104 |
| `netmarble-tech-blog` | `rss / wordpress_paged / feed_only` | 73 |

2026-05-17에 한국어 source를 추가로 확장했습니다.

| Source | 전략 | 수집 결과 |
| --- | --- | ---: |
| `banksalad-blog` | `rss / none / feed_only` | 78 |
| `inflab-tech-blog` | `rss / none / feed_only` | 42 |
| `upstage-blog` | `sitemap / none / article_fetch` | 76 |

이번 추가 라운드에서 총 196개 article을 신규 수집했습니다.

Sendbird는 sitemap이 크고 기술 글도 일부 포함하지만, 제품/마케팅 글이 많이 섞여 한국어 기술 사례 source로 바로 넣기에는 품질 검증이 더 필요합니다.

2026-05-18에 글로벌 엔지니어링 블로그 5곳을 추가했습니다. 한국어 source를 우선한다는 방향은 유지하되, 검색/인프라/관측성/플랫폼 엔지니어링 사례를 보강하기 위해 RSS 품질이 확인된 source만 먼저 넣었습니다.

추가 전 feed probe 결과:

| Source | Feed 응답 | Entry 수 | 비고 |
| --- | ---: | ---: | --- |
| `github-engineering-blog` | 200 | 10 | engineering category feed |
| `cloudflare-engineering-blog` | 200 | 14 | engineering tag feed |
| `datadog-engineering-blog` | 200 | 92 | engineering XML feed |
| `dropbox-tech-blog` | 200 | 10 | 전체 tech feed |
| `slack-engineering-blog` | 200 | 8 | WordPress feed |

수집 결과:

| Source | 전략 | 수집 결과 |
| --- | --- | ---: |
| `github-engineering-blog` | `rss / none / feed_only` | 10 |
| `cloudflare-engineering-blog` | `rss / none / feed_only` | 14 |
| `datadog-engineering-blog` | `rss / none / feed_only` | 92 |
| `dropbox-tech-blog` | `rss / none / feed_only` | 10 |
| `slack-engineering-blog` | `rss / none / feed_only` | 8 |

이번 추가 라운드에서 총 134개 article을 신규 수집했습니다.

Netflix Tech Blog도 후보였지만 현재 로컬 probe에서 SSL 인증서 검증 오류가 발생해 이번 라운드에서는 제외했습니다. 브라우저 또는 배포 환경에서 정상 접근 여부를 별도로 확인한 뒤 추가합니다.

신규 영어권 source는 아직 LLM 사례 요약을 생성하지 않았습니다. RSS summary만으로도 검색 대상에는 포함되지만, 카드의 `문제/해결` 품질을 높이려면 이후 `llm:summarize`를 별도로 실행해야 합니다.

2026-05-18에 신규 글로벌 source 134개 article 전체에 대해 LLM 사례 요약을 생성했습니다.

| Source | LLM 요약 결과 |
| --- | ---: |
| `cloudflare-engineering-blog` | 14 |
| `datadog-engineering-blog` | 92 |
| `dropbox-tech-blog` | 10 |
| `github-engineering-blog` | 10 |
| `slack-engineering-blog` | 8 |

총 134개 요약이 생성되었고 실패 건수는 0개입니다.

LLM 요약 반영 후 검색 평가 평균은 낮아졌습니다. 신규 영어권 글과 LLM 요약 keyword가 검색 후보를 넓히면서 기존 평가셋의 정답 문서가 일부 뒤로 밀렸기 때문입니다. 따라서 다음 수집 확장 단계에서는 article 수 증가와 함께 평가셋도 반드시 함께 보강합니다.

이후 신규 글로벌 source를 반영해 검색 평가셋을 보강했습니다. Datadog의 Go/Lambda/observability 사례, Cloudflare의 데이터 파이프라인/플랫폼 복원력 사례, Dropbox와 GitHub의 검색 품질/검색 아키텍처 사례를 기대 결과에 추가했습니다.

평가셋 보강 후 검색 평가 평균은 다음과 같이 재측정되었습니다.

| Metric | 보강 전 | 보강 후 |
| --- | ---: | ---: |
| `precision@5` | 0.420 | 0.468 |
| `recall@10` | 0.808 | 0.834 |
| `mrr` | 0.836 | 0.879 |
| `ndcg@10` | 0.751 | 0.788 |

이는 검색 로직을 바꿔 얻은 개선이 아니라, 신규 source 유입으로 생긴 유효한 검색 결과를 평가 기준에 반영한 결과입니다. 앞으로 source를 추가할 때는 수집 가능한 글 수뿐 아니라 해당 source가 어떤 query intent를 강화하는지도 함께 기록합니다.

2026-05-18에 한국어 기술 블로그 3곳을 추가 수집했습니다.

추가 전 feed probe 결과:

| Source | Feed 응답 | Entry 수 | 비고 |
| --- | ---: | ---: | --- |
| `hyperconnect-tech-blog` | 200 | 10 | AI, 추천, 실시간 통신, 인프라 사례 |
| `watcha-tech-blog` | 200 | 10 | 추천, MLOps, 클라우드 비용, 마이그레이션 사례 |
| `nhn-cloud-meetup` | 200 | 10 | DB, 보안, 클라우드, 개발 생산성 사례 |

수집 및 요약 결과:

| Source | 수집 결과 | LLM 요약 결과 |
| --- | ---: | ---: |
| `hyperconnect-tech-blog` | 10 | 10 |
| `watcha-tech-blog` | 10 | 10 |
| `nhn-cloud-meetup` | 10 | 10 |

이번 추가 라운드에서 총 30개 article을 신규 수집했고, 모두 LLM 사례 요약까지 생성했습니다.

재처리 결과:

| 항목 | 결과 |
| --- | ---: |
| 전체 article | 1703 |
| 추출 keyword | 3615 |
| Elasticsearch article 색인 | 1703 |
| suggestion 색인 | 90 |

검색 평가:

| Metric | 이전 | 이번 |
| --- | ---: | ---: |
| `precision@5` | 0.468 | 0.473 |
| `recall@10` | 0.834 | 0.834 |
| `mrr` | 0.879 | 0.862 |
| `ndcg@10` | 0.788 | 0.784 |

`precision@5`는 소폭 상승했지만, 일부 broad query에서 신규 후보가 상위에 섞이면서 `mrr`, `ndcg@10`은 소폭 하락했습니다. 다음 단계에서는 새 source에서 들어온 AI/추천/MLOps/ClickHouse/보안 관련 글을 평가셋에 보강하거나, query intent별 ranking 조정을 검토합니다.
