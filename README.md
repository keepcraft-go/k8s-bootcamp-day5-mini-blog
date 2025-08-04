# k8s-bootcamp-day5-mini-blog

## 개요
쿠버네티스를 활용한 미니 블로그 실습용 프로젝트입니다.

## 실습 파일 구성
- `backend/`: Flask API 서버 코드
- `frontend/`: Nginx + HTML + JS 코드
- `k8s/`: Deployment & Service YAML
- `docs/`: 실습 설명 문서 및 아키텍처

## 실행 방법
```bash
cd k8s-bootcamp-day5-mini-blog
docker build -t yourname/backend:latest backend
docker build -t yourname/frontend:latest frontend
docker push yourname/backend:latest
docker push yourname/frontend:latest
kubectl apply -f k8s/01_namespace.yaml  # optional
kubectl apply -f k8s/02_backend-deployment.yaml
kubectl apply -f k8s/03_frontend-deployment.yaml
