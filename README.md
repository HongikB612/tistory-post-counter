# tistory-post-counter
Tistory 블로그 게시물 정보를 받아오는 프로그램
모각글 집계용

## 사용법

### 1. Tistory API 키 발급
[https://www.tistory.com/guide/api/manage/register](https://www.tistory.com/guide/api/manage/register) 에 들어가서, 앱을 등록한 후 키를 발급받습니다.

이때 **Redirect URI**를 설정해줘야 하는데, 이는 자신이 원하는 주소를 입력하면 됩니다.
저는 제 블로그 주소인 `https://nx006.tistory.com/` 로 입력했습니다.

### 2. `.env` 파일 생성
`.env` 파일을 생성하고, 다음과 같이 입력합니다.

```
CLIENT_ID=발급받은 클라이언트 ID
SECRET_KEY=발급받은 시크릿 키
REDIRECT_URI=등록한 Redirect URI
```

예를 들어 저는 다음과 같이 입력했습니다.

```
CLIENT_ID=1234567890abcdef1234
SECRET_KEY=1234567890abcdef1234567890abcdef12345678
REDIRECT_URI=https://nx006.tistory.com/
```

### 3. 실행 및 Authorization Code 발급

main.py를 실행합니다. 자동으로 브라우저가 열리고, Tistory 계정으로 로그인하라고 하면 로그인합니다.

Authorization Code를 발급받기 위한 OAuth 창이 뜹니다. **허가하기**를 누르면, 아까 전 설정해둔 Redirect URI로 이동합니다.

이때 주소창에 `code=`와 `&status=` 사이에 붙은 문자열이 Authorization Code입니다. 이를 복사해둡니다.

예를 들어 다음과 같이 되어 있습니다.
```text
https://nx006.tistory.com/?code=1234567890abcdef1234567890abcdef12345678&status=200
```

위에서 `code=`와 `&status` 사이에 있는 `1234567890abcdef1234567890abcdef12345678`이 Authorization Code입니다.

### 4. 터미널에 Authorization Code 입력

main.py를 실행한 터미널로 돌아오면, `Input provided code: `라는 문구와 함께 사용자의 입력을 기다립니다. 여기에 방금 복사해둔 Authorization Code를 붙여넣습니다.

### 5. 결과 확인
만약 Authorization Code가 유효하다면, 정상적인 ACCESS_TOKEN이 발급될 것입니다. 터미널에서 이를 확인할 수 있습니다. 원한다면 이를 `.env` 파일에 추가해줍니다.

```text
CLIENT_ID=1234567890abcdef1234
SECRET_KEY=1234567890abcdef1234567890abcdef12345678
REDIRECT_URI=https://nx006.tistory.com/
ACCESS_TOKEN=1234567890
```

이렇게 `.env`에 추가해놓으면, 다음부터는 Authorization Code를 입력할 필요 없이 바로 실행할 수 있습니다.

### 6. 게시물 정보 확인
main.py를 실행하면, 리스트에 포함된 블로그 게시물 정보를 확인할 수 있습니다.
리스트 명단은 블로그 이름으로 되어 있으며, 수정할 수 있습니다.