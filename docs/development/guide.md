# 🛠️ Development Guide

## Building and Extending SpiralBrain

This guide provides comprehensive information for developers working with SpiralBrain, including setup, development workflows, testing, and contribution guidelines.

---

## 🚀 Quick Start Development

### **Prerequisites**

```bash
# Required software
Python >= 3.9, <= 3.11
Node.js >= 16.0 (for frontend development)
Docker >= 20.10
docker-compose >= 2.0
git >= 2.30

# System requirements
- 8GB RAM minimum
- 4 CPU cores minimum
- 20GB storage minimum
- GPU recommended for model training
```

### **Development Environment Setup**

```bash
# Clone the repository
git clone https://github.com/your-org/spiralbrain.git
cd spiralbrain

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Start development services
docker-compose -f docker-compose.dev.yml up -d

# Run database migrations
alembic upgrade head

# Start the development server
python -m uvicorn spiral_brain_core.main:app --reload --host 0.0.0.0 --port 8000
```

### **Development Docker Compose**

```yaml
# docker-compose.dev.yml
version: '3.8'

services:
  # Development database with persistent data
  postgres-dev:
    image: postgres:15-alpine
    environment:
    POSTGRES_DB: spiralbrain_dev
      POSTGRES_USER: developer
      POSTGRES_PASSWORD: dev_password
    volumes:
      - postgres_dev_data:/var/lib/postgresql/data
    ports:
      - "5433:5432"  # Different port to avoid conflicts

  # Redis for development
  redis-dev:
    image: redis:7-alpine
    ports:
      - "6380:6379"  # Different port for development

  # Elasticsearch for development
  elasticsearch-dev:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.7.0
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
      - "ES_JAVA_OPTS=-Xms256m -Xmx256m"
    ports:
      - "9201:9200"  # Different port for development

volumes:
  postgres_dev_data:
```

---

## 🏗️ Project Structure

### **Core Components**

```
SpiralBrain-v2.0/
├── spiral_brain_core/       # Main fusion engine (v2)
│   ├── main.py                # FastAPI application entrypoint (app)
│   └── __init__.py
├── spiral_cortex_core/         # Legacy fusion engine (archived)
│   ├── cortex_fusion.py       # Legacy FastAPI application
│   ├── fusion_engine.py       # Legacy cognitive fusion logic
│   ├── models/                # Legacy Pydantic models
│   └── tests/                 # Legacy unit tests
├── SpiralBrain-Nexus/          # Emotional intelligence engine
│   ├── adaptive_planner.py     # Learning orchestration
│   ├── biofeedback_*.py        # Physiological computing
│   └── emotional_*.py          # SEC calibration
├── SpiralCode-X/              # Risk analysis engine
│   ├── risk_analyzer.py       # Ensemble risk modeling
│   ├── active_learning.py     # Continuous learning
│   └── validation_*.py        # Model validation
├── docs/                      # Documentation
├── monitoring/                # Observability stack
├── nginx/                     # Reverse proxy config
└── docker-compose.yml         # Production deployment
```

### **Key Files and Their Purpose**

| File/Component | Purpose | Key Capabilities |
|---------------|---------|------------------|
| `cortex_fusion.py` | Main API server | RESTful endpoints for all cognitive functions |
| `fusion_engine.py` | Core fusion logic | Multi-modal decision integration |
| `adaptive_planner.py` | Learning orchestration | Dynamic model adaptation |
| `biofeedback_*.py` | Physiological computing | Real-time emotional monitoring |
| `risk_analyzer.py` | Risk assessment | Ensemble prediction modeling |
| `emotional_*.py` | SEC calibration | Symbolic-emotional processing |

---

## 🔧 Development Workflows

### **Adding New Cognitive Capabilities**

```python
# Example: Adding a new emotion analysis model
from spiral_cortex_core.models.emotion import EmotionAnalyzer
from spiral_cortex_core.fusion_engine import FusionEngine

class AdvancedEmotionAnalyzer(EmotionAnalyzer):
    """Advanced emotion analysis with cultural context."""

    def __init__(self):
        super().__init__()
        self.cultural_models = self._load_cultural_models()

    def analyze_with_culture(self, text: str, culture: str) -> dict:
        """Analyze emotion with cultural context."""
        base_analysis = self.analyze(text)

        # Apply cultural calibration
        cultural_adjustment = self.cultural_models[culture].predict(base_analysis)

        return {
            **base_analysis,
            "cultural_context": culture,
            "adjusted_valence": base_analysis["valence"] + cultural_adjustment
        }

# Integration with fusion engine
fusion_engine = FusionEngine()
fusion_engine.register_analyzer("advanced_emotion", AdvancedEmotionAnalyzer())
```

