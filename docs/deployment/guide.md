# 🚀 Deployment Guide

## Production Deployment of SpiralCortex

This guide provides comprehensive instructions for deploying SpiralCortex in production environments, including Docker containerization, orchestration, monitoring, and scaling strategies.

---

## 🏗️ Architecture Overview

### **Production Stack**

```
┌─────────────────────────────────────────────────┐
│              EXTERNAL LOAD BALANCER             │
│  (AWS ALB / Nginx / Cloud Load Balancer)        │
├─────────────────────────────────────────────────┤
│              API GATEWAY LAYER                  │
│  ┌─────────────────────────────────────────┐   │
│  │ SpiralCortex Fusion API (FastAPI)      │   │
│  │ - /api/v1/fusion                     │   │
│  │ - /api/v1/emotion                    │   │
│  │ - /api/v1/risk                       │   │
│  │ - /api/v1/ethics                     │   │
│  └─────────────────────────────────────────┘   │
├─────────────────────────────────────────────────┤
│              MICROSERVICES LAYER                │
│  ┌─────────────────────────────────────────┐   │
│  │ SpiralBrain-Nexus (Emotional AI)       │   │
│  │ SpiralCode-X (Risk Analysis)           │   │
│  │ Ethical Regulator (Governance)         │   │
│  └─────────────────────────────────────────┘   │
├─────────────────────────────────────────────────┤
│              INFRASTRUCTURE LAYER               │
│  ┌─────────────────────────────────────────┐   │
│  │ PostgreSQL (Data)                      │   │
│  │ Redis (Cache)                          │   │
│  │ Elasticsearch (Search)                 │   │
│  │ MinIO (Object Storage)                 │   │
│  └─────────────────────────────────────────┘   │
├─────────────────────────────────────────────────┤
│              MONITORING & LOGGING               │
│  ┌─────────────────────────────────────────┐   │
│  │ Prometheus (Metrics)                   │   │
│  │ Grafana (Dashboards)                   │   │
│  │ ELK Stack (Logs)                       │   │
│  │ Jaeger (Tracing)                       │   │
│  └─────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘
```

### **Deployment Options**

1. **Docker Compose** (Development/Testing)
2. **Kubernetes** (Production)
3. **AWS ECS/Fargate** (Cloud)
4. **Azure Container Instances** (Cloud)
5. **Google Cloud Run** (Serverless)

---

## 🐳 Docker Deployment

### **Prerequisites**

```bash
# Required software
docker >= 20.10.0
docker-compose >= 2.0.0
git >= 2.30.0

# System requirements
- 16GB RAM minimum
- 4 CPU cores minimum
- 100GB storage minimum
- NVIDIA GPU (optional, for acceleration)
```

### **Quick Start with Docker Compose**

```bash
# Clone the repository
git clone https://github.com/your-org/spiralcortex.git
cd spiralcortex

# Copy environment template
cp .env.example .env

# Edit configuration
nano .env  # Configure your settings

# Start all services
docker-compose up -d

# Check service health
docker-compose ps

# View logs
docker-compose logs -f spiralcortex-fusion
```

### **Environment Configuration**

```bash
# .env file configuration
# Database
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=spiralcortex
POSTGRES_USER=spiralcortex
POSTGRES_PASSWORD=your_secure_password

# Redis Cache
REDIS_URL=redis://localhost:6379/0

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
API_WORKERS=4

# Security
JWT_SECRET_KEY=your_jwt_secret_key
API_KEY=your_api_key

# Monitoring
PROMETHEUS_ENABLED=true
GRAFANA_ADMIN_PASSWORD=admin

# Model Configuration
MODEL_CACHE_DIR=/app/models
EMOTION_MODEL_PATH=/app/models/emotion_v2
RISK_MODEL_PATH=/app/models/risk_v3
```

### **Docker Compose Services**

```yaml
version: '3.8'

services:
  # Main Fusion API
  spiralcortex-fusion:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    environment:
      - ENVIRONMENT=production
    depends_on:
      - postgres
      - redis
    volumes:
      - ./models:/app/models:ro
      - ./logs:/app/logs

  # Database
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: spiralcortex
      POSTGRES_USER: spiralcortex
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  # Cache
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

  # Monitoring
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    environment:
      GF_SECURITY_ADMIN_PASSWORD: ${GRAFANA_ADMIN_PASSWORD}
    volumes:
      - grafana_data:/var/lib/grafana

volumes:
  postgres_data:
  redis_data:
  grafana_data:
```

