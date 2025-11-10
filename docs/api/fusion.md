# 🔌 SpiralBrain API Reference

## Overview

SpiralBrain provides a unified REST API that combines emotional intelligence, analytical reasoning, and ethical governance. All endpoints return JSON responses with comprehensive metadata.

## Base URL
```
https://your-domain.com/api/v1/cortex/
```

## Authentication
Currently open access. Enterprise deployments should implement API key authentication.

---

## 🔄 Fusion API

The core cognitive fusion endpoint that combines all intelligence modalities.

### POST `/fuse`

Unifies emotional, analytical, and ethical processing into a single cognitive decision.

#### Request Body
```json
{
  "data": {
    "text": "Market analysis text or context",
    "dataset_type": "day_trader|hodler|miner|defi_user|large_portfolio",
    "context": "Optional additional context",
    "metadata": {
      "user_id": "optional_user_identifier",
      "session_id": "optional_session_tracking",
      "risk_tolerance": "low|medium|high"
    }
  }
}
```

#### Parameters
- `text` (string): Primary input text for analysis
- `dataset_type` (string): Context type for adaptive weighting optimization
- `context` (string, optional): Additional situational context
- `metadata` (object, optional): Additional processing metadata

#### Response
```json
{
  "fused_score": 0.734,
  "confidence": 0.892,
  "cognitive_metrics": {
    "emotional_valence": 0.732,
    "metacognitive_stability": 0.845,
    "coherence_score": 0.678
  },
  "analytical_metrics": {
    "risk_score": 0.423,
    "confidence": 0.876,
    "ensemble_consensus": 0.789
  },
  "recommendation": "Moderately favorable - proceed with caution",
  "explanation": "Analysis shows balanced market conditions with moderate risk...",
  "ethical_assessment": {
    "moral_valence": 0.123,
    "ethical_dimensions": {
      "harm_minimization": 0.856,
      "fairness": 0.734,
      "transparency": 0.923,
      "autonomy": 0.645,
      "volatility_control": 0.789,
      "long_term_welfare": 0.567
    },
    "justification": "Decision maintains ethical balance with moderate risk consideration",
    "confidence": 0.834,
    "modulation_details": {
      "original_score": 0.733,
      "ethical_adjustment": 0.001,
      "gamma": 0.015,
      "dimension_adjustments": {}
    }
  },
  "governance_evaluation": {
    "status": "compliant",
    "violations_count": 0,
    "actions_applied": [],
    "recommendations": [
      "All governance policies satisfied."
    ]
  },
  "processing_metadata": {
    "total_latency_ms": 1.2,
    "components_used": ["emotion", "risk", "ethics"],
    "adaptive_weights": {
      "emotion": 0.45,
      "risk": 0.55
    }
  }
}
```

#### Response Fields
- `fused_score` (float): Final cognitive decision score [0.0, 1.0]
- `confidence` (float): Overall confidence in the fusion result [0.0, 1.0]
- `cognitive_metrics` (object): Raw emotional intelligence outputs
- `analytical_metrics` (object): Raw risk analysis outputs
- `recommendation` (string): Human-readable action guidance
- `ethical_assessment` (object): Complete ethical evaluation with justification
- `governance_evaluation` (object): Policy compliance and actions taken

---

## 🧠 Emotional Analysis API

Direct access to SpiralBrain-Nexus emotional intelligence capabilities.

### POST `/emotion/analyze`

Performs deep emotional analysis using SEC (Symbolic-Emotional Calibration).

#### Request Body
```json
{
  "data": "Text to analyze for emotional content",
  "include_sec": true,
  "include_biofeedback": false
}
```

#### Response
```json
{
  "emotional_valence": 0.723,
  "sec_dimensions": {
    "arousal": 0.645,
    "valence": 0.723,
    "dominance": 0.567,
    "anger": 0.123,
    "fear": 0.234,
    "joy": 0.456,
    "sadness": 0.089,
    "surprise": 0.312
  },
  "metacognitive_metrics": {
    "stability": 0.834,
    "coherence": 0.756,
    "attention_entropy": 0.423
  },
  "pathway_activations": {
    "creative": 0.645,
    "reasoning": 0.723,
    "attention": 0.567,
    "vision": 0.234
  },
  "justification": "Analysis shows positive emotional valence with moderate arousal...",
  "confidence": 0.892
}
```

---

## 🧮 Risk Analysis API

Direct access to SpiralCode-X analytical and risk assessment capabilities.

### POST `/risk/analyze`

Performs comprehensive risk analysis with ensemble intelligence.

#### Request Body
```json
{
  "data": {
    "transaction_data": {...},
    "market_conditions": {...},
    "user_profile": {...}
  },
  "analysis_type": "comprehensive",
  "include_ensemble": true
}
```

#### Response
```json
{
  "risk_score": 0.423,
  "confidence": 0.876,
  "ensemble_breakdown": {
    "day_trader_model": 0.456,
    "hodler_model": 0.389,
    "market_model": 0.412,
    "consensus_score": 0.423
  },
  "risk_dimensions": {
    "market_volatility": 0.678,
    "liquidity_risk": 0.345,
    "counterparty_risk": 0.234,
    "regulatory_risk": 0.123
  },
  "recommendations": [
    "Consider position sizing limits",
    "Monitor volatility thresholds"
  ],
  "active_learning_feedback": {
    "model_updated": true,
    "improvement_margin": 0.023
  }
}
```

---

## ⚖️ Ethical Governance API

Access to the ethical regulator and governance policy system.

### POST `/ethics/assess`

Evaluates ethical context and governance compliance.

