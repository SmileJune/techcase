# 추가 기술 블로그 후보 백로그

이 문서는 TechCase에 앞으로 추가할 기업 기술 블로그 후보를 정리한 백로그입니다.

목표는 단순히 많은 RSS를 넣는 것이 아니라, 다음 기준을 만족하는 source를 우선적으로 늘리는 것입니다.

- 기업 또는 조직이 직접 운영하는 공식 기술/엔지니어링 블로그
- 실제 서비스 운영, 아키텍처, 장애 대응, 인프라, 데이터, 검색, 프론트엔드/백엔드 사례가 포함된 블로그
- RSS/Atom feed 또는 안정적인 목록 페이지가 있어 반복 수집이 가능한 블로그
- 광고성 콘텐츠보다 엔지니어링 사례의 비중이 높은 블로그
- 한국어/영어 검색 품질을 함께 높일 수 있는 블로그

이미 수집 중인 source는 이 문서의 추가 후보에서 제외합니다. 현재 수집 중인 source와 수집 결과는 [기술 블로그 수집 전략](./source-collection-strategy.md)에 기록합니다.

## 우선순위 기준

| 우선순위 | 의미 | 다음 작업 |
| --- | --- | --- |
| P0 | 공식 블로그이고 RSS/Atom feed가 확인되어 바로 seed 추가 가능 | source seed 추가 후 `crawl:rss` 실행 |
| P1 | 공식 블로그로 보이며 feed 후보가 있지만 실제 응답/본문 품질 확인 필요 | source probe 후 seed 추가 |
| P2 | RSS가 없거나 불안정해서 HTML 목록, sitemap, 상세 페이지 fetcher가 필요 | 별도 수집기 구현 후 추가 |
| P3 | 기술 블로그 성격은 있으나 공식성, 업데이트 상태, 수집 정책 확인 필요 | 보류 |

## 바로 추가하기 좋은 영어권 후보

영어권 대형 기술 블로그는 분산 시스템, 데이터 플랫폼, 인프라, 검색, observability, 대규모 운영 사례가 많아서 TechCase의 검색 품질 평가에 도움이 됩니다.

| 우선순위 | 회사/블로그 | Site | Feed 후보 | 수집 방식 | 주요 기대 주제 | 비고 |
| --- | --- | --- | --- | --- | --- | --- |
| P0 | Netflix Tech Blog | `https://netflixtechblog.com` | `https://netflixtechblog.com/feed` | `rss / none / feed_only` | Java, data platform, media pipeline, personalization, reliability | Medium 기반이라 최신 글 중심으로 내려올 가능성이 큼 |
| P0 | Meta Engineering | `https://engineering.fb.com` | `https://engineering.fb.com/feed/` | `rss / wordpress_paged / feed_only` | ML, mobile, infra, configuration, scale | WordPress feed 확인됨 |
| P0 | Slack Engineering | `https://slack.engineering` | `https://slack.engineering/feed/` | `rss / wordpress_paged / feed_only` | AWS, data pipeline, deployment, platform engineering | WordPress feed 확인됨 |
| P0 | Cloudflare Blog | `https://blog.cloudflare.com` | `https://blog.cloudflare.com/rss/` 또는 tag feed | `rss / none / feed_only` | CDN, network, security, Workers, Rust, observability | 전체 feed와 tag feed 중 선택 필요 |
| P0 | GitHub Engineering | `https://github.blog/engineering/` | `https://github.blog/engineering/feed/` | `rss / none / feed_only` | developer platform, code search, CI, infra | engineering category feed 우선 |
| P0 | Datadog Engineering | `https://www.datadoghq.com/blog/engineering/` | `https://www.datadoghq.com/blog/engineering/index.xml` | `rss / none / feed_only` | observability, metrics, tracing, backend, infra | 기존 후보 문서에서 feed 확인됨 |
| P0 | Dropbox Tech | `https://dropbox.tech` | `https://dropbox.tech/feed` | `rss / none / feed_only` | storage, sync, reliability, infra | 기존 후보 문서에서 feed 확인됨 |
| P0 | Lyft Engineering | `https://eng.lyft.com` | `https://eng.lyft.com/feed` | `rss / none / feed_only` | marketplace, dispatch, data, infra | 기존 후보 문서에서 feed 확인됨 |
| P0 | Airbnb Tech Blog | `https://airbnb.tech` | `https://medium.com/feed/airbnb-engineering` | `rss / none / feed_only` | data mesh, experimentation, infra, ML | 공식 사이트는 `airbnb.tech`, 글은 Medium으로 연결됨 |
| P0 | Stripe Blog | `https://stripe.com/blog` | `https://stripe.com/blog/feed.rss` | `rss / none / feed_only` | payments, API, reliability, infra | engineering-only 필터링 필요할 수 있음 |
| P0 | Pinterest Engineering | `https://medium.com/pinterest-engineering` | `https://medium.com/feed/pinterest-engineering` | `rss / none / feed_only` | recommendation, ML, data, infra | Medium 기반 |

