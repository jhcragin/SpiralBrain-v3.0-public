# Internal API Documentation

This document provides comprehensive documentation for SpiralCortex's internal APIs, integration patterns, and communication protocols.

## Table of Contents

- [API Architecture](#api-architecture)
- [Core Components](#core-components)
- [Data Flow Patterns](#data-flow-patterns)
- [Integration APIs](#integration-apis)
- [Communication Protocols](#communication-protocols)
- [Error Handling](#error-handling)
- [Testing APIs](#testing-apis)

## API Architecture

### Overview

SpiralCortex uses a modular API architecture with clear separation of concerns:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   External APIs │    │  Internal APIs  │    │ Core Components │
│                 │    │                 │    │                 │
│ - REST/GraphQL  │◄──►│ - Component APIs│◄──►│ - Neural Models │
│ - WebSocket     │    │ - Data Flow APIs│    │ - Data Processors│
│ - gRPC          │    │ - Control APIs  │    │ - Storage Layer │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### API Layers

1. **External API Layer**: Public interfaces for client applications
2. **Internal API Layer**: Component communication and data flow
3. **Core Component Layer**: Business logic and data processing

## Core Components

### Neural Processing API

```python
from spiral_cortex.core.neural import NeuralProcessor, ModelConfig

class NeuralAPI:
    """API for neural network operations"""

    def __init__(self, config: ModelConfig):
        self.processor = NeuralProcessor(config)

    async def process_modalities(self, modalities: Dict[str, torch.Tensor]) -> ProcessingResult:
        """
        Process multiple input modalities through neural networks.

        Args:
            modalities: Dictionary mapping modality names to input tensors
                - 'physiological': Tensor of shape (batch, time, features)
                - 'emotional': Tensor of shape (batch, time, emotion_dims)
                - 'cognitive': Tensor of shape (batch, time, cognitive_features)
                - 'environmental': Tensor of shape (batch, time, env_features)

        Returns:
            ProcessingResult containing:
                - fused_features: Combined representation
                - attention_weights: Modality importance scores
                - predictions: Task-specific outputs
                - confidence_scores: Prediction confidence

        Raises:
            NeuralProcessingError: If processing fails
            ValidationError: If input validation fails
        """
        return await self.processor.process(modalities)

    async def update_model(self, new_weights: Dict[str, torch.Tensor]) -> bool:
        """
        Update model weights for continuous learning.

        Args:
            new_weights: Dictionary of layer names to weight tensors

        Returns:
            bool: True if update successful

        Raises:
            ModelUpdateError: If weight update fails
        """
        return await self.processor.update_weights(new_weights)

    def get_model_info(self) -> ModelInfo:
        """
        Get current model information and capabilities.

        Returns:
            ModelInfo containing:
                - architecture: Model architecture details
                - input_requirements: Expected input formats
                - output_capabilities: Available outputs
                - performance_metrics: Current performance stats
        """
        return self.processor.get_info()
```

### Data Processing API

```python
from spiral_cortex.core.data import DataProcessor, DataPipeline
from typing import AsyncGenerator, List

class DataProcessingAPI:
    """API for data ingestion and preprocessing"""

    def __init__(self, pipeline_config: PipelineConfig):
        self.pipeline = DataPipeline(pipeline_config)

    async def ingest_stream(self, stream_id: str, data_generator: AsyncGenerator[RawData, None]) -> str:
        """
        Ingest a real-time data stream for processing.

        Args:
            stream_id: Unique identifier for the data stream
            data_generator: Async generator yielding RawData objects

        Returns:
            str: Processing job ID for tracking

        Raises:
            StreamIngestionError: If stream setup fails
        """
        return await self.pipeline.ingest_stream(stream_id, data_generator)

    async def process_batch(self, batch: DataBatch) -> ProcessedBatch:
        """
        Process a batch of data through the preprocessing pipeline.

        Args:
            batch: DataBatch containing:
                - physiological_data: Sensor readings
                - metadata: Timing and quality information
                - context: Environmental context

        Returns:
            ProcessedBatch with:
                - normalized_data: Preprocessed sensor data
                - quality_metrics: Data quality assessments
                - features: Extracted features
                - processing_stats: Performance metrics

        Raises:
            DataProcessingError: If batch processing fails
        """
        return await self.pipeline.process_batch(batch)

    async def get_stream_status(self, stream_id: str) -> StreamStatus:
        """
        Get the current status of a data stream.

        Args:
            stream_id: Stream identifier

        Returns:
            StreamStatus containing:
                - active: Whether stream is currently active
                - last_update: Timestamp of last data received
                - data_rate: Current data ingestion rate
                - buffer_status: Queue/buffer utilization
                - error_count: Number of processing errors
        """
        return await self.pipeline.get_stream_status(stream_id)

    def validate_data_format(self, data: RawData) -> ValidationResult:
        """
        Validate data format and quality requirements.

        Args:
            data: Raw data to validate

        Returns:
            ValidationResult with:
                - is_valid: Boolean validation result
                - errors: List of validation errors
                - warnings: List of validation warnings
                - quality_score: Overall data quality score
        """
        return self.pipeline.validate_data(data)
```

### Storage API

```python
from spiral_cortex.core.storage import StorageManager, QueryBuilder
from datetime import datetime, timedelta

class StorageAPI:
    """API for data storage and retrieval operations"""

    def __init__(self, storage_config: StorageConfig):
        self.manager = StorageManager(storage_config)

    async def store_session_data(self, session_id: str, data: SessionData) -> bool:
        """
        Store a complete session's data.

        Args:
            session_id: Unique session identifier
            data: SessionData containing:
                - physiological_data: Time-series sensor data
                - emotional_states: Emotional state predictions
                - cognitive_metrics: Cognitive performance data
                - metadata: Session metadata (start time, duration, etc.)

        Returns:
            bool: True if storage successful

        Raises:
            StorageError: If storage operation fails
        """
        return await self.manager.store_session(session_id, data)

    async def retrieve_session_data(self, session_id: str, time_range: Optional[TimeRange] = None) -> SessionData:
        """
        Retrieve stored session data.

        Args:
            session_id: Session identifier
            time_range: Optional time range for partial retrieval

        Returns:
            SessionData: Complete or partial session data

        Raises:
            NotFoundError: If session not found
            StorageError: If retrieval fails
        """
        return await self.manager.retrieve_session(session_id, time_range)

    async def query_sessions(self, query: SessionQuery) -> List[SessionSummary]:
        """
        Query sessions based on criteria.

        Args:
            query: SessionQuery with filters:
                - date_range: Date range filter
                - user_id: User identifier filter
                - data_quality: Minimum quality threshold
                - tags: Session tags filter

        Returns:
            List[SessionSummary]: Matching session summaries

        Raises:
            QueryError: If query execution fails
        """
        return await self.manager.query_sessions(query)

    async def export_data(self, export_request: ExportRequest) -> ExportResult:
        """
        Export data in specified format.

        Args:
            export_request: ExportRequest containing:
                - sessions: List of session IDs to export
                - format: Export format (JSON, CSV, Parquet)
                - compression: Compression method
                - destination: Export destination

        Returns:
            ExportResult with:
                - success: Export success status
                - file_path: Path to exported file
                - record_count: Number of records exported
                - file_size: Size of exported file

        Raises:
            ExportError: If export operation fails
        """
        return await self.manager.export_data(export_request)

    async def cleanup_old_data(self, retention_days: int) -> CleanupResult:
        """
        Clean up old data based on retention policy.

        Args:
            retention_days: Number of days to retain data

        Returns:
            CleanupResult with:
                - deleted_sessions: Number of sessions deleted
                - freed_space_mb: Space freed in MB
                - errors: Any cleanup errors encountered
        """
        cutoff_date = datetime.now() - timedelta(days=retention_days)
        return await self.manager.cleanup_data(cutoff_date)
```

## Data Flow Patterns

### Real-Time Processing Pipeline

```python
from spiral_cortex.core.pipeline import RealTimePipeline, PipelineStage

class RealTimeProcessingAPI:
    """API for real-time data processing pipelines"""

    def __init__(self):
        self.pipeline = RealTimePipeline()

    def create_pipeline(self, config: PipelineConfig) -> str:
        """
        Create a real-time processing pipeline.

        Args:
            config: PipelineConfig with:
                - input_sources: List of data sources
                - processing_stages: Ordered list of processing steps
                - output_sinks: Where to send results
                - quality_thresholds: Data quality requirements
                - latency_requirements: Maximum allowed latency

        Returns:
            str: Pipeline ID for management

        Raises:
            PipelineCreationError: If pipeline creation fails
        """
        return self.pipeline.create(config)

    async def start_pipeline(self, pipeline_id: str) -> bool:
        """
        Start a processing pipeline.

        Args:
            pipeline_id: Pipeline identifier

        Returns:
            bool: True if pipeline started successfully

        Raises:
            PipelineError: If pipeline fails to start
        """
        return await self.pipeline.start(pipeline_id)

    async def stop_pipeline(self, pipeline_id: str) -> bool:
        """
        Stop a processing pipeline.

        Args:
            pipeline_id: Pipeline identifier

        Returns:
            bool: True if pipeline stopped successfully
        """
        return await self.pipeline.stop(pipeline_id)

    async def get_pipeline_metrics(self, pipeline_id: str) -> PipelineMetrics:
        """
        Get real-time metrics for a pipeline.

        Args:
            pipeline_id: Pipeline identifier

        Returns:
            PipelineMetrics containing:
                - throughput: Data processing rate
                - latency: End-to-end processing latency
                - queue_depth: Input queue utilization
                - error_rate: Processing error rate
                - stage_metrics: Per-stage performance metrics
        """
        return await self.pipeline.get_metrics(pipeline_id)

    def add_processing_stage(self, pipeline_id: str, stage: PipelineStage) -> bool:
        """
        Add a processing stage to an existing pipeline.

        Args:
            pipeline_id: Pipeline identifier
            stage: PipelineStage to add with:
                - stage_type: Type of processing (filter, transform, aggregate)
                - config: Stage-specific configuration
                - position: Where to insert in pipeline

        Returns:
            bool: True if stage added successfully

        Raises:
            PipelineModificationError: If stage cannot be added
        """
        return self.pipeline.add_stage(pipeline_id, stage)
```

### Batch Processing API

```python
from spiral_cortex.core.batch import BatchProcessor, BatchJob

class BatchProcessingAPI:
    """API for batch data processing operations"""

    def __init__(self):
        self.processor = BatchProcessor()

    async def submit_batch_job(self, job: BatchJob) -> str:
        """
        Submit a batch processing job.

        Args:
            job: BatchJob containing:
                - job_type: Type of batch operation
                - input_data: Data to process
                - processing_config: Job configuration
                - priority: Job priority level
                - callback_url: Optional result callback

        Returns:
            str: Job ID for tracking

        Raises:
            BatchSubmissionError: If job submission fails
        """
        return await self.processor.submit_job(job)

    async def get_job_status(self, job_id: str) -> JobStatus:
        """
        Get the status of a batch job.

        Args:
            job_id: Job identifier

        Returns:
            JobStatus containing:
                - status: Current job status (queued, running, completed, failed)
                - progress: Completion percentage (0-100)
                - start_time: Job start timestamp
                - estimated_completion: Estimated completion time
                - error_message: Error details if failed
        """
        return await self.processor.get_job_status(job_id)

    async def cancel_job(self, job_id: str) -> bool:
        """
        Cancel a running or queued batch job.

        Args:
            job_id: Job identifier

        Returns:
            bool: True if job cancelled successfully

        Raises:
            JobCancellationError: If cancellation fails
        """
        return await self.processor.cancel_job(job_id)

    async def get_job_results(self, job_id: str) -> BatchResults:
        """
        Retrieve results from a completed batch job.

        Args:
            job_id: Job identifier

        Returns:
            BatchResults containing:
                - success: Whether job completed successfully
                - output_data: Processed results
                - processing_stats: Performance statistics
                - error_details: Any errors encountered

        Raises:
            JobNotCompleteError: If job not yet completed
            ResultRetrievalError: If results cannot be retrieved
        """
        return await self.processor.get_results(job_id)

    def list_active_jobs(self) -> List[JobSummary]:
        """
        List all active batch jobs.

        Returns:
            List[JobSummary]: Summaries of active jobs with:
                - job_id: Job identifier
                - job_type: Type of job
                - status: Current status
                - submitted_time: When job was submitted
                - priority: Job priority
        """
        return self.processor.list_jobs()
```

## Integration APIs

### Hardware Integration API

```python
from spiral_cortex.integrations.hardware import HardwareManager, DeviceConfig

class HardwareIntegrationAPI:
    """API for hardware device integration"""

    def __init__(self):
        self.manager = HardwareManager()

    async def register_device(self, device_config: DeviceConfig) -> str:
        """
        Register a hardware device for data collection.

        Args:
            device_config: DeviceConfig containing:
                - device_type: Type of device (sensor, wearable, etc.)
                - connection_params: Connection parameters
                - data_format: Expected data format
                - sampling_rate: Desired sampling rate
                - calibration_data: Device calibration information

        Returns:
            str: Device ID for management

        Raises:
            DeviceRegistrationError: If device registration fails
        """
        return await self.manager.register_device(device_config)

    async def start_data_collection(self, device_id: str) -> bool:
        """
        Start data collection from a registered device.

        Args:
            device_id: Device identifier

        Returns:
            bool: True if collection started successfully

        Raises:
            DeviceError: If collection cannot be started
        """
        return await self.manager.start_collection(device_id)

    async def stop_data_collection(self, device_id: str) -> bool:
        """
        Stop data collection from a device.

        Args:
            device_id: Device identifier

        Returns:
            bool: True if collection stopped successfully
        """
        return await self.manager.stop_collection(device_id)

    async def calibrate_device(self, device_id: str, calibration_data: CalibrationData) -> bool:
        """
        Calibrate a hardware device.

        Args:
            device_id: Device identifier
            calibration_data: CalibrationData with:
                - reference_values: Known reference measurements
                - calibration_procedure: Calibration steps
                - environmental_conditions: Calibration environment

        Returns:
            bool: True if calibration successful

        Raises:
            CalibrationError: If calibration fails
        """
        return await self.manager.calibrate_device(device_id, calibration_data)

    def get_device_status(self, device_id: str) -> DeviceStatus:
        """
        Get the current status of a device.

        Args:
            device_id: Device identifier

        Returns:
            DeviceStatus containing:
                - connected: Connection status
                - collecting: Data collection status
                - battery_level: Battery level (if applicable)
                - signal_quality: Signal quality metrics
                - last_data_time: Timestamp of last data received
                - error_count: Number of errors encountered
        """
        return self.manager.get_device_status(device_id)

    def list_connected_devices(self) -> List[DeviceInfo]:
        """
        List all connected and registered devices.

        Returns:
            List[DeviceInfo]: Information about connected devices
        """
        return self.manager.list_devices()
```

### External Service Integration API

```python
from spiral_cortex.integrations.external import ServiceManager, ServiceConfig

class ExternalServiceAPI:
    """API for integrating with external services"""

    def __init__(self):
        self.manager = ServiceManager()

    async def register_service(self, service_config: ServiceConfig) -> str:
        """
        Register an external service for integration.

        Args:
            service_config: ServiceConfig containing:
                - service_type: Type of service (API, database, etc.)
                - endpoint_url: Service endpoint
                - authentication: Authentication credentials
                - rate_limits: API rate limiting configuration
                - retry_policy: Error retry configuration

        Returns:
            str: Service ID for management

        Raises:
            ServiceRegistrationError: If service registration fails
        """
        return await self.manager.register_service(service_config)

    async def call_service(self, service_id: str, request: ServiceRequest) -> ServiceResponse:
        """
        Make a call to an external service.

        Args:
            service_id: Service identifier
            request: ServiceRequest with:
                - method: HTTP method (GET, POST, etc.)
                - path: API endpoint path
                - parameters: Query parameters
                - data: Request body data
                - headers: Additional headers

        Returns:
            ServiceResponse containing:
                - status_code: HTTP status code
                - data: Response data
                - headers: Response headers
                - latency_ms: Request latency

        Raises:
            ServiceCallError: If service call fails
        """
        return await self.manager.call_service(service_id, request)

    async def get_service_health(self, service_id: str) -> ServiceHealth:
        """
        Check the health status of an external service.

        Args:
            service_id: Service identifier

        Returns:
            ServiceHealth containing:
                - available: Service availability status
                - response_time_ms: Average response time
                - error_rate: Recent error rate
                - last_check: Timestamp of last health check
        """
        return await self.manager.check_service_health(service_id)

    def configure_circuit_breaker(self, service_id: str, config: CircuitBreakerConfig) -> bool:
        """
        Configure circuit breaker for service resilience.

        Args:
            service_id: Service identifier
            config: CircuitBreakerConfig with:
                - failure_threshold: Number of failures before opening
                - recovery_timeout: Time before attempting recovery
                - monitoring_window: Time window for failure counting

        Returns:
            bool: True if configuration successful

        Raises:
            ConfigurationError: If configuration fails
        """
        return self.manager.configure_circuit_breaker(service_id, config)
```

## Communication Protocols

### Internal Message Bus

```python
from spiral_cortex.core.messaging import MessageBus, Message, MessageHandler

class MessageBusAPI:
    """API for internal message passing between components"""

    def __init__(self):
        self.bus = MessageBus()

    def subscribe(self, topic: str, handler: MessageHandler) -> str:
        """
        Subscribe to messages on a topic.

        Args:
            topic: Message topic to subscribe to
            handler: MessageHandler function that takes a Message object

        Returns:
            str: Subscription ID for unsubscribing

        Raises:
            SubscriptionError: If subscription fails
        """
        return self.bus.subscribe(topic, handler)

    def unsubscribe(self, subscription_id: str) -> bool:
        """
        Unsubscribe from a topic.

        Args:
            subscription_id: Subscription identifier

        Returns:
            bool: True if unsubscribed successfully
        """
        return self.bus.unsubscribe(subscription_id)

    async def publish(self, topic: str, message: Message) -> bool:
        """
        Publish a message to a topic.

        Args:
            topic: Topic to publish to
            message: Message object with:
                - message_id: Unique message identifier
                - payload: Message data
                - metadata: Message metadata (timestamp, source, etc.)
                - priority: Message priority level

        Returns:
            bool: True if message published successfully

        Raises:
            PublishError: If message cannot be published
        """
        return await self.bus.publish(topic, message)

    def get_topic_stats(self, topic: str) -> TopicStats:
        """
        Get statistics for a message topic.

        Args:
            topic: Topic name

        Returns:
            TopicStats containing:
                - subscriber_count: Number of active subscribers
                - message_rate: Messages per second
                - queue_depth: Pending message queue depth
                - error_count: Number of delivery errors
        """
        return self.bus.get_topic_stats(topic)

    def create_topic(self, topic: str, config: TopicConfig) -> bool:
        """
        Create a new message topic with configuration.

        Args:
            topic: Topic name
            config: TopicConfig with:
                - persistence: Whether to persist messages
                - retention_policy: Message retention settings
                - max_queue_size: Maximum queue size
                - delivery_guarantee: Delivery guarantee level

        Returns:
            bool: True if topic created successfully

        Raises:
            TopicCreationError: If topic creation fails
        """
        return self.bus.create_topic(topic, config)
```

### WebSocket Communication

```python
from spiral_cortex.core.websocket import WebSocketManager, ConnectionConfig
import asyncio

class WebSocketAPI:
    """API for WebSocket-based real-time communication"""

    def __init__(self):
        self.manager = WebSocketManager()

    async def create_endpoint(self, path: str, config: ConnectionConfig) -> str:
        """
        Create a WebSocket endpoint.

        Args:
            path: URL path for the endpoint
            config: ConnectionConfig with:
                - message_format: Expected message format
                - heartbeat_interval: Heartbeat interval in seconds
                - max_connections: Maximum concurrent connections
                - authentication_required: Whether authentication is required

        Returns:
            str: Endpoint ID for management

        Raises:
            EndpointCreationError: If endpoint creation fails
        """
        return await self.manager.create_endpoint(path, config)

    async def broadcast_message(self, endpoint_id: str, message: WebSocketMessage) -> int:
        """
        Broadcast a message to all connected clients.

        Args:
            endpoint_id: Endpoint identifier
            message: WebSocketMessage with:
                - message_type: Type of message
                - payload: Message data
                - target_clients: Optional list of target client IDs

        Returns:
            int: Number of clients message was sent to

        Raises:
            BroadcastError: If broadcast fails
        """
        return await self.manager.broadcast(endpoint_id, message)

    async def send_to_client(self, endpoint_id: str, client_id: str, message: WebSocketMessage) -> bool:
        """
        Send a message to a specific client.

        Args:
            endpoint_id: Endpoint identifier
            client_id: Target client identifier
            message: Message to send

        Returns:
            bool: True if message sent successfully

        Raises:
            ClientNotFoundError: If client not connected
            SendError: If message send fails
        """
        return await self.manager.send_to_client(endpoint_id, client_id, message)

    def get_connection_stats(self, endpoint_id: str) -> ConnectionStats:
        """
        Get connection statistics for an endpoint.

        Args:
            endpoint_id: Endpoint identifier

        Returns:
            ConnectionStats containing:
                - active_connections: Number of active connections
                - total_connections: Total connections since startup
                - messages_sent: Total messages sent
                - messages_received: Total messages received
                - connection_uptime_avg: Average connection duration
        """
        return self.manager.get_connection_stats(endpoint_id)

    def set_message_handler(self, endpoint_id: str, handler: MessageHandler) -> bool:
        """
        Set a message handler for incoming WebSocket messages.

        Args:
            endpoint_id: Endpoint identifier
            handler: MessageHandler function that takes (client_id, message)

        Returns:
            bool: True if handler set successfully

        Raises:
            HandlerError: If handler cannot be set
        """
        return self.manager.set_message_handler(endpoint_id, handler)
```

## Error Handling

### Error Types and Codes

```python
from enum import Enum
from typing import Dict, Any

class ErrorCode(Enum):
    """Standardized error codes for API responses"""

    # General errors
    INTERNAL_ERROR = "INTERNAL_ERROR"
    INVALID_REQUEST = "INVALID_REQUEST"
    UNAUTHORIZED = "UNAUTHORIZED"
    FORBIDDEN = "FORBIDDEN"
    NOT_FOUND = "NOT_FOUND"

    # Neural processing errors
    NEURAL_PROCESSING_FAILED = "NEURAL_PROCESSING_FAILED"
    MODEL_NOT_FOUND = "MODEL_NOT_FOUND"
    INVALID_MODEL_INPUT = "INVALID_MODEL_INPUT"

    # Data processing errors
    DATA_VALIDATION_FAILED = "DATA_VALIDATION_FAILED"
    STREAM_INGESTION_FAILED = "STREAM_INGESTION_FAILED"
    BATCH_PROCESSING_FAILED = "BATCH_PROCESSING_FAILED"

    # Storage errors
    STORAGE_OPERATION_FAILED = "STORAGE_OPERATION_FAILED"
    DATA_NOT_FOUND = "DATA_NOT_FOUND"
    EXPORT_FAILED = "EXPORT_FAILED"

    # Hardware errors
    DEVICE_CONNECTION_FAILED = "DEVICE_CONNECTION_FAILED"
    HARDWARE_CALIBRATION_FAILED = "HARDWARE_CALIBRATION_FAILED"

    # External service errors
    SERVICE_UNAVAILABLE = "SERVICE_UNAVAILABLE"
    SERVICE_TIMEOUT = "SERVICE_TIMEOUT"

class APIError(Exception):
    """Base exception for API errors"""

    def __init__(self, code: ErrorCode, message: str, details: Dict[str, Any] = None):
        self.code = code
        self.message = message
        self.details = details or {}

    def to_dict(self) -> Dict[str, Any]:
        """Convert error to dictionary for API responses"""
        return {
            "error": {
                "code": self.code.value,
                "message": self.message,
                "details": self.details
            }
        }
```

### Error Response Format

```python
from typing import Union

def create_error_response(error: Union[APIError, Exception]) -> Dict[str, Any]:
    """
    Create standardized error response.

    Args:
        error: Exception to convert to response

    Returns:
        Dict containing standardized error format
    """
    if isinstance(error, APIError):
        return error.to_dict()
    else:
        # Handle unexpected exceptions
        return {
            "error": {
                "code": ErrorCode.INTERNAL_ERROR.value,
                "message": "An unexpected error occurred",
                "details": {
                    "exception_type": type(error).__name__,
                    "exception_message": str(error)
                }
            }
        }

# Usage in API endpoints
async def api_endpoint(request):
    try:
        # API logic here
        result = await process_request(request)
        return {"success": True, "data": result}
    except APIError as e:
        return create_error_response(e)
    except Exception as e:
        # Log unexpected errors
        logger.error(f"Unexpected error in api_endpoint: {e}")
        return create_error_response(e)
```

### Error Recovery Strategies

```python
from typing import Callable, Any
import asyncio
import time

class ErrorRecovery:
    """Strategies for handling and recovering from errors"""

    @staticmethod
    async def retry_with_backoff(func: Callable, max_attempts: int = 3,
                                base_delay: float = 1.0, max_delay: float = 60.0) -> Any:
        """
        Retry a function with exponential backoff.

        Args:
            func: Function to retry
            max_attempts: Maximum number of retry attempts
            base_delay: Base delay between retries in seconds
            max_delay: Maximum delay between retries in seconds

        Returns:
            Result of successful function call

        Raises:
            Last exception if all retries fail
        """
        last_exception = None

        for attempt in range(max_attempts):
            try:
                return await func()
            except Exception as e:
                last_exception = e

                if attempt < max_attempts - 1:
                    delay = min(base_delay * (2 ** attempt), max_delay)
                    await asyncio.sleep(delay)

        raise last_exception

    @staticmethod
    def circuit_breaker(func: Callable, failure_threshold: int = 5,
                       recovery_timeout: float = 60.0) -> Callable:
        """
        Circuit breaker decorator for service calls.

        Args:
            func: Function to protect with circuit breaker
            failure_threshold: Number of failures before opening circuit
            recovery_timeout: Time before attempting recovery

        Returns:
            Decorated function with circuit breaker protection
        """
        failure_count = 0
        last_failure_time = 0
        circuit_open = False

        def wrapper(*args, **kwargs):
            nonlocal failure_count, last_failure_time, circuit_open

            current_time = time.time()

            # Check if circuit should be closed (recovery timeout passed)
            if circuit_open and (current_time - last_failure_time) > recovery_timeout:
                circuit_open = False
                failure_count = 0

            # If circuit is open, fail fast
            if circuit_open:
                raise APIError(ErrorCode.SERVICE_UNAVAILABLE,
                             "Service temporarily unavailable (circuit breaker open)")

            try:
                result = func(*args, **kwargs)
                # Success - reset failure count
                failure_count = 0
                return result
            except Exception as e:
                failure_count += 1
                last_failure_time = current_time

                # Open circuit if failure threshold reached
                if failure_count >= failure_threshold:
                    circuit_open = True

                raise e

        return wrapper

    @staticmethod
    def fallback_handler(primary_func: Callable, fallback_func: Callable) -> Callable:
        """
        Execute primary function with fallback on failure.

        Args:
            primary_func: Primary function to execute
            fallback_func: Fallback function to execute on primary failure

        Returns:
            Decorated function with fallback behavior
        """
        def wrapper(*args, **kwargs):
            try:
                return primary_func(*args, **kwargs)
            except Exception as e:
                # Log the primary failure
                logger.warning(f"Primary function failed, using fallback: {e}")
                return fallback_func(*args, **kwargs)

        return wrapper
```

## Testing APIs

### Component Testing API

```python
from spiral_cortex.testing import ComponentTester, TestSuite, TestResult
import pytest

class ComponentTestingAPI:
    """API for testing system components"""

    def __init__(self):
        self.tester = ComponentTester()

    async def run_component_tests(self, component_name: str, test_config: TestConfig) -> TestResult:
        """
        Run tests for a specific component.

        Args:
            component_name: Name of component to test
            test_config: TestConfig with:
                - test_types: Types of tests to run (unit, integration, performance)
                - test_data: Test data and fixtures
                - timeout_seconds: Test execution timeout
                - parallel_execution: Whether to run tests in parallel

        Returns:
            TestResult containing:
                - success: Overall test success
                - passed_tests: Number of tests passed
                - failed_tests: Number of tests failed
                - test_duration: Total test execution time
                - coverage_report: Code coverage metrics
                - error_details: Details of failed tests

        Raises:
            TestExecutionError: If test execution fails
        """
        return await self.tester.run_component_tests(component_name, test_config)

    async def run_integration_tests(self, components: List[str]) -> IntegrationTestResult:
        """
        Run integration tests between components.

        Args:
            components: List of component names to test together

        Returns:
            IntegrationTestResult with:
                - component_interactions: Tested interaction patterns
                - data_flow_validation: Data flow correctness
                - performance_under_load: Load testing results
                - error_handling: Error propagation testing
        """
        return await self.tester.run_integration_tests(components)

    def create_test_suite(self, suite_name: str, tests: List[TestCase]) -> str:
        """
        Create a custom test suite.

        Args:
            suite_name: Name for the test suite
            tests: List of TestCase objects with:
                - test_name: Name of the test
                - test_function: Test function to execute
                - setup_function: Optional setup function
                - teardown_function: Optional teardown function
                - expected_result: Expected test outcome

        Returns:
            str: Test suite ID for execution

        Raises:
            TestSuiteCreationError: If suite creation fails
        """
        return self.tester.create_test_suite(suite_name, tests)

    async def run_performance_tests(self, component_name: str, load_config: LoadConfig) -> PerformanceTestResult:
        """
        Run performance tests under load.

        Args:
            component_name: Component to performance test
            load_config: LoadConfig with:
                - concurrent_users: Number of concurrent operations
                - request_rate: Requests per second
                - duration_seconds: Test duration
                - resource_limits: System resource limits

        Returns:
            PerformanceTestResult containing:
                - throughput: Operations per second
                - latency_percentiles: Response time percentiles
                - resource_utilization: CPU, memory, I/O usage
                - error_rate: Percentage of failed operations
                - scalability_metrics: Performance scaling characteristics
        """
        return await self.tester.run_performance_tests(component_name, load_config)

    def get_test_history(self, component_name: str, days: int = 30) -> List[TestResult]:
        """
        Get historical test results for a component.

        Args:
            component_name: Component name
            days: Number of days of history to retrieve

        Returns:
            List[TestResult]: Historical test results
        """
        return self.tester.get_test_history(component_name, days)

    def generate_test_report(self, test_results: List[TestResult]) -> TestReport:
        """
        Generate a comprehensive test report.

        Args:
            test_results: List of test results to include

        Returns:
            TestReport with:
                - summary_statistics: Overall test statistics
                - trend_analysis: Test result trends over time
                - failure_analysis: Common failure patterns
                - recommendations: Suggested improvements
        """
        return self.tester.generate_report(test_results)
```

This documentation provides comprehensive coverage of SpiralCortex's internal APIs and integration patterns. All APIs follow consistent patterns for error handling, logging, and monitoring to ensure reliable operation.
