# Performance Profiling Guide

This guide provides comprehensive techniques for profiling and optimizing performance in SpiralCortex, covering CPU, GPU, memory, and real-time performance analysis.

## Table of Contents

- [Profiling Tools](#profiling-tools)
- [CPU Profiling](#cpu-profiling)
- [GPU Profiling](#gpu-profiling)
- [Memory Profiling](#memory-profiling)
- [Real-Time Performance](#real-time-performance)
- [Network Profiling](#network-profiling)
- [Database Profiling](#database-profiling)
- [Optimization Strategies](#optimization-strategies)

## Profiling Tools

### Built-in Python Profilers

```python
import cProfile
import pstats
import io

def profile_function(func, *args, **kwargs):
    """Profile a function using cProfile"""
    pr = cProfile.Profile()
    pr.enable()

    result = func(*args, **kwargs)

    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())

    return result

# Usage
@profile_function
def my_function():
    # Code to profile
    pass
```

### PyTorch Profilers

```python
import torch
from torch.profiler import profile, record_function, ProfilerActivity

def profile_pytorch_model(model, input_tensor):
    """Profile PyTorch model execution"""
    with profile(activities=[ProfilerActivity.CPU, ProfilerActivity.CUDA],
                 record_shapes=True,
                 profile_memory=True,
                 with_stack=True) as prof:
        with record_function("model_inference"):
            model(input_tensor)

    # Print results
    print(prof.key_averages().table(sort_by="cuda_time_total", row_limit=10))

    # Export for further analysis
    prof.export_chrome_trace("trace.json")
```

### Memory Profilers

```python
from memory_profiler import profile, memory_usage
import tracemalloc

@profile
def memory_intensive_function():
    """Function decorated with memory profiler"""
    # Code to profile
    pass

def profile_memory_usage(func, *args, **kwargs):
    """Profile memory usage of a function"""
    mem_usage = memory_usage((func, args, kwargs), interval=0.1)
    print(f"Memory usage: {max(mem_usage) - min(mem_usage):.2f} MB")
    return func(*args, **kwargs)

# Using tracemalloc for detailed memory tracing
tracemalloc.start()
snapshot1 = tracemalloc.take_snapshot()

# Code to profile

snapshot2 = tracemalloc.take_snapshot()
top_stats = snapshot2.compare_to(snapshot1, 'lineno')
for stat in top_stats[:10]:
    print(stat)
```

## CPU Profiling

### Detailed CPU Analysis

```python
import time
import psutil
import threading
from collections import defaultdict

class CPUProfiler:
    def __init__(self):
        self.cpu_usage = []
        self.function_times = defaultdict(list)
        self._monitoring = False

    def start_monitoring(self, interval=0.1):
        """Start CPU monitoring in background thread"""
        self._monitoring = True
        self.monitor_thread = threading.Thread(target=self._monitor_cpu, args=(interval,))
        self.monitor_thread.daemon = True
        self.monitor_thread.start()

    def stop_monitoring(self):
        """Stop CPU monitoring"""
        self._monitoring = False
        if hasattr(self, 'monitor_thread'):
            self.monitor_thread.join()

    def _monitor_cpu(self, interval):
        """Monitor CPU usage"""
        while self._monitoring:
            self.cpu_usage.append(psutil.cpu_percent(interval=interval))
            time.sleep(interval)

    def profile_function(self, func_name):
        """Decorator to profile function execution time"""
        def decorator(func):
            def wrapper(*args, **kwargs):
                start_time = time.perf_counter()
                result = func(*args, **kwargs)
                end_time = time.perf_counter()

                execution_time = end_time - start_time
                self.function_times[func_name].append(execution_time)
                return result
            return wrapper
        return decorator

    def get_report(self):
        """Generate profiling report"""
        report = {
            'cpu_usage': {
                'average': sum(self.cpu_usage) / len(self.cpu_usage) if self.cpu_usage else 0,
                'max': max(self.cpu_usage) if self.cpu_usage else 0,
                'min': min(self.cpu_usage) if self.cpu_usage else 0
            },
            'function_times': {}
        }

        for func_name, times in self.function_times.items():
            report['function_times'][func_name] = {
                'calls': len(times),
                'total_time': sum(times),
                'average_time': sum(times) / len(times),
                'max_time': max(times),
                'min_time': min(times)
            }

        return report

# Usage
profiler = CPUProfiler()
profiler.start_monitoring()

@profiler.profile_function('data_processing')
def process_data(data):
    # Processing code
    time.sleep(0.1)
    return data * 2

# Run some operations
for i in range(10):
    process_data(i)

profiler.stop_monitoring()
report = profiler.get_report()
print(report)
```

### Thread Analysis

```python
import threading
import time
from collections import defaultdict

class ThreadProfiler:
    def __init__(self):
        self.thread_times = defaultdict(list)
        self.active_threads = set()

    def profile_thread(self, thread_name):
        """Decorator to profile thread execution"""
        def decorator(func):
            def wrapper(*args, **kwargs):
                thread_id = threading.current_thread().ident
                self.active_threads.add(thread_id)

                start_time = time.perf_counter()
                try:
                    result = func(*args, **kwargs)
                    return result
                finally:
                    end_time = time.perf_counter()
                    execution_time = end_time - start_time
                    self.thread_times[thread_name].append(execution_time)
                    self.active_threads.discard(thread_id)
            return wrapper
        return decorator

    def get_thread_report(self):
        """Generate thread profiling report"""
        return {
            'thread_count': len(self.active_threads),
            'thread_times': dict(self.thread_times)
        }
```

## GPU Profiling

### NVIDIA GPU Profiling

```python
import torch
import time

class GPUProfiler:
    def __init__(self):
        self.gpu_usage = []
        self.memory_usage = []
        self.gpu_times = defaultdict(list)

    def profile_gpu_function(self, func_name):
        """Decorator to profile GPU function execution"""
        def decorator(func):
            def wrapper(*args, **kwargs):
                if not torch.cuda.is_available():
                    return func(*args, **kwargs)

                torch.cuda.synchronize()  # Wait for all GPU operations to complete
                start_time = time.perf_counter()

                result = func(*args, **kwargs)

                torch.cuda.synchronize()  # Wait for completion
                end_time = time.perf_counter()

                execution_time = end_time - start_time
                self.gpu_times[func_name].append(execution_time)

                # Record GPU memory usage
                memory_allocated = torch.cuda.memory_allocated() / 1024**2  # MB
                memory_reserved = torch.cuda.memory_reserved() / 1024**2   # MB
                self.memory_usage.append((memory_allocated, memory_reserved))

                return result
            return wrapper
        return decorator

    def get_gpu_report(self):
        """Generate GPU profiling report"""
        if not torch.cuda.is_available():
            return {"error": "CUDA not available"}

        report = {
            'device': torch.cuda.get_device_name(),
            'device_count': torch.cuda.device_count(),
            'memory_summary': torch.cuda.memory_summary(),
            'function_times': {}
        }

        for func_name, times in self.gpu_times.items():
            report['function_times'][func_name] = {
                'calls': len(times),
                'total_time': sum(times),
                'average_time': sum(times) / len(times),
                'max_time': max(times),
                'min_time': min(times)
            }

        if self.memory_usage:
            max_memory = max(self.memory_usage, key=lambda x: x[0])
            report['peak_memory'] = {
                'allocated_mb': max_memory[0],
                'reserved_mb': max_memory[1]
            }

        return report

# Usage
gpu_profiler = GPUProfiler()

@gpu_profiler.profile_gpu_function('model_training')
def train_step(model, optimizer, batch):
    # Training code
    pass

# Training loop
for batch in dataloader:
    train_step(model, optimizer, batch)

report = gpu_profiler.get_gpu_report()
print(report)
```

### Multi-GPU Profiling

```python
class MultiGPUProfiler:
    def __init__(self):
        self.device_profilers = {}
        if torch.cuda.is_available():
            for i in range(torch.cuda.device_count()):
                self.device_profilers[i] = GPUProfiler()

    def profile_multi_gpu_function(self, func_name):
        """Profile function across multiple GPUs"""
        def decorator(func):
            def wrapper(*args, **kwargs):
                results = {}
                for device_id, profiler in self.device_profilers.items():
                    torch.cuda.set_device(device_id)
                    decorated_func = profiler.profile_gpu_function(f"{func_name}_gpu_{device_id}")
                    result = decorated_func(func)(*args, **kwargs)
                    results[device_id] = result
                return results
            return wrapper
        return decorator

    def get_multi_gpu_report(self):
        """Generate report for all GPUs"""
        report = {}
        for device_id, profiler in self.device_profilers.items():
            report[f'gpu_{device_id}'] = profiler.get_gpu_report()
        return report
```

## Memory Profiling

### Detailed Memory Analysis

```python
import gc
import torch
from collections import defaultdict

class MemoryProfiler:
    def __init__(self):
        self.memory_snapshots = []
        self.object_counts = defaultdict(list)

    def take_snapshot(self, label=""):
        """Take a memory snapshot"""
        gc.collect()  # Force garbage collection

        snapshot = {
            'label': label,
            'timestamp': time.time(),
            'cpu_memory': psutil.Process().memory_info().rss / 1024**2,  # MB
        }

        if torch.cuda.is_available():
            snapshot.update({
                'gpu_allocated': torch.cuda.memory_allocated() / 1024**2,
                'gpu_reserved': torch.cuda.memory_reserved() / 1024**2,
                'gpu_max_allocated': torch.cuda.max_memory_allocated() / 1024**2,
            })

        self.memory_snapshots.append(snapshot)
        return snapshot

    def profile_memory_function(self, func_name):
        """Decorator to profile memory usage of a function"""
        def decorator(func):
            def wrapper(*args, **kwargs):
                # Take before snapshot
                before = self.take_snapshot(f"{func_name}_before")

                result = func(*args, **kwargs)

                # Take after snapshot
                after = self.take_snapshot(f"{func_name}_after")

                # Calculate difference
                memory_diff = {
                    'cpu_mb': after['cpu_memory'] - before['cpu_memory']
                }

                if torch.cuda.is_available():
                    memory_diff.update({
                        'gpu_allocated_mb': after['gpu_allocated'] - before['gpu_allocated'],
                        'gpu_reserved_mb': after['gpu_reserved'] - before['gpu_reserved']
                    })

                print(f"Memory usage for {func_name}: {memory_diff}")
                return result
            return wrapper
        return decorator

    def detect_memory_leaks(self, threshold_mb=10):
        """Detect potential memory leaks"""
        if len(self.memory_snapshots) < 2:
            return []

        leaks = []
        for i in range(1, len(self.memory_snapshots)):
            prev = self.memory_snapshots[i-1]
            curr = self.memory_snapshots[i]

            cpu_diff = curr['cpu_memory'] - prev['cpu_memory']
            if cpu_diff > threshold_mb:
                leaks.append({
                    'type': 'cpu',
                    'increase_mb': cpu_diff,
                    'from': prev['label'],
                    'to': curr['label']
                })

            if torch.cuda.is_available():
                gpu_diff = curr['gpu_allocated'] - prev['gpu_allocated']
                if gpu_diff > threshold_mb:
                    leaks.append({
                        'type': 'gpu',
                        'increase_mb': gpu_diff,
                        'from': prev['label'],
                        'to': curr['label']
                    })

        return leaks

# Usage
memory_profiler = MemoryProfiler()

@memory_profiler.profile_memory_function('data_loading')
def load_data():
    # Data loading code
    pass

@memory_profiler.profile_memory_function('model_inference')
def run_inference():
    # Inference code
    pass

# Run operations
load_data()
run_inference()

# Check for leaks
leaks = memory_profiler.detect_memory_leaks()
if leaks:
    print("Potential memory leaks detected:")
    for leak in leaks:
        print(f"  {leak}")
```

## Real-Time Performance

### Latency Analysis

```python
import time
from collections import deque
import statistics

class LatencyProfiler:
    def __init__(self, window_size=100):
        self.latencies = deque(maxlen=window_size)
        self.start_times = {}

    def start_timer(self, operation_id):
        """Start timing an operation"""
        self.start_times[operation_id] = time.perf_counter()

    def end_timer(self, operation_id):
        """End timing an operation and record latency"""
        if operation_id in self.start_times:
            end_time = time.perf_counter()
            latency = (end_time - self.start_times[operation_id]) * 1000  # Convert to ms
            self.latencies.append(latency)
            del self.start_times[operation_id]
            return latency
        return None

    def get_latency_stats(self):
        """Get latency statistics"""
        if not self.latencies:
            return {}

        return {
            'count': len(self.latencies),
            'mean': statistics.mean(self.latencies),
            'median': statistics.median(self.latencies),
            'p95': statistics.quantiles(self.latencies, n=20)[18],  # 95th percentile
            'p99': statistics.quantiles(self.latencies, n=100)[98],  # 99th percentile
            'min': min(self.latencies),
            'max': max(self.latencies),
            'std_dev': statistics.stdev(self.latencies) if len(self.latencies) > 1 else 0
        }

    def check_sla(self, target_latency_ms=100, percentile=95):
        """Check if latency meets SLA requirements"""
        if not self.latencies:
            return False

        p95_latency = statistics.quantiles(self.latencies, n=100)[percentile-1]
        return p95_latency <= target_latency_ms

# Usage
latency_profiler = LatencyProfiler()

def process_request(request_id, data):
    latency_profiler.start_timer(request_id)

    # Process the request
    result = process_data(data)

    latency = latency_profiler.end_timer(request_id)
    if latency:
        print(f"Request {request_id} processed in {latency:.2f}ms")

    return result

# Simulate requests
for i in range(1000):
    process_request(f"req_{i}", f"data_{i}")

stats = latency_profiler.get_latency_stats()
print("Latency Statistics:")
for key, value in stats.items():
    print(f"  {key}: {value:.2f}")

sla_met = latency_profiler.check_sla(target_latency_ms=50)
print(f"SLA met (50ms p95): {sla_met}")
```

### Throughput Analysis

```python
class ThroughputProfiler:
    def __init__(self):
        self.operations = []
        self.start_time = time.time()

    def record_operation(self, operation_type="default"):
        """Record a completed operation"""
        self.operations.append((time.time(), operation_type))

    def get_throughput_stats(self, window_seconds=60):
        """Calculate throughput statistics"""
        current_time = time.time()
        window_start = current_time - window_seconds

        # Filter operations in the time window
        window_ops = [(t, op) for t, op in self.operations if t >= window_start]

        if not window_ops:
            return {'throughput_ops_per_sec': 0}

        total_ops = len(window_ops)
        time_span = current_time - window_start
        throughput = total_ops / time_span

        # Group by operation type
        op_counts = defaultdict(int)
        for _, op_type in window_ops:
            op_counts[op_type] += 1

        return {
            'total_operations': total_ops,
            'time_window_seconds': time_span,
            'throughput_ops_per_sec': throughput,
            'operations_by_type': dict(op_counts)
        }

# Usage
throughput_profiler = ThroughputProfiler()

def process_batch(batch):
    # Process batch
    time.sleep(0.01)  # Simulate processing time
    throughput_profiler.record_operation('batch_processing')

# Simulate continuous processing
for i in range(1000):
    process_batch(f"batch_{i}")

stats = throughput_profiler.get_throughput_stats()
print(f"Throughput: {stats['throughput_ops_per_sec']:.2f} ops/sec")
```

## Network Profiling

### HTTP Request Profiling

```python
import requests
import time
from collections import defaultdict

class NetworkProfiler:
    def __init__(self):
        self.request_times = defaultdict(list)
        self.request_sizes = defaultdict(list)

    def profile_request(self, url, method='GET', **kwargs):
        """Profile an HTTP request"""
        start_time = time.perf_counter()

        response = requests.request(method, url, **kwargs)

        end_time = time.perf_counter()
        request_time = (end_time - start_time) * 1000  # Convert to ms

        # Record metrics
        self.request_times[url].append(request_time)
        self.request_sizes[url].append(len(response.content))

        return response, request_time

    def get_network_report(self):
        """Generate network profiling report"""
        report = {}

        for url, times in self.request_times.items():
            sizes = self.request_sizes[url]
            report[url] = {
                'requests': len(times),
                'avg_latency_ms': sum(times) / len(times),
                'min_latency_ms': min(times),
                'max_latency_ms': max(times),
                'avg_response_size_kb': sum(sizes) / len(sizes) / 1024,
                'total_data_kb': sum(sizes) / 1024
            }

        return report

# Usage
network_profiler = NetworkProfiler()

# Profile API calls
response, latency = network_profiler.profile_request('http://api.example.com/data')
print(f"Request took {latency:.2f}ms")

response, latency = network_profiler.profile_request('http://api.example.com/model', method='POST', json={'data': 'test'})
print(f"POST request took {latency:.2f}ms")

report = network_profiler.get_network_report()
print("Network Report:")
for url, stats in report.items():
    print(f"  {url}: {stats['avg_latency_ms']:.2f}ms avg latency")
```

## Database Profiling

### Query Performance Analysis

```python
import sqlite3
import time
from collections import defaultdict

class DatabaseProfiler:
    def __init__(self, db_path):
        self.db_path = db_path
        self.query_times = defaultdict(list)
        self.query_counts = defaultdict(int)

    def profile_query(self, query_name):
        """Decorator to profile database queries"""
        def decorator(func):
            def wrapper(*args, **kwargs):
                start_time = time.perf_counter()

                result = func(*args, **kwargs)

                end_time = time.perf_counter()
                query_time = (end_time - start_time) * 1000  # Convert to ms

                self.query_times[query_name].append(query_time)
                self.query_counts[query_name] += 1

                return result
            return wrapper
        return decorator

    def execute_profiled_query(self, query_name, query, params=None):
        """Execute a query with profiling"""
        start_time = time.perf_counter()

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        results = cursor.fetchall()
        conn.close()

        end_time = time.perf_counter()
        query_time = (end_time - start_time) * 1000

        self.query_times[query_name].append(query_time)
        self.query_counts[query_name] += 1

        return results, query_time

    def get_db_report(self):
        """Generate database profiling report"""
        report = {}

        for query_name, times in self.query_times.items():
            report[query_name] = {
                'executions': self.query_counts[query_name],
                'avg_time_ms': sum(times) / len(times),
                'min_time_ms': min(times),
                'max_time_ms': max(times),
                'total_time_ms': sum(times)
            }

        return report

# Usage
db_profiler = DatabaseProfiler('spiralcortex.db')

@db_profiler.profile_query('user_lookup')
def get_user(user_id):
    return db_profiler.execute_profiled_query(
        'user_lookup',
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    )

# Execute some queries
for i in range(100):
    get_user(i)

report = db_profiler.get_db_report()
print("Database Report:")
for query, stats in report.items():
    print(f"  {query}: {stats['avg_time_ms']:.2f}ms avg")
```

## Optimization Strategies

### Performance Optimization Workflow

```python
class PerformanceOptimizer:
    def __init__(self):
        self.baseline_metrics = {}
        self.optimization_attempts = []

    def establish_baseline(self, system_component):
        """Establish performance baseline for a component"""
        # Run profiling to get baseline metrics
        baseline = self.profile_component(system_component)
        self.baseline_metrics[system_component] = baseline
        return baseline

    def profile_component(self, component):
        """Profile a system component"""
        # This would integrate with the profilers above
        # For demonstration, return mock metrics
        return {
            'latency_ms': 50.0,
            'throughput_ops_sec': 100.0,
            'memory_mb': 256.0,
            'cpu_percent': 45.0
        }

    def apply_optimization(self, component, optimization_name, optimization_func):
        """Apply an optimization and measure impact"""
        print(f"Applying optimization: {optimization_name} to {component}")

        # Get before metrics
        before_metrics = self.profile_component(component)

        # Apply optimization
        optimization_func()

        # Get after metrics
        after_metrics = self.profile_component(component)

        # Calculate improvement
        improvement = {}
        for metric in before_metrics:
            if metric in after_metrics:
                if 'latency' in metric.lower():
                    # Lower is better for latency
                    improvement[metric] = (before_metrics[metric] - after_metrics[metric]) / before_metrics[metric] * 100
                else:
                    # Higher is better for other metrics
                    improvement[metric] = (after_metrics[metric] - before_metrics[metric]) / before_metrics[metric] * 100

        attempt = {
            'component': component,
            'optimization': optimization_name,
            'before': before_metrics,
            'after': after_metrics,
            'improvement_percent': improvement,
            'timestamp': time.time()
        }

        self.optimization_attempts.append(attempt)
        return attempt

    def get_optimization_report(self):
        """Generate optimization report"""
        successful_optimizations = []
        failed_optimizations = []

        for attempt in self.optimization_attempts:
            avg_improvement = sum(attempt['improvement_percent'].values()) / len(attempt['improvement_percent'])

            if avg_improvement > 0:
                successful_optimizations.append((attempt, avg_improvement))
            else:
                failed_optimizations.append((attempt, avg_improvement))

        # Sort by improvement
        successful_optimizations.sort(key=lambda x: x[1], reverse=True)

        return {
            'successful_optimizations': successful_optimizations,
            'failed_optimizations': failed_optimizations,
            'total_attempts': len(self.optimization_attempts)
        }

# Usage
optimizer = PerformanceOptimizer()

# Establish baseline
baseline = optimizer.establish_baseline('neural_network')
print(f"Baseline latency: {baseline['latency_ms']}ms")

# Apply optimizations
def optimize_batch_size():
    # Code to increase batch size
    pass

result = optimizer.apply_optimization(
    'neural_network',
    'increase_batch_size',
    optimize_batch_size
)

print(f"Optimization result: {result['improvement_percent']}")

# Get final report
report = optimizer.get_optimization_report()
print(f"Successful optimizations: {len(report['successful_optimizations'])}")
```

### Common Optimization Patterns

```python
# 1. Vectorization
def optimize_vectorization():
    """Replace loops with vectorized operations"""
    import numpy as np

    # Slow version
    def slow_operation(data):
        result = []
        for item in data:
            result.append(item * 2 + 1)
        return result

    # Fast version
    def fast_operation(data):
        return np.array(data) * 2 + 1

    return fast_operation

# 2. Caching
from functools import lru_cache

@lru_cache(maxsize=128)
def cached_expensive_operation(param):
    """Cache expensive operations"""
    # Expensive computation
    time.sleep(0.1)
    return param * param

# 3. Async processing
import asyncio

async def async_processing(data_batches):
    """Process data asynchronously"""
    tasks = []
    for batch in data_batches:
        task = asyncio.create_task(process_batch_async(batch))
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    return results

# 4. Memory pooling
class TensorPool:
    """Pool for reusing tensors"""
    def __init__(self):
        self.pool = {}

    def get_tensor(self, shape, dtype=torch.float32):
        key = (shape, dtype)
        if key in self.pool:
            return self.pool[key].pop()
        return torch.zeros(shape, dtype=dtype)

    def return_tensor(self, tensor):
        key = (tuple(tensor.shape), tensor.dtype)
        if key not in self.pool:
            self.pool[key] = []
        self.pool[key].append(tensor)
```

This guide provides comprehensive profiling techniques for optimizing SpiralCortex performance. Regular profiling should be integrated into the development workflow to maintain optimal performance.