### **Extending the Fusion Engine**

```python
# Adding new fusion modalities
from spiral_cortex_core.fusion_engine import FusionEngine, FusionModality

class MarketSentimentModality(FusionModality):
    """Market sentiment analysis modality."""

    def __init__(self):
        self.sentiment_model = self._load_market_model()

    def process(self, input_data: dict) -> dict:
        """Process market data for sentiment."""
        text = input_data.get("market_news", "")
        sentiment = self.sentiment_model.predict(text)

        return {
            "modality": "market_sentiment",
            "sentiment_score": sentiment,
            "confidence": 0.89,
            "market_impact": self._calculate_impact(sentiment)
        }

# Register new modality
fusion_engine.add_modality(MarketSentimentModality())
```

### **Creating Custom Ethical Rules**

```python
# Custom ethical governance rules
from spiral_cortex_core.ethical_regulator import EthicalRegulator, EthicalRule

class MarketManipulationRule(EthicalRule):
    """Detect and prevent market manipulation."""

    def evaluate(self, decision_context: dict) -> dict:
        """Evaluate decision for market manipulation risk."""
        trade_volume = decision_context.get("trade_volume", 0)
        price_impact = decision_context.get("price_impact", 0)

        # Check for manipulation patterns
        manipulation_score = self._calculate_manipulation_risk(
            trade_volume, price_impact
        )

        return {
            "rule": "market_manipulation_prevention",
            "violation_level": "high" if manipulation_score > 0.8 else "low",
            "recommended_action": "block_trade" if manipulation_score > 0.8 else "monitor",
            "justification": f"Manipulation risk score: {manipulation_score:.2f}"
        }

# Register custom rule
regulator = EthicalRegulator()
regulator.add_rule(MarketManipulationRule())
```

---

## 🧪 Testing Strategy

### **Test Categories**

```python
# Unit Tests - Test individual components
def test_emotion_analyzer():
    analyzer = EmotionAnalyzer()
    result = analyzer.analyze("I feel happy today")

    assert result["valence"] > 0.5
    assert "joy" in result["emotions"]

# Integration Tests - Test component interactions
def test_fusion_pipeline():
    fusion = FusionEngine()
    input_data = {
        "text": "Market is crashing",
        "context": "trading_decision"
    }

    result = fusion.fuse(input_data)

    assert "fused_score" in result
    assert "ethical_assessment" in result
    assert result["confidence"] > 0.8

# End-to-End Tests - Test complete workflows
def test_trading_workflow():
    # Simulate complete trading decision workflow
    market_data = get_market_data()
    emotional_state = get_trader_emotion()

    decision = cortex.fuse({
        "market_data": market_data,
        "emotional_context": emotional_state,
        "risk_tolerance": "moderate"
    })

    assert decision["action"] in ["buy", "sell", "hold"]
    assert decision["ethical_clearance"] == True
```

### **Running Tests**

```bash
# Run all tests
pytest

# Run specific test categories
pytest tests/unit/          # Unit tests
pytest tests/integration/   # Integration tests
pytest tests/e2e/          # End-to-end tests

# Run with coverage
pytest --cov=spiral_cortex_core --cov-report=html

# Run performance tests
pytest tests/performance/ -v

# Run tests in parallel
pytest -n auto

# Run tests with different Python versions
tox
```

### **Test Configuration**

```ini
# pytest.ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts =
    --strict-markers
    --strict-config
    --cov=spiral_cortex_core
    --cov-report=term-missing
    --cov-report=html:htmlcov
markers =
    unit: Unit tests
    integration: Integration tests
    e2e: End-to-end tests
    performance: Performance tests
    slow: Slow running tests
```

---

## 🔍 Code Quality & Standards

### **Linting and Formatting**

```bash
# Run all quality checks
pre-commit run --all-files

# Individual tools
black .                    # Code formatting
isort .                    # Import sorting
flake8 .                   # Linting
mypy .                     # Type checking
bandit .                   # Security scanning

# Auto-fix issues
black .
isort .
```

### **Code Quality Tools Configuration**

```ini
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files

  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
        language_version: python3.9

  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.3.0
    hooks:
      - id: mypy
```

### **Type Hints and Documentation**

