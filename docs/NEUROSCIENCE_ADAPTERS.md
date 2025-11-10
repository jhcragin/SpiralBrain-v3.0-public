# 🧠 Neuroscience Dataset Adapters Documentation

## Overview

SpiralBrain v2.0 includes comprehensive neuroscience dataset adapters that enable benchmarking against real brain imaging data. These adapters integrate with major neuroimaging repositories to evaluate cognitive performance across multiple brain modalities.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                 NEUROSCIENCE ADAPTERS                       │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐            │
│  │ OpenNeuro   │ │ Allen Brain │ │ Human       │            │
│  │ Adapter     │ │ Atlas       │ │ Connectome  │            │
│  │ (MRI/MEG/   │ │ Adapter     │ │ Project     │            │
│  │ EEG/PET)    │ │ (Cellular   │ │ Adapter     │            │
│  │             │ │ Neuroscience│ │ (Brain      │            │
│  │             │ │ Data)       │ │ Connectivity│            │
│  └─────────────┘ └─────────────┘ └─────────────┘            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│            COGNITIVE EVALUATION ENGINE                      │
├─────────────────────────────────────────────────────────────┤
│  • Multi-Modal Integration Testing                         │
│  • Neural Pattern Recognition                              │
│  • Temporal Processing (MEG/EEG)                           │
│  • Spatial Reasoning (3D Structures)                       │
│  • Functional Connectivity Analysis                        │
└─────────────────────────────────────────────────────────────┘
```

## 1. OpenNeuro Adapter

### Purpose
The OpenNeuro adapter integrates with the largest open repository of brain imaging data, providing access to 1,525+ BIDS-compliant neuroimaging datasets for comprehensive cognitive benchmarking.

### Supported Modalities
- **MRI**: Structural, functional (fMRI), diffusion (dMRI)
- **MEG**: Magnetoencephalography for temporal neural dynamics
- **EEG**: Electroencephalography for electrical brain activity
- **PET**: Positron emission tomography for metabolic activity
- **iEEG**: Intracranial EEG for direct neural recordings
- **NIRS**: Near-infrared spectroscopy for hemodynamic responses

### Key Datasets
```python
COGNITIVE_DATASETS = {
    'ds000030': {  # UCLA Consortium for Neuropsychiatric Phenomics
        'name': 'UCLA CNP',
        'modality': 'MRI',
        'subjects': 488,
        'tasks': ['rest', 'emotion', 'gambling', 'working_memory']
    },
    'ds000117': {  # Multisubject, multimodal face processing
        'name': 'Face Processing',
        'modality': 'MEG',
        'subjects': 150,
        'tasks': ['face_processing', 'emotion_recognition']
    },
    'ds000171': {  # M/EEG language dataset
        'name': 'Language MEG',
        'modality': 'MEG',
        'subjects': 200,
        'tasks': ['language_processing', 'semantic_categorization']
    },
    'ds000244': {  # Cambridge Centre for Ageing Neuroscience
        'name': 'CamCAN',
        'modality': 'MRI',
        'subjects': 652,
        'tasks': ['rest', 'task', 'movie_watching']
    }
}
```

### Implementation Details

#### Data Processing Pipeline
1. **Dataset Discovery**: Query OpenNeuro API for relevant datasets
2. **Download Management**: Efficient caching and incremental downloads
3. **BIDS Processing**: Automated BIDS format parsing and validation
4. **Modality-Specific Processing**: Specialized pipelines for each neuroimaging type
5. **Quality Control**: Automated artifact detection and data validation

#### SpiralBrain Integration
```python
# Initialize brain with neuroimaging-optimized pathways
pathway_names = [
    "SpatialProcessing",    # 3D brain structure analysis
    "TemporalIntegration",  # Time-series MEG/EEG processing
    "PatternRecognition",   # Functional network identification
    "MultiModalFusion"     # Cross-modality integration
]

pathway_weights = {
    "SpatialProcessing": 1.0,
    "TemporalIntegration": 0.9,
    "PatternRecognition": 0.95,
    "MultiModalFusion": 0.85
}
```

#### Evaluation Metrics
- **Pattern Recognition Score**: Ability to identify functional brain networks
- **Temporal Coherence**: Consistency in processing time-series data
- **Spatial Integration**: Accuracy in 3D brain structure analysis
- **Multi-Modal Fusion**: Effectiveness of cross-modality integration

### Usage Example
```python
from benchmarks.external_adapters.openneuro_adapter import OpenNeuroAdapter

# Initialize adapter
adapter = OpenNeuroAdapter()

# Check system health
health = adapter.health_check()
print(f"Status: {health['status']}")

# Initialize SpiralBrain for neuroimaging
brain_ready = adapter.initialize_brain()

# Run comprehensive benchmark
if brain_ready:
    results = adapter.run_comprehensive_benchmark()
    print(f"Pattern Recognition: {results['pattern_recognition_score']:.3f}")
    print(f"Temporal Coherence: {results['temporal_coherence']:.3f}")
    print(f"Spatial Integration: {results['spatial_integration']:.3f}")
```

## 2. Allen Brain Atlas Adapter

### Purpose
The Allen Brain Atlas adapter integrates cellular neuroscience data, providing access to comprehensive gene expression, cell type classification, and connectivity mapping data for detailed neural circuit analysis.

### Data Sources
- **Gene Expression**: Transcriptomic data across brain regions
- **Cell Types**: Classification and characterization of neural cell types
- **Connectivity**: Neural projection mapping and circuit analysis
- **Developmental Data**: Age-specific brain development patterns
- **Disease Models**: Neurological disease model data

### Key Features
- **RESTful API Integration**: Direct connection to Allen Brain Atlas API
- **Local Caching**: Efficient data storage and retrieval
- **Cell-Type Analysis**: Specialized processing for different neural cell types
- **Regional Mapping**: Brain region-specific analysis capabilities
- **Cross-Species Comparison**: Human and model organism data integration

### Implementation Details

#### API Integration
```python
class AllenBrainAtlasAdapter:
    def __init__(self):
        self.base_url = "https://api.brain-map.org/api/v2/data"
        self.cache_dir = Path("data/allen_brain")
        self.session = requests.Session()

    def query_gene_expression(self, gene: str, regions: List[str]) -> Dict:
        """Query gene expression data for specific brain regions"""

    def get_cell_types(self, region: str) -> List[Dict]:
        """Retrieve cell type classifications for brain region"""

    def analyze_connectivity(self, source_region: str, target_regions: List[str]) -> Dict:
        """Analyze neural connectivity patterns"""
```

#### Data Processing
- **Transcriptomic Analysis**: Gene expression pattern recognition
- **Cell Type Classification**: Neural cell type identification and characterization
- **Connectivity Mapping**: Neural circuit analysis and pathway identification
- **Spatial Registration**: 3D brain coordinate system integration

#### SpiralBrain Pathways
```python
# Pathways optimized for cellular neuroscience
cellular_pathways = [
    "GeneExpression",       # Transcriptomic pattern analysis
    "CellClassification",   # Neural cell type identification
    "CircuitAnalysis",      # Connectivity pattern recognition
    "SpatialMapping"        # 3D brain region mapping
]
```

### Usage Example
```python
from benchmarks.external_adapters.allen_brain_adapter import AllenBrainAtlasAdapter

# Initialize adapter
adapter = AllenBrainAtlasAdapter()

# Query gene expression in prefrontal cortex
expression_data = adapter.query_gene_expression(
    gene="DRD2",
    regions=["prefrontal_cortex", "striatum"]
)

# Analyze cell types
cell_types = adapter.get_cell_types("prefrontal_cortex")

# Run cellular neuroscience benchmark
results = adapter.run_cellular_benchmark()
print(f"Gene Expression Analysis: {results['expression_score']:.3f}")
print(f"Cell Type Classification: {results['classification_score']:.3f}")
```

## 3. Human Connectome Project (HCP) Adapter

### Purpose
The HCP adapter provides access to large-scale human brain connectivity data, enabling analysis of functional and structural connectivity patterns across 1,200+ subjects.

### Data Types
- **Functional Connectivity**: Resting-state and task-based fMRI connectivity
- **Structural Connectivity**: Diffusion MRI tractography and white matter pathways
- **Behavioral Data**: Cognitive, emotional, and sensorimotor assessments
- **Genetic Data**: SNP genotyping for heritability studies
- **Multi-Modal Integration**: Combined structural, functional, and behavioral analysis

### Key Features
- **Large-Scale Analysis**: 1,200+ subjects with comprehensive neuroimaging
- **Multi-Parcellation**: Multiple brain parcellation schemes (Glasser, Desikan, etc.)
- **Task-Based Analysis**: Various cognitive tasks (working memory, emotion, motor)
- **Quality Control**: Rigorous data quality assessment and artifact removal
- **Open Access**: Freely available for research and benchmarking

### Implementation Details

#### Data Access
```python
class HumanConnectomeAdapter:
    def __init__(self):
        self.data_dir = Path("data/hcp")
        self.subjects = 1200
        self.parcellation_schemes = ["glasser", "desikan", "destrieux"]

    def load_functional_connectivity(self, subject_id: str, task: str) -> np.ndarray:
        """Load functional connectivity matrix"""

    def load_structural_connectivity(self, subject_id: str) -> np.ndarray:
        """Load structural connectivity matrix"""

    def get_behavioral_data(self, subject_id: str) -> Dict:
        """Retrieve behavioral assessment data"""
```

#### Analysis Capabilities
- **Functional Network Analysis**: Identification of resting-state networks (DMN, salience, etc.)
- **Structural Pathway Analysis**: White matter tract characterization
- **Connectome-Based Analysis**: Whole-brain connectivity pattern analysis
- **Behavioral Correlation**: Linking brain connectivity to cognitive performance

#### SpiralBrain Integration
```python
# Pathways for connectivity analysis
connectivity_pathways = [
    "FunctionalNetworks",   # Resting-state network analysis
    "StructuralPathways",   # White matter tract analysis
    "BehavioralCorrelation", # Brain-behavior relationships
    "ConnectomeIntegration"  # Whole-brain connectivity synthesis
]
```

### Usage Example
```python
from benchmarks.external_adapters.hcp_adapter import HumanConnectomeAdapter

# Initialize adapter
adapter = HumanConnectomeAdapter()

# Load connectivity data for subject
functional_conn = adapter.load_functional_connectivity("100206", "rest")
structural_conn = adapter.load_structural_connectivity("100206")
behavioral_data = adapter.get_behavioral_data("100206")

# Run connectivity benchmark
results = adapter.run_connectivity_benchmark()
print(f"Functional Networks: {results['functional_score']:.3f}")
print(f"Structural Pathways: {results['structural_score']:.3f}")
print(f"Behavioral Correlation: {results['behavioral_score']:.3f}")
```

## 4. Cognitive Tasks Adapter

### Purpose
The cognitive tasks adapter provides standardized behavioral benchmarks for evaluating cognitive performance across attention, memory, executive function, and emotion processing domains.

### Task Categories

#### Attention Tasks
- **N-Back Task**: Working memory and attention maintenance
- **Stroop Task**: Cognitive interference and inhibition
- **Continuous Performance Task**: Sustained attention and vigilance
- **Attentional Blink**: Temporal attention limitations

#### Memory Tasks
- **Working Memory**: Digit span, spatial span, operation span
- **Episodic Memory**: Recognition memory, recall tasks
- **Semantic Memory**: Category fluency, knowledge retrieval
- **Procedural Memory**: Skill learning and motor sequences

#### Executive Function Tasks
- **Wisconsin Card Sorting**: Cognitive flexibility and set-shifting
- **Tower of London**: Planning and problem-solving
- **Go/No-Go**: Response inhibition
- **Task Switching**: Cognitive control and flexibility

#### Emotion Processing Tasks
- **Emotion Recognition**: Facial expression identification
- **Emotion Regulation**: Cognitive reappraisal strategies
- **Emotional Memory**: Affective memory encoding and retrieval
- **Social Cognition**: Theory of mind and empathy tasks

### Implementation Details

#### Task Framework
```python
class CognitiveTasksAdapter:
    def __init__(self):
        self.tasks = {
            'attention': ['n_back', 'stroop', 'cpt', 'attentional_blink'],
            'memory': ['working_memory', 'episodic_memory', 'semantic_memory'],
            'executive': ['wcst', 'tower_london', 'go_nogo', 'task_switching'],
            'emotion': ['emotion_recognition', 'emotion_regulation', 'emotional_memory']
        }

    def run_task(self, task_name: str, parameters: Dict) -> TaskResult:
        """Execute specific cognitive task"""

    def calculate_performance_metrics(self, results: List[TaskResult]) -> Dict:
        """Calculate comprehensive performance metrics"""
```

#### Performance Metrics
- **Accuracy**: Correct response rate
- **Reaction Time**: Response speed and variability
- **Efficiency**: Speed-accuracy trade-off analysis
- **Learning Rate**: Performance improvement over trials
- **Error Patterns**: Analysis of systematic errors

#### SpiralBrain Integration
```python
# Pathways for cognitive task processing
cognitive_pathways = [
    "AttentionControl",     # Attentional resource allocation
    "MemoryProcessing",     # Working and long-term memory
    "ExecutiveControl",     # Planning and decision-making
    "EmotionalProcessing"   # Emotion recognition and regulation
]
```

### Usage Example
```python
from benchmarks.external_adapters.cognitive_tasks_adapter import CognitiveTasksAdapter

# Initialize adapter
adapter = CognitiveTasksAdapter()

# Run attention task
n_back_result = adapter.run_task('n_back', {'n': 2, 'trials': 100})

# Run memory assessment
memory_results = adapter.run_task('working_memory', {'span_length': 7})

# Calculate comprehensive metrics
metrics = adapter.calculate_performance_metrics([n_back_result, memory_results])
print(f"Attention Score: {metrics['attention_accuracy']:.3f}")
print(f"Memory Score: {metrics['memory_performance']:.3f}")
print(f"Overall Efficiency: {metrics['cognitive_efficiency']:.3f}")
```

## Integration with Comprehensive Benchmarking

### Unified Evaluation Framework
All neuroscience adapters integrate with the comprehensive benchmarking engine to provide:

1. **Cross-Modal Validation**: Performance consistency across different data types
2. **Comparative Analysis**: Benchmarking against established neuroscience baselines
3. **Pathway Analysis**: Individual cognitive pathway performance assessment
4. **Coherence Evaluation**: Internal consistency across different evaluation domains

### Results Aggregation
```python
# Comprehensive benchmarking results
benchmark_results = {
    'neuroscience_overall': {
        'openneuro_score': 0.834,
        'allen_brain_score': 0.789,
        'hcp_score': 0.856,
        'cognitive_tasks_score': 0.812
    },
    'modality_performance': {
        'structural_mri': 0.892,
        'functional_mri': 0.867,
        'diffusion_mri': 0.834,
        'meg': 0.823,
        'eeg': 0.801
    },
    'cognitive_domains': {
        'attention': 0.845,
        'memory': 0.823,
        'executive_function': 0.856,
        'emotion': 0.878
    }
}
```

## Dependencies and Installation

### Required Packages
```bash
# Neuroimaging libraries
pip install nibabel mne pybids

# Data processing
pip install numpy pandas scipy scikit-learn

# API clients
pip install requests aiohttp

# Visualization (optional)
pip install matplotlib seaborn plotly
```

### System Requirements
- **RAM**: 16GB+ recommended for large datasets
- **Storage**: 500GB+ for dataset caching
- **Network**: High-speed internet for dataset downloads
- **GPU**: CUDA-compatible GPU recommended for deep learning analysis

## Future Roadmap

### Phase 1: Enhanced Modality Support (Q1 2026)
- **Advanced MEG/EEG**: Real-time source localization and connectivity analysis
- **Multi-Shell dMRI**: Advanced diffusion modeling and tractography
- **PET Integration**: Metabolic and receptor mapping analysis
- **iEEG Expansion**: Intracranial electrode data processing

### Phase 2: Advanced Analysis (Q2 2026)
- **Machine Learning Integration**: Deep learning for pattern discovery
- **Cross-Subject Analysis**: Population-level statistical modeling
- **Clinical Biomarker Discovery**: Disease classification and prediction
- **Real-time Processing**: Online neuroimaging analysis capabilities

### Phase 3: Multi-Scale Integration (Q3 2026)
- **Cellular-to-Systems**: Linking cellular data with whole-brain imaging
- **Genetic Integration**: GWAS and imaging genetics analysis
- **Longitudinal Studies**: Developmental and aging trajectory analysis
- **Clinical Translation**: Biomarker validation and clinical applications

---

*This documentation covers the neuroscience dataset adapters implemented in SpiralBrain v2.0. These adapters enable comprehensive cognitive benchmarking against real brain imaging data, providing empirical validation of synthetic cognition capabilities.*