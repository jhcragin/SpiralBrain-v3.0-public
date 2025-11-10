# Debugging Guide

This guide provides systematic approaches for debugging issues in SpiralCortex, covering common problems, debugging techniques, and troubleshooting workflows.

## Table of Contents

- [Common Issues](#common-issues)
- [Debugging Techniques](#debugging-techniques)
- [Performance Debugging](#performance-debugging)
- [Multi-Modal Issues](#multi-modal-issues)
- [Neural Network Debugging](#neural-network-debugging)
- [System Integration Issues](#system-integration-issues)
- [Logging and Monitoring](#logging-and-monitoring)

## Common Issues

### Memory Issues

**Symptoms:**

- Out of memory errors during training/inference
- Gradual memory leaks over time
- CUDA out of memory errors

**Debugging Steps:**

1. Check tensor sizes and batch sizes
2. Use `torch.cuda.memory_summary()` for GPU memory analysis
3. Monitor memory usage with `psutil` or `memory_profiler`
4. Look for unreleased tensors or model references

**Solutions:**

- Reduce batch size
- Use gradient accumulation
- Implement proper tensor cleanup
- Use `torch.no_grad()` for inference

### Training Instability

**Symptoms:**

- NaN or Inf values in losses/gradients
- Oscillating or diverging loss
- Poor convergence

**Debugging Steps:**

1. Check input data normalization
2. Verify gradient clipping implementation
3. Monitor learning rate schedules
4. Check for exploding/vanishing gradients

**Solutions:**

- Implement gradient clipping
- Use learning rate schedulers
- Add regularization techniques
- Check data preprocessing pipelines

### Real-Time Performance Issues

**Symptoms:**

- Latency spikes above 100ms
- Inconsistent frame rates
- High CPU/GPU utilization

**Debugging Steps:**

1. Profile with `torch.profiler` or `cProfile`
2. Check for blocking operations
3. Monitor queue depths and buffer usage
4. Analyze thread utilization

**Solutions:**

- Optimize model architecture
- Implement asynchronous processing
- Use model quantization
- Optimize data pipelines

## Debugging Techniques

### Logging Best Practices

```python
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

# Use appropriate log levels
logger.debug("Detailed debugging information")
logger.info("General information about program execution")
logger.warning("Warning about potential issues")
logger.error("Error that doesn't stop execution")
logger.critical("Critical error that may stop execution")
```

### Interactive Debugging

```python
# Use pdb for interactive debugging
import pdb

def problematic_function(data):
    pdb.set_trace()  # Set breakpoint
    result = process_data(data)
    return result

# Or use IPython for enhanced debugging
from IPython import embed

def debug_function(data):
    embed()  # Drop into IPython shell
    return process_data(data)
```

### Unit Testing for Debugging

```python
import unittest
import torch
from unittest.mock import Mock, patch

class TestModelDebugging(unittest.TestCase):
    def test_gradient_flow(self):
        """Test that gradients flow properly through the model"""
        model = create_model()
        input_tensor = torch.randn(1, 10)

        # Forward pass
        output = model(input_tensor)
        loss = output.sum()

        # Backward pass
        loss.backward()

        # Check gradients
        for name, param in model.named_parameters():
            self.assertIsNotNone(param.grad, f"No gradient for {name}")
            self.assertFalse(torch.isnan(param.grad).any(), f"NaN gradient in {name}")

    def test_output_shapes(self):
        """Test that model outputs have expected shapes"""
        model = create_model()
        test_inputs = [
            torch.randn(1, 10),
            torch.randn(4, 10),
            torch.randn(8, 10)
        ]

        for input_tensor in test_inputs:
            with self.subTest(batch_size=input_tensor.shape[0]):
                output = model(input_tensor)
                expected_shape = (input_tensor.shape[0], model.output_dim)
                self.assertEqual(output.shape, expected_shape)
```

## Performance Debugging

### Profiling Neural Networks

```python
import torch
from torch.profiler import profile, record_function, ProfilerActivity

def profile_model(model, input_tensor):
    with profile(activities=[ProfilerActivity.CPU, ProfilerActivity.CUDA],
                 record_shapes=True) as prof:
        with record_function("model_inference"):
            model(input_tensor)

    print(prof.key_averages().table(sort_by="cuda_time_total", row_limit=10))

# Memory profiling
from torch.cuda import memory_summary
print(memory_summary())
```

### Performance Monitoring

```python
import time
import psutil
import GPUtil

class PerformanceMonitor:
    def __init__(self):
        self.start_time = time.time()
        self.cpu_percent = psutil.cpu_percent()
        self.memory_percent = psutil.virtual_memory().percent

        if torch.cuda.is_available():
            self.gpu_utilization = GPUtil.getGPUs()[0].load * 100
            self.gpu_memory = GPUtil.getGPUs()[0].memoryUtil * 100

    def report(self):
        elapsed = time.time() - self.start_time
        print(f"Elapsed time: {elapsed:.2f}s")
        print(f"CPU usage: {psutil.cpu_percent()}%")
        print(f"Memory usage: {psutil.virtual_memory().percent}%")

        if torch.cuda.is_available():
            gpu = GPUtil.getGPUs()[0]
            print(f"GPU usage: {gpu.load * 100:.1f}%")
            print(f"GPU memory: {gpu.memoryUtil * 100:.1f}%")
```

## Multi-Modal Issues

### Modality Synchronization

**Common Issues:**

- Time synchronization between different sensors
- Missing data in one modality
- Different sampling rates

**Debugging:**

```python
def check_modality_sync(physiological_data, emotional_data, timestamp_offset=0.1):
    """Check synchronization between modalities"""
    phys_times = physiological_data['timestamps']
    emot_times = emotional_data['timestamps']

    # Check for time alignment
    time_diffs = []
    for phys_time in phys_times:
        closest_emot = min(emot_times, key=lambda x: abs(x - phys_time))
        time_diffs.append(abs(phys_time - closest_emot))

    max_diff = max(time_diffs)
    avg_diff = sum(time_diffs) / len(time_diffs)

    print(f"Max time difference: {max_diff:.3f}s")
    print(f"Average time difference: {avg_diff:.3f}s")

    if max_diff > timestamp_offset:
        print("WARNING: Modalities may be out of sync!")
        return False
    return True
```

### Fusion Layer Debugging

```python
def debug_fusion_layer(fusion_model, modalities):
    """Debug multi-modal fusion layer"""
    # Test individual modalities
    individual_outputs = {}
    for modality_name, modality_data in modalities.items():
        with torch.no_grad():
            output = fusion_model.extract_features(modality_data, modality_name)
            individual_outputs[modality_name] = output

            # Check for NaN/inf values
            if torch.isnan(output).any() or torch.isinf(output).any():
                print(f"WARNING: Invalid values in {modality_name} features")

    # Test fusion
    try:
        fused_output = fusion_model.fuse_modalities(individual_outputs)
        print(f"Fusion successful. Output shape: {fused_output.shape}")

        # Check fusion weights
        if hasattr(fusion_model, 'attention_weights'):
            weights = fusion_model.attention_weights
            print(f"Attention weights: {weights}")
            print(f"Weight distribution: mean={weights.mean():.3f}, std={weights.std():.3f}")

    except Exception as e:
        print(f"Fusion failed: {e}")
        return False

    return True
```

## Neural Network Debugging

### Gradient Analysis

```python
def analyze_gradients(model):
    """Analyze gradient flow in neural network"""
    grad_norms = {}
    grad_means = {}
    grad_stds = {}

    for name, param in model.named_parameters():
        if param.grad is not None:
            grad_norms[name] = param.grad.norm().item()
            grad_means[name] = param.grad.mean().item()
            grad_stds[name] = param.grad.std().item()

    # Check for vanishing/exploding gradients
    for name, norm in grad_norms.items():
        if norm < 1e-7:
            print(f"WARNING: Vanishing gradient in {name}: {norm}")
        elif norm > 1e3:
            print(f"WARNING: Exploding gradient in {name}: {norm}")

    return grad_norms, grad_means, grad_stds
```

### Activation Analysis

```python
def analyze_activations(model, input_tensor, layer_names=None):
    """Analyze activations in neural network layers"""
    activations = {}

    def hook_fn(name):
        def hook(module, input, output):
            activations[name] = output.detach().cpu()
        return hook

    hooks = []
    if layer_names is None:
        layer_names = [name for name, _ in model.named_modules() if len(name) > 0]

    for name in layer_names:
        try:
            module = dict(model.named_modules())[name]
            hook = module.register_forward_hook(hook_fn(name))
            hooks.append(hook)
        except KeyError:
            print(f"Warning: Layer {name} not found")

    # Forward pass
    with torch.no_grad():
        _ = model(input_tensor)

    # Remove hooks
    for hook in hooks:
        hook.remove()

    # Analyze activations
    for name, activation in activations.items():
        print(f"Layer {name}:")
        print(f"  Shape: {activation.shape}")
        print(f"  Mean: {activation.mean():.4f}")
        print(f"  Std: {activation.std():.4f}")
        print(f"  Min: {activation.min():.4f}")
        print(f"  Max: {activation.max():.4f}")

        # Check for dead neurons
        if (activation == 0).all():
            print(f"  WARNING: All activations are zero!")

    return activations
```

## System Integration Issues

### Hardware Interface Debugging

```python
def debug_hardware_interface(interface):
    """Debug hardware interface connections"""
    try:
        # Test connection
        connected = interface.connect()
        if not connected:
            print("ERROR: Failed to connect to hardware")
            return False

        # Test data acquisition
        test_data = interface.read_data(timeout=5.0)
        if test_data is None:
            print("ERROR: No data received from hardware")
            return False

        # Validate data format
        expected_keys = ['physiological', 'timestamps', 'quality_metrics']
        for key in expected_keys:
            if key not in test_data:
                print(f"ERROR: Missing expected data key: {key}")
                return False

        # Check data quality
        if 'quality_metrics' in test_data:
            quality = test_data['quality_metrics']
            if quality < 0.5:
                print(f"WARNING: Low data quality: {quality}")

        print("Hardware interface test passed")
        return True

    except Exception as e:
        print(f"Hardware interface error: {e}")
        return False
```

### API Integration Testing

```python
def test_api_integration(api_client, test_endpoints):
    """Test API integration points"""
    results = {}

    for endpoint, test_data in test_endpoints.items():
        try:
            response = api_client.post(endpoint, json=test_data)

            if response.status_code == 200:
                data = response.json()
                # Validate response structure
                if validate_response_structure(data, endpoint):
                    results[endpoint] = "PASS"
                    print(f"✓ {endpoint}: Success")
                else:
                    results[endpoint] = "INVALID_RESPONSE"
                    print(f"✗ {endpoint}: Invalid response structure")
            else:
                results[endpoint] = f"HTTP_{response.status_code}"
                print(f"✗ {endpoint}: HTTP {response.status_code}")

        except Exception as e:
            results[endpoint] = f"ERROR: {str(e)}"
            print(f"✗ {endpoint}: {str(e)}")

    return results
```

## Logging and Monitoring

### Structured Logging

```python
import json
import logging
from datetime import datetime

class StructuredLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Add console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def log_event(self, event_type, **kwargs):
        """Log structured event"""
        event_data = {
            'timestamp': datetime.utcnow().isoformat(),
            'event_type': event_type,
            'data': kwargs
        }

        self.logger.info(json.dumps(event_data))

# Usage
logger = StructuredLogger('spiralcortex')

# Log different types of events
logger.log_event('model_inference', model_version='1.0', latency_ms=45.2)
logger.log_event('data_quality_check', sensor='heart_rate', quality_score=0.95)
logger.log_event('user_interaction', action='start_session', user_id='user123')
```

### Health Monitoring

```python
class SystemHealthMonitor:
    def __init__(self):
        self.metrics = {}
        self.alerts = []

    def record_metric(self, name, value, timestamp=None):
        """Record a system metric"""
        if timestamp is None:
            timestamp = time.time()

        if name not in self.metrics:
            self.metrics[name] = []

        self.metrics[name].append((timestamp, value))

        # Keep only recent metrics (last hour)
        cutoff = timestamp - 3600
        self.metrics[name] = [
            (t, v) for t, v in self.metrics[name] if t > cutoff
        ]

    def check_thresholds(self, thresholds):
        """Check metrics against thresholds"""
        for metric_name, threshold in thresholds.items():
            if metric_name in self.metrics:
                recent_values = [v for _, v in self.metrics[metric_name][-10:]]  # Last 10 values

                if recent_values:
                    avg_value = sum(recent_values) / len(recent_values)

                    if avg_value > threshold:
                        alert = f"ALERT: {metric_name} above threshold: {avg_value:.2f} > {threshold}"
                        self.alerts.append((time.time(), alert))
                        print(alert)

    def get_health_report(self):
        """Generate health report"""
        report = {
            'timestamp': datetime.utcnow().isoformat(),
            'metrics': {},
            'alerts': self.alerts[-10:]  # Last 10 alerts
        }

        for name, values in self.metrics.items():
            if values:
                recent_values = values[-10:]
                report['metrics'][name] = {
                    'current': recent_values[-1][1],
                    'average': sum(v for _, v in recent_values) / len(recent_values),
                    'min': min(v for _, v in recent_values),
                    'max': max(v for _, v in recent_values)
                }

        return report
```

## Quick Reference

### Essential Debug Commands

```bash
# Python debugging
python -m pdb script.py  # Run with debugger
python -c "import torch; print(torch.__version__)"  # Check PyTorch version

# GPU debugging
nvidia-smi  # GPU status
watch -n 1 nvidia-smi  # Monitor GPU usage

# Memory debugging
python -m memory_profiler script.py  # Profile memory usage
python -c "import torch; torch.cuda.memory_summary()"  # GPU memory info

# Network debugging
netstat -tlnp  # Check listening ports
curl -X GET http://localhost:8000/health  # Test API endpoint
```

### Common Error Patterns

| Error Pattern | Likely Cause | Solution |
|---------------|--------------|----------|
| `CUDA out of memory` | Batch size too large | Reduce batch size, use gradient accumulation |
| `NaN in loss` | Unstable training | Add gradient clipping, check learning rate |
| `Shape mismatch` | Incorrect tensor dimensions | Verify model input/output shapes |
| `Connection refused` | Service not running | Check service status, restart if needed |
| `Import error` | Missing dependency | Install missing package, check virtual environment |

This guide should be updated as new debugging patterns and techniques are discovered during development.