```python
from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field

class FusionRequest(BaseModel):
    """Request model for cognitive fusion."""

    text: str = Field(..., description="Input text for analysis")
    context: Optional[str] = Field(None, description="Contextual information")
    modalities: List[str] = Field(
        default_factory=lambda: ["emotion", "risk", "ethics"],
        description="Fusion modalities to apply"
    )
    ethical_constraints: Dict[str, Union[str, float]] = Field(
        default_factory=dict,
        description="Ethical constraints for the decision"
    )

    class Config:
        schema_extra = {
            "example": {
                "text": "Should I invest in this stock?",
                "context": "investment_decision",
                "modalities": ["emotion", "risk", "ethics"],
                "ethical_constraints": {
                    "max_risk": 0.3,
                    "fairness_required": True
                }
            }
        }

def fuse_cognitive_data(request: FusionRequest) -> Dict[str, Union[float, str]]:
    """
    Fuse multiple cognitive modalities for unified decision making.

    This function combines emotional intelligence, risk analysis, and ethical
    reasoning to provide comprehensive decision support.

    Args:
        request: Fusion request with input data and constraints

    Returns:
        Dictionary containing fused decision and metadata

    Raises:
        ValueError: If fusion modalities are incompatible
        EthicalViolationError: If decision violates ethical constraints

    Example:
        >>> request = FusionRequest(text="Market is volatile")
        >>> result = fuse_cognitive_data(request)
        >>> print(result["fused_score"])
        0.456
    """
    # Implementation here
    pass
```

---

## 🚀 Performance Optimization

### **Profiling and Benchmarking**

```python
# Performance profiling
import cProfile
import pstats
from functools import wraps

def profile_function(func):
    """Decorator to profile function performance."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()

        result = func(*args, **kwargs)

        profiler.disable()
        stats = pstats.Stats(profiler)
        stats.sort_stats('cumulative')
        stats.print_stats(20)  # Top 20 functions

        return result
    return wrapper

# Memory profiling
from memory_profiler import profile

@profile
def memory_intensive_fusion():
    """Profile memory usage of fusion process."""
    # Implementation
    pass

# Benchmarking
import time
from statistics import mean, stdev

def benchmark_fusion(iterations: int = 100):
    """Benchmark fusion engine performance."""
    times = []

    for _ in range(iterations):
        start_time = time.perf_counter()

        # Run fusion
        result = fusion_engine.fuse(test_data)

        end_time = time.perf_counter()
        times.append(end_time - start_time)

    print(f"Average time: {mean(times):.4f}s")
    print(f"Std deviation: {stdev(times):.4f}s")
    print(f"Min time: {min(times):.4f}s")
    print(f"Max time: {max(times):.4f}s")
```

### **Optimization Techniques**

```python
# Async processing for I/O bound operations
import asyncio
from concurrent.futures import ThreadPoolExecutor

class AsyncFusionEngine:
    """Asynchronous fusion engine for better concurrency."""

    def __init__(self):
        self.executor = ThreadPoolExecutor(max_workers=4)

    async def fuse_async(self, input_data: dict) -> dict:
        """Asynchronous fusion processing."""
        loop = asyncio.get_event_loop()

        # Run CPU-intensive tasks in thread pool
        emotional_task = loop.run_in_executor(
            self.executor, self._analyze_emotion, input_data
        )
        risk_task = loop.run_in_executor(
            self.executor, self._analyze_risk, input_data
        )
        ethics_task = loop.run_in_executor(
            self.executor, self._analyze_ethics, input_data
        )

        # Wait for all analyses to complete
        emotional_result, risk_result, ethics_result = await asyncio.gather(
            emotional_task, risk_task, ethics_task
        )

        # Fuse results
        return self._fuse_results(
            emotional_result, risk_result, ethics_result
        )

# Caching for expensive computations
from functools import lru_cache
import hashlib

class CachedFusionEngine:
    """Fusion engine with intelligent caching."""

    def __init__(self):
        self.cache = {}

    @lru_cache(maxsize=1000)
    def _cached_emotion_analysis(self, text_hash: str, text: str) -> dict:
        """Cache emotion analysis results."""
        if text_hash in self.cache:
            return self.cache[text_hash]

        result = self._analyze_emotion_uncached(text)
        self.cache[text_hash] = result
        return result

    def analyze_emotion(self, text: str) -> dict:
        """Analyze emotion with caching."""
        text_hash = hashlib.md5(text.encode()).hexdigest()
        return self._cached_emotion_analysis(text_hash, text)
```

---

## 🔒 Security Development

### **Secure Coding Practices**