#### Request Body
```json
{
  "data": {
    "decision_context": "Description of decision scenario",
    "stakeholders": ["user", "market", "regulators"],
    "potential_impacts": ["financial", "emotional", "societal"]
  },
  "policies_to_check": ["all"]
}
```

#### Response
```json
{
  "moral_valence": 0.123,
  "ethical_dimensions": {
    "harm_minimization": 0.856,
    "fairness": 0.734,
    "transparency": 0.923,
    "autonomy": 0.645,
    "volatility_control": 0.789,
    "long_term_welfare": 0.567
  },
  "governance_status": "compliant",
  "policy_violations": [],
  "justification": "Decision maintains ethical balance with appropriate safeguards...",
  "recommended_actions": [
    "Ensure transparent communication",
    "Monitor for unintended consequences"
  ],
  "audit_trail": {
    "assessment_timestamp": "2025-10-12T20:30:00Z",
    "policies_evaluated": 7,
    "confidence_score": 0.834
  }
}
```

---

## 📊 Monitoring & Metrics API

Access to system performance and health metrics.

### GET `/health`

Basic health check endpoint.

#### Response
```json
{
  "status": "healthy",
  "timestamp": "2025-10-12T20:30:00Z",
  "version": "v24.0",
  "components": {
    "fusion_engine": "operational",
    "emotional_ai": "operational",
    "analytical_ai": "operational",
    "ethical_regulator": "operational"
  }
}
```

### GET `/metrics`

Prometheus-compatible metrics endpoint.

#### Response
```
# HELP spiralcortex_fusion_request_duration_seconds Time spent processing fusion requests
# TYPE spiralcortex_fusion_request_duration_seconds histogram
spiralcortex_fusion_request_duration_seconds_bucket{le="0.1"} 12543
spiralcortex_fusion_request_duration_seconds_bucket{le="0.5"} 12843
...

# HELP spiralcortex_fused_score_distribution Distribution of fusion scores
# TYPE spiralcortex_fused_score_distribution histogram
spiralcortex_fused_score_distribution_bucket{le="0.2"} 1234
...
```

### GET `/status`

Detailed system status and performance metrics.

#### Response
```json
{
  "system_status": "operational",
  "uptime_seconds": 345600,
  "performance_metrics": {
    "average_latency_ms": 1.2,
    "requests_per_second": 45.6,
    "error_rate": 0.001,
    "accuracy_score": 0.827
  },
  "component_status": {
    "spiralbrain_nexus": {
      "status": "healthy",
      "last_update": "2025-10-12T20:29:45Z",
      "performance_score": 0.945
    },
    "spiralcode_x": {
      "status": "healthy",
      "last_update": "2025-10-12T20:29:50Z",
      "performance_score": 0.912
    },
    "ethical_regulator": {
      "status": "healthy",
      "last_update": "2025-10-12T20:29:47Z",
      "performance_score": 0.978
    }
  },
  "active_alerts": []
}
```

---

## 📋 Batch Processing API

For high-throughput processing of multiple items.

### POST `/batch/fuse`

Process multiple fusion requests in a single call.

#### Request Body
```json
{
  "requests": [
    {
      "id": "request_1",
      "data": {"text": "First analysis...", "dataset_type": "day_trader"}
    },
    {
      "id": "request_2",
      "data": {"text": "Second analysis...", "dataset_type": "hodler"}
    }
  ],
  "options": {
    "parallel_processing": true,
    "include_detailed_metrics": false
  }
}
```

#### Response
```json
{
  "batch_id": "batch_12345",
  "total_requests": 2,
  "processed_requests": 2,
  "results": [
    {
      "id": "request_1",
      "fused_score": 0.734,
      "confidence": 0.892,
      "status": "success"
    },
    {
      "id": "request_2",
      "fused_score": 0.623,
      "confidence": 0.845,
      "status": "success"
    }
  ],
  "batch_metrics": {
    "total_latency_ms": 2.1,
    "average_latency_ms": 1.05,
    "success_rate": 1.0
  }
}
```

---

## 🔧 Configuration API

Runtime configuration management (admin access required).

### GET `/config`

Retrieve current system configuration.

### POST `/config/update`

Update system configuration parameters.

### POST `/policies/update`

Update ethical governance policies.

---

## 📊 Error Handling

All endpoints follow consistent error response format:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid dataset_type provided",
    "details": {
      "field": "dataset_type",
      "provided_value": "invalid_type",
      "allowed_values": ["day_trader", "hodler", "miner", "defi_user", "large_portfolio"]
    }
  },
  "request_id": "req_12345",
  "timestamp": "2025-10-12T20:30:00Z"
}
```

### Common Error Codes
- `VALIDATION_ERROR`: Invalid request parameters
- `PROCESSING_ERROR`: Internal processing failure
- `RATE_LIMITED`: Too many requests
- `SERVICE_UNAVAILABLE`: Component temporarily unavailable

---

## 🔒 Rate Limiting

- **Standard Tier**: 100 requests/minute
- **Premium Tier**: 1000 requests/minute
- **Enterprise Tier**: Unlimited

Rate limit headers included in all responses:
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 87
X-RateLimit-Reset: 1634067600
```

---

## 📈 Webhook Integration

Configure webhooks for real-time notifications.

### POST `/webhooks/register`

Register a webhook endpoint for specific events.

### Supported Events
- `fusion_completed`: When fusion analysis finishes
- `ethical_violation`: When governance policies are violated
- `performance_degraded`: When system performance drops
- `model_updated`: When models are automatically retrained

This comprehensive API provides access to SpiralBrain's unified cognitive intelligence capabilities, combining emotional understanding, analytical rigor, and ethical responsibility into production-ready endpoints.