## 검증 후 추가할 영어권 후보

이 후보들은 가치가 높지만 RSS가 없거나, feed URL이 불확실하거나, 목록 페이지 수집이 필요합니다.

| 우선순위 | 회사/블로그 | Site | 예상 수집 방식 | 주요 기대 주제 | 확인할 내용 |
| --- | --- | --- | --- | --- | --- |
| P1 | Discord Engineering | `https://discord.com/category/engineering` | `rss` 또는 `html_list` | Cassandra, storage, real-time messaging, infra | RSS 존재 여부와 category URL 안정성 |
| P1 | DoorDash Engineering | `https://careersatdoordash.com/blog/engineering/` | `rss` 또는 `html_list` | logistics, marketplace, ML, data platform | feed 자동 탐색 필요 |
| P1 | Spotify Engineering | `https://engineering.atspotify.com` | `rss` 또는 `html_list` | backend, data, ML, platform | RSS/Atom 후보 확인 |
| P1 | Figma Engineering | `https://www.figma.com/blog/engineering/` | `rss` 또는 `html_list` | frontend, collaboration, performance, infra | engineering category feed 확인 |
| P1 | PayPal Technology Blog | `https://medium.com/paypal-tech` | `https://medium.com/feed/paypal-tech` | payments, platform, security | Medium feed 품질 확인 |
| P1 | Canva Engineering | `https://www.canva.dev/blog/engineering/` | `rss` 또는 `html_list` | frontend, design platform, infra | feed 후보 확인 |
| P2 | Uber Engineering | `https://www.uber.com/blog/engineering/` | `html_list / article_fetch` | marketplace, dispatch, data, infra | RSS 후보가 불안정하므로 목록 수집 우선 |
| P2 | Shopify Engineering | `https://shopify.engineering` | `html_list / article_fetch` | commerce platform, Ruby, infrastructure, data | `feed.xml`은 404 응답 확인됨 |
| P2 | LinkedIn Engineering | `https://www.linkedin.com/blog/engineering` | `html_list / deferred` | search, feed, data infra, ML | 접근 제한과 수집 정책 확인 |

## 추가 검토할 한국어 후보

한국어 후보는 TechCase의 핵심 차별점인 한글 문제상황 검색, 한영 기술명 검색, 국내 기업 사례 비교에 직접적으로 도움이 됩니다.

