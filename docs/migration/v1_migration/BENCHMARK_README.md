# 🧠 SpiralCortex Developer Benchmark Suite

A comprehensive benchmarking and data processing suite for evaluating SpiralCortex's six-phase cognitive evolution: from attention-based gating through temporal self-consistency.

## 🚀 Quick Start

### Run Full Benchmark Suite
```bash
# Run comprehensive benchmarks (recommended for developers)
python benchmark_suite.py
```

### Analyze Results
```bash
# Generate detailed analysis and visualizations
python benchmark_analyzer.py
```

### Test Cognitive Phases
```bash
# Phase 4: Reflective Self-Regulation Demo
python demo_reflective_self.py

# Phase 5: Causal Introspection Demo
python causal_introspection/causal_introspection.py

# Phase 6: Temporal Self-Consistency Demo
python temporal_self_consistency/temporal_self_consistency.py

# Phase 6: Full Integration Demo (Phase 5 + 6)
python temporal_self_consistency/integration_demo.py
```

## 📊 What Gets Tested

### Cognitive Phases
- **Phase 1: Attention-Based Gating**: Dynamic multimodal weighting with softmax attention
- **Phase 2: Adaptive Learning**: Reinforcement learning for coherence optimization
- **Phase 3: Real-Time Adaptation**: Continuous weight adjustment during inference
- **Phase 4: Reflective Self-Regulation**: Metacognitive prediction and pre-emptive corrections
- **Phase 5: Causal Introspection**: Counterfactual analysis and self-explanation
- **Phase 6: Temporal Self-Consistency**: Cognitive identity persistence across time

### AI Components
- **AttentionGatingIntegrator**: Phase 1 multimodal fusion with context-sensitive weighting
- **RealTimeAdapter**: Phase 3 continuous adaptation with memory-based bootstrapping
- **ReflectiveController**: Phase 4 metacognitive self-regulation with predictive monitoring
- **CausalIntrospector**: Phase 5 counterfactual perturbation analysis
- **TemporalSelfConsistency**: Phase 6 identity persistence and contradiction detection

### Test Scenarios
- **High Stress**: Extreme emotional states with various market conditions
- **Balanced**: Moderate emotional states with balanced market conditions
- **Low Stress**: Calm emotional states across different scenarios
- **Extreme Stress**: Edge case testing with maximum emotional intensity

### Market Conditions
- **Bull Market**: Favorable investment conditions
- **Bear Market**: Challenging investment conditions
- **Volatile**: High uncertainty market conditions
- **Stable**: Low volatility market conditions

## 📈 Performance Metrics

### Processing Performance
- **Average Processing Time**: Typical response time across all tests
- **Median Processing Time**: Central tendency of processing times
- **Min/Max Processing Times**: Best and worst case performance
- **Processing Time Standard Deviation**: Consistency of performance

### AI Quality Metrics
- **Fused Confidence**: Overall decision confidence from multi-modal fusion
- **Emotional Valence**: Emotional state assessment accuracy
- **Risk Score**: Risk assessment precision
- **Opportunity Score**: Opportunity detection effectiveness
- **Stress Level**: Emotional stress detection accuracy

## 📁 Output Files

### Benchmark Results
- `benchmark_results/benchmark_results_*.json`: Raw benchmark data
- `benchmark_results/benchmark_summary_*.json`: Session summary
- `benchmark_results/benchmark_report.json`: Detailed analysis report

### Visualizations
- `benchmark_charts/benchmark_overview.png`: Comprehensive performance overview
- `benchmark_charts/scenario_performance.png`: Scenario-by-scenario comparison

## 🔧 Configuration Options

### Benchmark Suites

#### Comprehensive Suite (Default)
- Tests all components across all scenarios
- Multiple fusion weight configurations
- 50 iterations per test configuration
- Concurrent execution for speed

#### Performance Suite
- High-throughput testing (200 iterations)
- Focus on processing speed
- Limited configurations for speed