```python
# Input validation
from pydantic import BaseModel, validator
import re

class SecureFusionRequest(BaseModel):
    """Secure fusion request with validation."""

    text: str = Field(..., min_length=1, max_length=10000)

    @validator('text')
    def validate_text(cls, v):
        """Validate input text for security."""
        # Check for malicious patterns
        if re.search(r'<script|javascript:|on\w+\s*=', v, re.IGNORECASE):
            raise ValueError('Potentially malicious content detected')

        # Check for excessive special characters
        special_chars = sum(1 for c in v if not c.isalnum() and not c.isspace())
        if special_chars / len(v) > 0.5:
            raise ValueError('Too many special characters')

        return v

# Rate limiting
from slowapi import Limiter, Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.post("/api/v1/fuse")
@limiter.limit("10/minute")
async def fuse_endpoint(request: SecureFusionRequest):
    """Rate-limited fusion endpoint."""
    return await fusion_engine.fuse(request.dict())

# Authentication and authorization
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Validate JWT token and get current user."""
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=["HS256"])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_id
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/api/v1/profile")
async def get_user_profile(current_user: str = Depends(get_current_user)):
    """Protected endpoint requiring authentication."""
    return await user_service.get_profile(current_user)
```

### **Security Testing**

```bash
# Security scanning
bandit -r .                          # Python security issues
safety check                         # Vulnerable dependencies
trivy image spiralbrain:latest      # Container security scan

# Penetration testing
nikto -h http://localhost:8000       # Web server scanning
sqlmap -u "http://localhost:8000/api/v1/fusion" --data="text=test"  # SQL injection testing
```

---

## 📊 Monitoring & Debugging

### **Development Monitoring**

```python
# Structured logging
import structlog
import logging

# Configure structured logging
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer()
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()

# Usage
def process_fusion_request(request_data):
    logger.info(
        "Processing fusion request",
        user_id=request_data.get("user_id"),
        request_size=len(str(request_data)),
        modalities=request_data.get("modalities", [])
    )

    try:
        result = fusion_engine.fuse(request_data)
        logger.info(
            "Fusion completed successfully",
            fused_score=result.get("fused_score"),
            processing_time=result.get("processing_time")
        )
        return result
    except Exception as e:
        logger.error(
            "Fusion processing failed",
            error=str(e),
            error_type=type(e).__name__,
            request_data=request_data
        )
        raise
```

### **Debug Configuration**

```python
# Debug settings for development
import os

DEBUG = os.getenv("DEBUG", "false").lower() == "true"

if DEBUG:
    # Enable debug logging
    logging.basicConfig(level=logging.DEBUG)

    # Enable SQL query logging
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

    # Enable HTTP request logging
    logging.getLogger('urllib3').setLevel(logging.DEBUG)

    # Memory debugging
    import tracemalloc
    tracemalloc.start()

    # Performance profiling
    import cProfile
    profiler = cProfile.Profile()
    profiler.enable()
```

---

## 🤝 Contributing Guidelines

### **Development Workflow**

```bash
# 1. Create a feature branch
git checkout -b feature/new-cognitive-modality

# 2. Make changes with tests
# Edit code...
# Add tests...

# 3. Run quality checks
pre-commit run --all-files

# 4. Run tests
pytest tests/ -v

# 5. Update documentation if needed
# Edit docs...

# 6. Commit changes
git add .
git commit -m "Add new cognitive modality for market sentiment

- Implements market sentiment analysis
- Integrates with fusion engine
- Adds comprehensive tests
- Updates API documentation"

# 7. Create pull request
git push origin feature/new-cognitive-modality
# Create PR on GitHub
```

### **Pull Request Requirements**

- **Code Quality**: Passes all linting and formatting checks
- **Tests**: Includes unit and integration tests with >90% coverage
- **Documentation**: Updates relevant documentation
- **Security**: Passes security scanning
- **Performance**: No significant performance regressions
- **Compatibility**: Maintains backward compatibility

### **Code Review Checklist**

```markdown
## Code Review Checklist

### Functionality
- [ ] Code implements the intended feature
- [ ] Edge cases are handled appropriately
- [ ] Error handling is robust
- [ ] Security considerations are addressed

### Code Quality
- [ ] Code follows project conventions
- [ ] Functions are well-documented
- [ ] Variables and functions have descriptive names
- [ ] Code is DRY (Don't Repeat Yourself)

### Testing
- [ ] Unit tests cover new functionality
- [ ] Integration tests verify component interactions
- [ ] Performance tests ensure no regressions
- [ ] Edge cases are tested

### Documentation
- [ ] Code is well-commented
- [ ] API documentation is updated
- [ ] README changes if needed
- [ ] Breaking changes are documented

### Security
- [ ] Input validation is implemented
- [ ] Authentication/authorization is proper
- [ ] No sensitive data is logged
- [ ] Dependencies are secure
```