| 우선순위 | 회사/블로그 | Site | Feed 후보 | 예상 수집 방식 | 주요 기대 주제 | 확인할 내용 |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | 네이버 클라우드 플랫폼 | `https://medium.com/naver-cloud-platform` | `https://medium.com/feed/naver-cloud-platform` | `rss / none / feed_only` | cloud, Kubernetes, DevOps, database | 공식성/업데이트 상태 확인 |
| P1 | 넷마블 기술 블로그 | `https://netmarble.engineering` | 확인 필요 | `rss` 또는 `html_list` | game backend, large traffic, data | feed 자동 탐색 |
| P1 | G마켓 기술 블로그 | `https://dev.gmarket.com` | 확인 필요 | `rss` 또는 `html_list` | commerce, search, backend, data | feed 자동 탐색 |
| P1 | 직방 기술 블로그 | `https://medium.com/zigbang` | `https://medium.com/feed/zigbang` | `rss / none / feed_only` | real estate platform, backend, data | Medium feed 품질 확인 |
| P1 | 인프랩 기술 블로그 | `https://tech.inflab.com` | 확인 필요 | `rss` 또는 `html_list` | education platform, backend, infra | RSS/목록 구조 확인 |
| P1 | 뱅크샐러드 기술 블로그 | `https://blog.banksalad.com/tech/` | 확인 필요 | `rss` 또는 `html_list` | fintech, mobile, data, backend | 공식 tech category feed 확인 |
| P1 | 라인/LY 일본어 기술 블로그 | `https://techblog.lycorp.co.jp/ja` | `https://techblog.lycorp.co.jp/ja/feed/index.xml` | `rss / none / feed_only` | messaging, infra, platform | 한국어 LY와 중복 정책 필요 |
| P1 | PortOne Developers | `https://developers.portone.io/blog` | 확인 필요 | `rss` 또는 `html_list` | payments, API, SDK | 기술 블로그와 문서성 글 분리 필요 |
| P1 | Sendbird Engineering | `https://sendbird.com/blog/topic/engineering` | 확인 필요 | `rss` 또는 `html_list` | messaging, chat, infra, SDK | feed 또는 category 목록 확인 |
| P1 | Upstage Blog | `https://www.upstage.ai/blog` | 확인 필요 | `rss` 또는 `html_list` | LLM, ML platform, AI infra | 연구/제품 글과 엔지니어링 글 분리 |
| P2 | 쿠팡 Engineering Blog | `https://www.coupang.jobs/en/life-at-coupang/engineering-blog/` | RSS 없음으로 추정 | `html_list / article_fetch` | commerce, logistics, data, platform | 기존 문서에서 별도 수집기 대상으로 분류 |
| P2 | 오늘의집 기술 블로그 | 확인 필요 | 확인 필요 | `html_list / article_fetch` | commerce, recommendation, frontend, backend | 공식 URL과 목록 구조 확인 |
| P2 | 야놀자 기술 블로그 | `https://yanolja.github.io` | 확인 필요 | `rss` 또는 `html_list` | travel platform, backend, data | 업데이트 상태 확인 |
| P2 | 원티드 제품 팀 | `https://medium.com/wantedjobs` | Medium feed 후보 | `rss / none / feed_only` | matching, recommendation, product engineering | 기술 글 비중 확인 |
| P2 | 스포카 기술 블로그 | `https://spoqa.github.io` | 확인 필요 | `rss` 또는 `html_list` | backend, data, open source | 업데이트 상태 확인 |

## 일본/글로벌 아시아권 후보

일본/아시아권 블로그는 영어권 대기업과 한국 기업 사이의 사례를 보완할 수 있습니다. 다만 언어가 늘어나면 검색 analyzer와 LLM 요약 비용이 함께 늘어나므로, 우선은 RSS 확인 후 소량 수집으로 평가합니다.

| 우선순위 | 회사/블로그 | Site | 예상 수집 방식 | 주요 기대 주제 | 비고 |
| --- | --- | --- | --- | --- | --- |
| P1 | Mercari Engineering | `https://engineering.mercari.com` | `rss` 또는 `html_list` | marketplace, microservices, mobile, ML | 일본어/영어 혼합 가능 |
| P1 | DeNA Engineering | `https://engineering.dena.com` | `rss` 또는 `html_list` | game, backend, infra, ML | 일본어 중심 |
| P1 | Cookpad Developers | `https://techlife.cookpad.com` | `rss` 또는 `html_list` | Ruby, search, data, product engineering | 일본어 중심 |
| P1 | ZOZO TECH BLOG | `https://techblog.zozo.com` | `rss` 또는 `html_list` | commerce, data, search, frontend | 일본어 중심 |
| P1 | Hatena Developer Blog | `https://developer.hatenastaff.com` | `rss` 또는 `html_list` | web, infra, SRE | 일본어 중심 |
| P1 | Grab Tech | `https://engineering.grab.com` | `rss` 또는 `html_list` | mobility, payments, data, infra | 영어 |

