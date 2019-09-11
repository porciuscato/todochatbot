# Todo list & chatbot
챗봇과 결합된 todo list

## Teleram Chatbot Webhook 사용법
1. webhook 설정
- setWebhook
```
https://api.telegram.org/bot<token>/setWebhook?url=<ngrok의https주소>/<token>/
(마지막 '/' 반드시 필요)
```
2. webhook 정보조회
- getWebhookInfo

3. webhook 삭제
- deleteWebhook