---

## ☸️ Kubernetes Deployment

### **Prerequisites**

```bash
# Required tools
kubectl >= 1.24.0
helm >= 3.9.0
kustomize >= 4.5.0

# Cluster requirements
- Kubernetes 1.24+
- 3 worker nodes minimum
- 32GB RAM total
- 8 CPU cores total
- 500GB storage
```

### **Helm Installation**

```bash
# Add Helm repository
helm repo add spiralcortex https://charts.spiralcortex.ai
helm repo update

# Install with default values
helm install spiralcortex spiralcortex/spiralcortex

# Install with custom values
helm install spiralcortex spiralcortex/spiralcortex \
  --values custom-values.yaml \
  --namespace spiralcortex \
  --create-namespace
```

### **Custom Values Configuration**

```yaml
# custom-values.yaml
global:
  environment: production
  imageRegistry: your-registry.com

fusion:
  replicaCount: 3
  image:
    tag: "v2.1.0"
  resources:
    requests:
      memory: "2Gi"
      cpu: "1000m"
    limits:
      memory: "4Gi"
      cpu: "2000m"

database:
  enabled: true
  postgresql:
    auth:
      database: spiralcortex
      username: spiralcortex
      password: "your-secure-password"

cache:
  enabled: true
  redis:
    auth:
      password: "your-redis-password"

monitoring:
  enabled: true
  prometheus:
    enabled: true
  grafana:
    enabled: true
    adminPassword: "your-grafana-password"

ingress:
  enabled: true
  className: nginx
  hosts:
    - host: api.spiralcortex.com
      paths:
        - path: /
          pathType: Prefix
```

### **Scaling Configuration**