## 한국어 우선 추가 순서

현재는 영어권 대형 블로그보다 한국어 기업 기술 블로그를 먼저 늘립니다. 한글 문제상황 검색, 한영 기술명 검색, 국내 기업 사례 비교가 TechCase의 초기 차별점에 더 직접적으로 연결되기 때문입니다.

우선 seed 추가 대상:

```text
naver-cloud-platform-tech-blog
zigbang-tech-blog
wantedlab-tech-blog
coupang-engineering-blog
lunit-team-blog
gmarket-tech-blog
netmarble-tech-blog
```

이 source들은 RSS 또는 Medium feed에서 entry가 확인되었습니다. 다만 Medium 기반 source는 최신 10개 중심으로 내려올 가능성이 높으므로, 과거 글 전체 수집이 필요해지면 Medium archive 또는 HTML 목록 수집을 별도로 검토합니다.

확인 결과 Medium archive HTML은 Cloudflare challenge가 걸릴 수 있어 서버 crawler로 안정적으로 수집하기 어렵습니다. Medium 기반 source는 우선 최신 feed 중심으로 수집하고, 과거 글 전체 수집은 공식 API 또는 허용 가능한 archive 접근 방식을 별도로 검토합니다.

반대로 G마켓과 넷마블은 RSS 최신 글 한계를 넘어설 수 있습니다.

```text
G마켓: sitemap.xml 기반 article URL 수집 가능
넷마블: RSS 페이지네이션 수집 가능
```

추가로 확인된 한국어 source:

```text
뱅크샐러드: RSS 78개 수집 가능
인프랩: RSS 42개 수집 가능
Upstage: sitemap에서 한국어 블로그 76개 수집 가능
```

Sendbird는 sitemap에 글이 많지만 제품/마케팅 콘텐츠가 많이 섞입니다. 기술 사례 검색 품질을 흐릴 수 있으므로, `engineering`, `SDK`, `API`, `infrastructure` 성격의 글만 고르는 필터가 생긴 뒤 추가하는 편이 좋습니다.

## 이후 추천 추가 순서

가장 현실적인 다음 순서는 다음과 같습니다.

1. 한국어 RSS source를 먼저 seed에 추가합니다.
2. `crawl:rss --source ...`로 source별 수집량과 summary 품질을 확인합니다.
3. `keywords:extract`, `llm:summarize --limit 100`, `search:reindex`, `suggest:reindex`를 source 단위로 실행합니다.
4. 검색 평가 데이터셋에 신규 한국어 source 기반 쿼리를 추가합니다.
5. 남은 한국어 P1 후보를 probe해서 실제 feed URL을 확정합니다.
6. RSS가 없는 P2 후보를 위해 `html_list` 수집기를 설계합니다.

한국어 source는 공식성과 RSS 품질 확인을 먼저 거친 뒤 추가합니다. 국내 후보는 서비스 차별점에 중요하지만, 블로그 URL 변경과 feed 부재가 상대적으로 많아서 probe 단계가 먼저 필요합니다.

## source probe에서 확인할 항목

후보가 늘어나면 수동 확인만으로는 한계가 있으므로, source 추가 전에 다음을 자동 점검하는 probe 명령이 필요합니다.

```text
site_url 접근 가능 여부
RSS/Atom autodiscovery link 존재 여부
feed_url 후보 응답 status
feed entry 개수
entry title/url/published_at 존재 여부
summary에 HTML boilerplate가 섞이는지 여부
content:encoded 또는 상세 본문 제공 여부
robots.txt 또는 접근 제한 여부
```

probe 결과가 안정적인 source만 seed에 넣고, 불안정한 source는 `deferred`로 남깁니다.
