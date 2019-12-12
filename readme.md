## 설치 요건
> pip3 install gitpython

`git-run.py`
> 설계는 리모트의 상태를 5분마다 체크하여 tag의 변화가 있을 때 깃풀 명령을 실행 함. 
> 파일의 위치는 대상 리포외의 장소에 저장하고 다음 명령을 실행
`nohup python3 git-run.py &`

> 서비스 형태로 등록하여 서버 재시작후에도 가동 되도록 하는 것은 미제입니다.

## 변경 가능한 부분

> 리포 패스 정의
` repo = git.Repo('path/to/repo')`

> 상태 변화 체크 하는 시간 설정
`time.sleep(60*5)`

이상입니다.