---

## 📚 Advanced Topics

### **Model Training and Deployment**

```python
# Custom model training pipeline
from spiral_cortex_core.training import ModelTrainer

class EmotionModelTrainer(ModelTrainer):
    """Custom trainer for emotion analysis models."""

    def __init__(self):
        super().__init__()
        self.datasets = self._load_training_datasets()

    def train_emotion_model(self, config: dict):
        """Train emotion analysis model."""
        # Prepare data
        train_data, val_data = self._prepare_data(self.datasets)

        # Configure model
        model = self._build_model(config)

        # Train with callbacks
        callbacks = [
            EarlyStopping(patience=5),
            ModelCheckpoint(filepath='best_emotion_model.h5'),
            TensorBoard(log_dir='./logs')
        ]

        history = model.fit(
            train_data,
            validation_data=val_data,
            epochs=config.get('epochs', 100),
            callbacks=callbacks
        )

        # Evaluate and save
        self._evaluate_model(model, val_data)
        self._save_model(model, 'emotion_model_v2')

        return model, history

# Continuous learning
class ContinuousLearner:
    """Continuous model improvement."""

    def __init__(self):
        self.feedback_buffer = []

    def add_feedback(self, prediction, actual, context):
        """Add user feedback for model improvement."""
        self.feedback_buffer.append({
            'prediction': prediction,
            'actual': actual,
            'context': context,
            'timestamp': datetime.now()
        })

    def retrain_if_needed(self):
        """Retrain model if performance degrades."""
        if len(self.feedback_buffer) >= 1000:
            self._retrain_model(self.feedback_buffer)
            self.feedback_buffer = []
```

### **Distributed Processing**

```python
# Distributed fusion processing
import ray

@ray.remote
class DistributedFusionWorker:
    """Distributed worker for fusion processing."""

    def __init__(self):
        self.emotion_analyzer = EmotionAnalyzer()
        self.risk_analyzer = RiskAnalyzer()
        self.ethical_regulator = EthicalRegulator()

    def process_fusion_task(self, task_data):
        """Process a single fusion task."""
        # Parallel processing of modalities
        emotion_future = self._analyze_emotion.remote(task_data)
        risk_future = self._analyze_risk.remote(task_data)
        ethics_future = self._analyze_ethics.remote(task_data)

        # Wait for results
        emotion_result = ray.get(emotion_future)
        risk_result = ray.get(risk_future)
        ethics_result = ray.get(ethics_future)

        # Fuse results
        return self._fuse_modalities(
            emotion_result, risk_result, ethics_result
        )

# Initialize Ray cluster
ray.init(address='auto')  # Connect to existing cluster

# Create worker pool
workers = [DistributedFusionWorker.remote() for _ in range(10)]

# Process tasks in parallel
futures = [worker.process_fusion_task.remote(task) for worker, task in zip(workers, tasks)]
results = ray.get(futures)
```

---

## 🎯 Best Practices

### **Performance Best Practices**

1. **Async/Await**: Use async programming for I/O operations
2. **Caching**: Implement intelligent caching strategies
3. **Batch Processing**: Process multiple requests together when possible
4. **Resource Pooling**: Use connection pools for databases and external services
5. **Lazy Loading**: Load heavy resources only when needed

### **Security Best Practices**

1. **Input Validation**: Always validate and sanitize inputs
2. **Least Privilege**: Grant minimum required permissions
3. **Secure Defaults**: Configure secure defaults, not convenience
4. **Regular Updates**: Keep dependencies and systems updated
5. **Monitoring**: Monitor for security incidents and anomalies

### **Code Quality Best Practices**

1. **DRY Principle**: Don't Repeat Yourself
2. **SOLID Principles**: Single responsibility, Open-closed, Liskov substitution, Interface segregation, Dependency inversion
3. **Descriptive Naming**: Use clear, descriptive names
4. **Documentation**: Document complex logic and APIs
5. **Testing**: Write tests first, maintain high coverage

### **DevOps Best Practices**

1. **Infrastructure as Code**: Define infrastructure in code
2. **CI/CD**: Automate testing and deployment
3. **Monitoring**: Implement comprehensive monitoring
4. **Backup**: Regular backups with testing
5. **Disaster Recovery**: Plan for and test disaster scenarios

---

This development guide provides the foundation for effectively working with and extending SpiralBrain. The system's modular architecture and comprehensive testing framework make it ideal for collaborative development and continuous improvement.