#### Stress Test Suite
- Edge case testing with extreme configurations
- Sequential execution for stability
- Focus on reliability under stress

### Custom Configuration
```python
from benchmark_suite import BenchmarkSuite

custom_suite = BenchmarkSuite(
    name="My Custom Benchmark",
    description="Testing specific scenarios",
    components=["fusion_engine"],  # Only test fusion
    scenarios=["high_stress_bull_market", "low_stress_stable"],
    configurations=[
        {"context": "high_stress_investment", "emotional_weight": 0.8, "analytical_weight": 0.2}
    ],
    iterations=100,
    concurrent=True
)
```

## 📊 Understanding Results

### Success Rates
- **>95%**: Excellent reliability
- **90-95%**: Good reliability with minor issues
- **<90%**: Investigate failed tests

### Processing Times
- **<0.01s**: Excellent performance (sub-10ms)
- **<0.1s**: Good performance (sub-100ms)
- **>0.1s**: Optimization opportunities available

### Key Metrics Interpretation

#### Fusion Confidence
- **High (>0.7)**: Strong multi-modal alignment
- **Medium (0.4-0.7)**: Balanced decision making
- **Low (<0.4)**: Potential decision conflicts

#### Emotional Valence
- **Positive**: Optimistic emotional state
- **Neutral (near 0)**: Balanced emotional state
- **Negative**: Pessimistic emotional state

#### Risk vs Opportunity Scores
- **Risk > Opportunity**: Conservative recommendations
- **Opportunity > Risk**: Aggressive recommendations
- **Balanced**: Moderate risk-adjusted decisions

## 🛠️ Advanced Usage

### Data Generation
```python
from benchmark_suite import DataGenerator

# Generate custom test data
emotional_data = DataGenerator.generate_emotional_data("high_stress", samples=1000)
analytical_data = DataGenerator.generate_analytical_data("volatile", samples=1000)
```

### Individual Component Testing
```python
from benchmark_suite import BenchmarkRunner

runner = BenchmarkRunner()

# Test single component
results = runner.benchmark_component(
    component="fusion_engine",
    scenario_data={"emotional": emotional_data, "analytical": analytical_data, "name": "custom_test"},
    configuration={"context": "balanced_investment"},
    iterations=50
)
```

### Custom Analysis
```python
from benchmark_analyzer import BenchmarkAnalyzer

analyzer = BenchmarkAnalyzer()

# Load and analyze results
analyzer.load_latest_results()
report = analyzer.generate_performance_report()
analyzer.create_visualizations(report)
```

## 🔍 Troubleshooting

### Common Issues

#### No Results Found
- Ensure `benchmark_suite.py` has been run first
- Check `benchmark_results/` directory exists
- Verify file permissions

#### Import Errors
- Ensure all dependencies are installed: `pip install torch numpy pandas matplotlib`
- Check Python path includes project directory

#### Memory Issues
- Reduce `iterations` in benchmark suites
- Run components individually instead of concurrently
- Use smaller batch sizes in custom configurations

#### Visualization Errors
- Ensure matplotlib backend supports PNG output
- Check write permissions for `benchmark_charts/` directory

## 📋 Dependencies

```txt
torch>=1.9.0
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.4.0
```

## 🎯 Best Practices

### For Development Testing
1. Start with comprehensive suite for full evaluation
2. Use performance suite for quick regression testing
3. Run stress tests before major releases

### For Performance Optimization
1. Focus on components with highest processing times
2. Compare different fusion weight configurations
3. Test edge cases with stress test suite

### For Quality Assurance
1. Monitor success rates across releases
2. Track key metrics for performance regression
3. Validate results across different scenarios

## 🤝 Contributing

When adding new benchmark scenarios or components:

1. Update `DataGenerator` for new data types
2. Add component methods to `BenchmarkRunner`
3. Update visualization logic for new metrics
4. Document new configuration options
5. Add corresponding analysis in `BenchmarkAnalyzer`

## 📄 License

This benchmark suite is part of the SpiralCortex project. See main project license for details.