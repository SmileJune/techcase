# 스케줄러 운영 설계

TechCase는 새 기술 블로그 글이 올라오면 다음 순서로 후처리합니다.

```text
RSS 수집
-> 신규 article 저장
-> 키워드 추출
-> 신규 article만 LLM 사례 요약 생성
-> Elasticsearch 재색인
```

## 실행 명령

스케줄러에서 실행할 기본 명령은 다음과 같습니다.

```bash
npm run ingest:scheduled
```

특정 source만 확인할 수도 있습니다.

```bash
npm run ingest:scheduled -- --source daangn-tech-blog
```

LLM 요약 생성 수를 제한할 수 있습니다.

```bash
npm run ingest:scheduled -- --summary-limit 20
```

LLM 비용을 쓰지 않고 수집, 키워드 추출, 재색인만 실행할 수도 있습니다.

```bash
npm run ingest:scheduled -- --skip-llm
```

## 신규 글만 요약하는 방식

`ingest:scheduled`는 실행 시작 시각을 기록합니다.

```text
started_at = now()
```

그 다음 RSS 수집을 실행하고, 이번 실행 중 새로 생성된 article만 LLM 요약 대상으로 선택합니다.

```text
Article.created_at >= started_at
```

따라서 기존에 수집되어 있었지만 아직 요약되지 않은 과거 글은 스케줄러에서 자동으로 요약하지 않습니다. 과거 글을 별도로 요약하고 싶을 때는 기존 `llm:summarize` 명령을 직접 실행합니다.

```bash
npm run llm:summarize -- --source woowa-tech-blog --limit 10
```

## 새 글이 없을 때

수집 결과 `created=0`, `updated=0`이면 후처리를 건너뜁니다.

```text
keyword_articles=0
keywords=0
summary_selected=0
summary_generated=0
indexed=0
```

이렇게 하는 이유는 다음과 같습니다.

- OpenAI API 비용을 낭비하지 않습니다.
- Elasticsearch 재색인을 불필요하게 반복하지 않습니다.
- source가 많아져도 주기 실행 비용을 낮게 유지할 수 있습니다.

## systemd timer 예시

초기 AWS 배포에서는 private EC2 내부에서 systemd timer로 실행하는 방식을 우선 사용합니다.

`/etc/systemd/system/techcase-ingest.service`

```ini
[Unit]
Description=TechCase scheduled ingest
After=network-online.target

[Service]
Type=oneshot
WorkingDirectory=/home/ec2-user/techcase
EnvironmentFile=/home/ec2-user/techcase/apps/backend/.env
ExecStart=/usr/bin/npm run ingest:scheduled -- --summary-limit 20
```

`/etc/systemd/system/techcase-ingest.timer`

```ini
[Unit]
Description=Run TechCase scheduled ingest every hour

[Timer]
OnCalendar=hourly
Persistent=true

[Install]
WantedBy=timers.target
```

활성화:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now techcase-ingest.timer
```

수동 실행:

```bash
sudo systemctl start techcase-ingest.service
```

로그 확인:

```bash
journalctl -u techcase-ingest.service -n 100
```

## 운영 기준

초기 추천 주기:

```text
1시간 또는 3시간 간격
```

초기 추천 LLM 제한:

```text
summary-limit = 20
```

이유:

- 기업 기술 블로그는 글 발행 빈도가 높지 않습니다.
- RSS 수집 대상이 늘어나도 새 글 수는 많지 않을 가능성이 큽니다.
- 새 글이 갑자기 많이 들어올 경우 LLM 비용을 제한할 수 있습니다.

## 향후 개선

수집량이 늘어나면 다음을 검토합니다.

```text
source별 실행 주기 분리
article 단위 incremental keyword extraction
article 단위 Elasticsearch partial indexing
LLM 요약 실패 재시도 큐
content_type 기반 technical_case 우선 요약
ECS Scheduled Task 또는 EventBridge Scheduler 전환
```