```yaml
# Horizontal Pod Autoscaling
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: spiralcortex-fusion-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: spiralcortex-fusion
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

---

## ☁️ Cloud Deployments

### **AWS ECS/Fargate**

```yaml
# Task Definition
{
  "family": "spiralcortex-fusion",
  "taskRoleArn": "arn:aws:iam::123456789012:role/ecsTaskExecutionRole",
  "executionRoleArn": "arn:aws:iam::123456789012:role/ecsTaskExecutionRole",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "2048",
  "memory": "4096",
  "containerDefinitions": [
    {
      "name": "fusion-api",
      "image": "123456789012.dkr.ecr.us-east-1.amazonaws.com/spiralcortex:latest",
      "essential": true,
      "portMappings": [
        {
          "containerPort": 8000,
          "hostPort": 8000,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {"name": "ENVIRONMENT", "value": "production"},
        {"name": "DATABASE_URL", "value": "postgresql://..."}
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/spiralcortex",
          "awslogs-region": "us-east-1",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ]
}
```

### **Azure Container Instances**

```bash
# Deploy to ACI
az container create \
  --resource-group spiralcortex-rg \
  --name spiralcortex-fusion \
  --image yourregistry.azurecr.io/spiralcortex:latest \
  --cpu 2 \
  --memory 4 \
  --registry-login-server yourregistry.azurecr.io \
  --registry-username yourusername \
  --registry-password yourpassword \
  --ports 8000 \
  --environment-variables \
    ENVIRONMENT=production \
    DATABASE_URL=postgresql://...
```

### **Google Cloud Run**

```bash
# Build and deploy
gcloud builds submit --tag gcr.io/your-project/spiralcortex
gcloud run deploy spiralcortex-fusion \
  --image gcr.io/your-project/spiralcortex \
  --platform managed \
  --port 8000 \
  --cpu 2 \
  --memory 4Gi \
  --max-instances 10 \
  --set-env-vars ENVIRONMENT=production
```

---

## 🔧 Configuration Management

### **Configuration Hierarchy**

```
1. Environment Variables (highest priority)
2. Configuration Files
3. Default Values (lowest priority)
```

### **Configuration Files**

```python
# config/production.yaml
app:
  name: "SpiralCortex Fusion API"
  version: "2.1.0"
  environment: "production"

api:
  host: "0.0.0.0"
  port: 8000
  workers: 4
  timeout: 30
  cors_origins:
    - "https://app.spiralcortex.com"
    - "https://dashboard.spiralcortex.com"

database:
  url: "postgresql://user:pass@host:5432/db"
  pool_size: 20
  max_overflow: 30
  pool_timeout: 30

cache:
  url: "redis://host:6379/0"
  ttl: 3600
  max_connections: 20

models:
  emotion:
    path: "/app/models/emotion_v2"
    version: "2.1.0"
  risk:
    path: "/app/models/risk_v3"
    version: "3.0.1"
  ethics:
    path: "/app/models/ethics_v1"
    version: "1.2.0"

monitoring:
  prometheus:
    enabled: true
    path: "/metrics"
  jaeger:
    enabled: true
    service_name: "spiralcortex-fusion"
```

### **Secrets Management**

```bash
# Using Kubernetes secrets
kubectl create secret generic spiralcortex-secrets \
  --from-literal=database-password=your-db-password \
  --from-literal=jwt-secret=your-jwt-secret \
  --from-literal=api-key=your-api-key

# Using AWS Secrets Manager
# Using Azure Key Vault
# Using Google Secret Manager
```

---

## 📊 Monitoring & Observability

### **Metrics Collection**

```python
# Prometheus metrics
from prometheus_client import Counter, Histogram, Gauge

# Request metrics
REQUEST_COUNT = Counter(
    'spiralcortex_requests_total',
    'Total number of requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'spiralcortex_request_duration_seconds',
    'Request duration in seconds',
    ['method', 'endpoint']
)

# Model metrics
MODEL_ACCURACY = Gauge(
    'spiralcortex_model_accuracy',
    'Model prediction accuracy',
    ['model_type']
)

ETHICAL_VIOLATIONS = Counter(
    'spiralcortex_ethical_violations_total',
    'Total number of ethical violations detected'
)
```

### **Grafana Dashboards**

Key dashboards to set up:

1. **System Performance**
   - CPU/Memory usage
   - Response times
   - Error rates
   - Throughput

2. **Model Performance**
   - Prediction accuracy
   - Model drift detection
   - Feature importance
   - Training metrics

3. **Business Metrics**
   - API usage by endpoint
   - User satisfaction scores
   - Ethical compliance rates
   - Revenue impact

4. **Infrastructure**
   - Database performance
   - Cache hit rates
   - Network latency
   - Storage usage

### **Logging Configuration**

```python
# Structured logging
import structlog

logger = structlog.get_logger()

# Request logging
logger.info(
    "API request processed",
    user_id=user_id,
    endpoint=endpoint,
    response_time=response_time,
    status_code=status_code,
    model_accuracy=accuracy
)

# Error logging
logger.error(
    "Model prediction failed",
    user_id=user_id,
    model_type=model_type,
    error=str(e),
    input_data=input_summary
)
```

---

## 🔒 Security Configuration

### **Network Security**

```yaml
# Kubernetes Network Policies
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: spiralcortex-fusion-policy
spec:
  podSelector:
    matchLabels:
      app: spiralcortex-fusion
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: ingress-nginx
    ports:
    - protocol: TCP
      port: 8000
  egress:
  - to:
    - podSelector:
        matchLabels:
          app: postgres
    ports:
    - protocol: TCP
      port: 5432
  - to:
    - podSelector:
        matchLabels:
          app: redis
    ports:
    - protocol: TCP
      port: 5432
```

### **API Security**

```python
# FastAPI security middleware
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    # Verify JWT token
    try:
        payload = jwt.decode(credentials.credentials, JWT_SECRET, algorithms=["HS256"])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Rate limiting
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.middleware("http")
async def add_rate_limiting(request: Request, call_next):
    # Rate limiting logic
    pass
```

### **Data Security**

- **Encryption at Rest**: Database and storage encryption
- **Encryption in Transit**: TLS 1.3 for all communications
- **Data Masking**: PII protection in logs
- **Access Controls**: Role-based access control (RBAC)

---

## 🚀 Scaling Strategies

### **Horizontal Scaling**

```yaml
# Kubernetes HPA for automatic scaling
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: spiralcortex-autoscaler
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: spiralcortex-fusion
  minReplicas: 3
  maxReplicas: 50
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

### **Vertical Scaling**

- **CPU Optimization**: Increase CPU cores for compute-intensive workloads
- **Memory Scaling**: Add RAM for larger model caching
- **GPU Acceleration**: NVIDIA GPUs for model inference acceleration

### **Database Scaling**

```sql
-- PostgreSQL scaling configuration
ALTER SYSTEM SET max_connections = '200';
ALTER SYSTEM SET shared_buffers = '2GB';
ALTER SYSTEM SET effective_cache_size = '6GB';
ALTER SYSTEM SET work_mem = '32MB';
ALTER SYSTEM SET maintenance_work_mem = '512MB';
```

### **Caching Strategies**

```python
# Multi-level caching
from cachetools import TTLCache, LRUCache

# Application cache
app_cache = TTLCache(maxsize=10000, ttl=3600)

# Model cache
model_cache = LRUCache(maxsize=100)

# Database query cache
query_cache = TTLCache(maxsize=5000, ttl=1800)
```

---

## 🔄 Backup & Recovery

### **Database Backup**

```bash
# Automated PostgreSQL backup
#!/bin/bash
BACKUP_DIR="/backups"
DATE=$(date +%Y%m%d_%H%M%S)
pg_dump -h localhost -U spiralcortex -d spiralcortex > $BACKUP_DIR/spiralcortex_$DATE.sql

# Compress and upload to S3
gzip $BACKUP_DIR/spiralcortex_$DATE.sql
aws s3 cp $BACKUP_DIR/spiralcortex_$DATE.sql.gz s3://spiralcortex-backups/
```

### **Model Backup**

```bash
# Model versioning and backup
#!/bin/bash
MODEL_DIR="/app/models"
BACKUP_DIR="/backups/models"

# Create timestamped backup
cp -r $MODEL_DIR $BACKUP_DIR/models_$(date +%Y%m%d_%H%M%S)

# Upload to cloud storage
aws s3 sync $BACKUP_DIR s3://spiralcortex-models/
```

### **Disaster Recovery**

```yaml
# Disaster recovery configuration
disasterRecovery:
  enabled: true
  backupSchedule: "0 2 * * *"  # Daily at 2 AM
  retentionPeriod: "30d"
  crossRegionReplication: true
  rto: "15m"  # Recovery Time Objective
  rpo: "5m"  # Recovery Point Objective
```

---

## 🧪 Testing & Validation

### **Pre-Deployment Testing**

```bash
# Health checks
curl -f http://localhost:8000/health

# Load testing
ab -n 10000 -c 100 http://localhost:8000/api/v1/fusion

# Model validation
python -m pytest tests/model_tests.py -v

# Integration testing
docker-compose -f docker-compose.test.yml up --abort-on-container-exit
```

### **Performance Testing**

```python
# Load testing script
import asyncio
import aiohttp
import time

async def load_test():
    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        tasks = []

        for i in range(1000):
            task = asyncio.create_task(make_request(session, i))
            tasks.append(task)

        results = await asyncio.gather(*tasks)
        end_time = time.time()

        print(f"Completed {len(results)} requests in {end_time - start_time:.2f} seconds")
        print(f"Average RPS: {len(results) / (end_time - start_time)}")
```

---

## 📞 Support & Troubleshooting

### **Common Issues**

1. **High Memory Usage**
   - Check model cache size
   - Monitor connection pools
   - Review batch processing settings

2. **Slow Response Times**
   - Check database query performance
   - Monitor cache hit rates
   - Review model inference times

3. **Connection Pool Exhaustion**
   - Increase database connection limits
   - Implement connection pooling
   - Add retry logic with backoff

### **Support Resources**

- **Documentation**: https://docs.spiralcortex.ai
- **Community Forum**: https://community.spiralcortex.ai
- **Enterprise Support**: support@spiralcortex.ai
- **Status Page**: https://status.spiralcortex.ai

### **Emergency Contacts**

- **Critical Issues**: +1-800-SPIRAL-911
- **Security Incidents**: security@spiralcortex.ai
- **System Outages**: ops@spiralcortex.ai

---

## 📈 Maintenance & Updates

### **Update Strategy**

```bash
# Rolling update procedure
kubectl set image deployment/spiralcortex-fusion \
  spiralcortex-fusion=your-registry.com/spiralcortex:v2.2.0

# Monitor rollout
kubectl rollout status deployment/spiralcortex-fusion

# Rollback if needed
kubectl rollout undo deployment/spiralcortex-fusion
```

### **Scheduled Maintenance**

- **Weekly**: Security patches and minor updates
- **Monthly**: Feature releases and model updates
- **Quarterly**: Major version upgrades
- **Annually**: Infrastructure modernization

### **Monitoring Maintenance Windows**

```yaml
# Maintenance window configuration
maintenance:
  enabled: true
  schedule: "0 2 * * 0"  # Sundays at 2 AM
  duration: "2h"
  notification:
    email: ops@company.com
    slack: "#ops-alerts"
  auto_approval: false
```

---

This deployment guide provides everything needed to successfully deploy SpiralCortex in production environments. The system is designed for high availability, scalability, and security, making it suitable for enterprise-grade cognitive AI applications.