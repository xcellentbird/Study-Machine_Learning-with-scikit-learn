git init: 로컬 저장소 생성
git status: 현 주소에서 add할 수 있는 파일을 나타냄
git add '파일이름': 현 주소의 해당 파일을 staging
git add -A: 현 주소의 모든 파일을 staging
git commit -m "message": staging한 파일을 local repo에 commit한다. 커밋 message와 함께
git log: commit 기록 확인하기
git branch "branch이름": 해당 이름으로 새로운 branch를 만든다.gg
git checkout "branch name": branch를 전환
git merge "대상 bracnh name": 해당 branch의 내용을 현재의 branch에 반영힌다.
git branch -d "branch name": 해당 branch를 삭제한다
git remote add "원격 저장소의 별칭" "원격 저장소의 주소": 원겨 저장소와 연결
git remote -v: 연결된 원격 저장소의 정보를git 볼 수 있다.
git push "원격 저장소 이름" "branch 이름": 해당 branch를 로컬 저장소에서 원격 저장소로 push
git branch -M 'branch 이름': 해당 브랜치르 만들고 이동

folk 기능: 타인의 repo를 복사해서 자신의 repo로 가져온다. 이 때 출처 정보가 담겨있다.

git clone "원격 저장소 주소" "별칭": 원격 저장소의 코드를 로커 저장소로 가져온다.
