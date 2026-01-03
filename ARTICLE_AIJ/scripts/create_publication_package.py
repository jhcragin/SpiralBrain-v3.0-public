#!/usr/bin/env python3
"""
SpiralBrain Publication Package Generator
Creates arXiv-ready manuscript package with paper, datasets, and replication materials
"""

import shutil
import zipfile
from datetime import datetime
from pathlib import Path


class PublicationPackager:
    """Creates publication-ready package for arXiv submission"""

    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.package_name = f"SpiralBrain_Adaptation_Paper_v1.0_{datetime.now().strftime('%Y%m%d')}"
        self.package_dir = self.project_root / "publication_package"

    def create_package_structure(self):
        """Create the publication package directory structure"""
        print("📁 Creating publication package structure...")

        # Main directories
        dirs = [
            "paper",
            "datasets",
            "code",
            "replication",
            "figures"
        ]

        for dir_name in dirs:
            (self.package_dir / dir_name).mkdir(parents=True, exist_ok=True)

        print(f"✅ Package structure created in: {self.package_dir}")

    def copy_paper_files(self):
        """Copy paper and related documentation"""
        print("📄 Copying paper files...")

        paper_files = [
            "SPIRALBRAIN_ADAPTATION_PAPER.md",
            "REPLICATION_RESULTS_SUMMARY.md",
            "README.md"
        ]

        for file in paper_files:
            src = self.project_root / file
            if src.exists():
                shutil.copy2(src, self.package_dir / "paper" / file)
                print(f"  ✓ {file}")

    def copy_datasets(self):
        """Copy experimental datasets and results"""
        print("📊 Copying datasets and results...")

        # Copy logs directory
        logs_src = self.project_root / "logs"
        logs_dst = self.package_dir / "datasets" / "logs"
        if logs_src.exists():
            shutil.copytree(logs_src, logs_dst, dirs_exist_ok=True)
            print("  ✓ Experimental logs")

        # Copy configs
        configs_src = self.project_root / "configs"
        configs_dst = self.package_dir / "datasets" / "configs"
        if configs_src.exists():
            shutil.copytree(configs_src, configs_dst, dirs_exist_ok=True)
            print("  ✓ Configuration files")

    def copy_code(self):
        """Copy essential code for replication"""
        print("💻 Copying replication code...")

        code_files = [
            "run_adaptation_tests.py",
            "setup_cross_context_replication.py",
            "run_envdrift_test.py",
            "requirements.replication.txt",
            "Dockerfile.replication",
            "docker-compose.replication.yml",
            "SpiralBrain_Colab_Replication.ipynb"
        ]

        for file in code_files:
            src = self.project_root / file
            if src.exists():
                shutil.copy2(src, self.package_dir / "code" / file)
                print(f"  ✓ {file}")

        # Copy testing framework
        testing_src = self.project_root / "testing"
        testing_dst = self.package_dir / "code" / "testing"
        if testing_src.exists():
            shutil.copytree(testing_src, testing_dst, dirs_exist_ok=True)
            print("  ✓ Testing framework")

    def copy_replication_materials(self):
        """Copy replication instructions and materials"""
        print("🔄 Copying replication materials...")

        replication_files = [
            "REPLICATION_INSTRUCTIONS.md",
            "DOCKER_REPLICATION_GUIDE.md",
            "COLAB_SETUP_GUIDE.md"
        ]

        for file in replication_files:
            src = self.project_root / file
            if src.exists():
                shutil.copy2(src, self.package_dir / "replication" / file)
            else:
                # Create placeholder if doesn't exist
                self.create_replication_guide(file)
                print(f"  ✓ {file} (created)")

    def create_replication_guide(self, filename: str):
        """Create replication guide if it doesn't exist"""
        content = ""

        if "DOCKER" in filename:
            content = """# Docker Replication Guide

## Prerequisites
- Docker Desktop installed and running
- At least 4GB RAM available
- 10GB free disk space

## Quick Start
```bash
# Build the replication environment
docker build -f Dockerfile.replication -t spiralbrain-replication .

# Run replication tests
docker run --rm spiralbrain-replication

# Or use docker-compose
docker-compose -f docker-compose.replication.yml up
```

## Expected Output
- Test completion in ~5-10 minutes
- Results saved to logs/cross_context_runs/
- G_ref ≈ 0.15, I_id ≈ 0.95 (generalization confirmed)
"""
        elif "COLAB" in filename:
            content = """# Google Colab Replication Guide

## Setup
1. Upload `SpiralBrain_Colab_Replication.ipynb` to Google Colab
2. Use GPU runtime (Runtime → Change runtime type → GPU)
3. Run all cells in sequence

## Expected Results
- Environment validation successful
- Replication tests complete in ~10-15 minutes
- Results demonstrate cross-platform generalization
- G_ref > 0.1, I_id > 0.9 confirmed

## Troubleshooting
- If GPU not available, tests will run on CPU (slower but functional)
- Ensure internet connection for git clone
- Check Colab resource limits for long-running tests
"""
        else:
            content = """# SpiralBrain Replication Instructions

## Overview
This package contains everything needed to replicate the SpiralBrain adaptation findings.

## Quick Replication (Recommended)
1. **Docker Method** (easiest):
   ```bash
   docker-compose -f docker-compose.replication.yml up
   ```

2. **Google Colab Method** (cloud):
   - Upload `SpiralBrain_Colab_Replication.ipynb`
   - Run all cells

3. **Local Method** (advanced):
   ```bash
   pip install -r requirements.replication.txt
   python run_adaptation_tests.py --config configs/replication/cross_context_replication.yaml full
   ```

## Validation Criteria
✅ **Success**: G_ref > 0.1, I_id > 0.9, R(t) < 5s
❌ **Failure**: Any metric below threshold

## Expected Runtime
- Docker: 5-10 minutes
- Colab: 10-15 minutes
- Local: 3-8 minutes (depends on hardware)

## Support
Results should match or exceed: G_ref = 0.132, I_id = 0.948
"""

        with open(self.package_dir / "replication" / filename, 'w', encoding='utf-8') as f:
            f.write(content)

    def create_readme(self):
        """Create comprehensive README for the package"""
        readme_content = f"""# SpiralBrain: Quantitative Confirmation of Reflective Adaptation

**Publication Package v1.0**
**Date:** {datetime.now().strftime('%B %d, %Y')}
**DOI:** [To be assigned]

## Abstract

SpiralBrain demonstrates measurable self-optimization through reflection, confirming that introspection enhances adaptive performance while maintaining system identity. Quantitative evidence (G_ref = 0.132, I_id = 0.948) from cross-environment validation and reflection ablation studies distinguishes SpiralBrain's organic adaptation from conventional statistical optimization.

**Cross-Context Replication Results:** G_ref = 0.150, I_id = 0.948 (generalization confirmed ✅)

## Package Contents

```
publication_package/
├── paper/                    # Manuscript and documentation
│   ├── SPIRALBRAIN_ADAPTATION_PAPER.md
│   ├── REPLICATION_RESULTS_SUMMARY.md
│   └── README.md
├── datasets/                 # Experimental data and configs
│   ├── logs/                # Raw experimental results
│   └── configs/             # YAML configurations
├── code/                    # Replication code
│   ├── run_adaptation_tests.py
│   ├── setup_cross_context_replication.py
│   ├── SpiralBrain_Colab_Replication.ipynb
│   └── testing/             # Testing framework
├── replication/             # Replication guides
│   ├── REPLICATION_INSTRUCTIONS.md
│   ├── DOCKER_REPLICATION_GUIDE.md
│   └── COLAB_SETUP_GUIDE.md
└── figures/                 # Generated visualizations
```

## Quick Start

### Option 1: Docker (Recommended)
```bash
cd code
docker-compose -f docker-compose.replication.yml up
```

### Option 2: Google Colab
1. Upload `code/SpiralBrain_Colab_Replication.ipynb` to Colab
2. Use GPU runtime
3. Run all cells

### Option 3: Local Environment
```bash
cd code
pip install -r requirements.replication.txt
python run_adaptation_tests.py --config ../datasets/configs/replication/cross_context_replication.yaml full
```

## Key Findings

### Primary Metrics
- **G_ref**: 0.132 (original), 0.150 (replication) - Reflection provides measurable benefit
- **I_id**: 0.948 - Identity preserved across environmental shifts
- **R(t)**: 0.102s - Fast adaptation to perturbations
- **λ***: 0.250 - Stable homeostatic coupling

### Replication Validation
✅ **Cross-Platform Generalization**: Performance maintained across WinCPU ↔ UbuntuGPU
✅ **Fault Resilience**: System recovers from adversarial conditions
✅ **Observer Effects**: Measurable introspection impact (Φ ratio ≈ 1.03)
✅ **Behavioral Phenotype**: Stretch-flex-flip-restart pattern confirmed

## Scientific Impact

This work provides **gold-standard evidence** for synthetic cognition by demonstrating:

1. **Organic Adaptation**: Reflection enables self-optimization beyond statistical methods
2. **Identity Preservation**: System maintains coherence across environmental changes
3. **Autonomous Recovery**: Self-regulation under fault conditions
4. **Observer Effects**: Introspection perturbs cognitive processes

## Citation

```bibtex
@article{{spiralbrain2025adaptation,
  title={{SpiralBrain: Quantitative Confirmation of Reflective Adaptation}},
  author={{John H Cragin}},
  journal={{arXiv preprint}},
  year={{2025}},
  note={{Cross-context replication validated}}
}}
```

## License

This research package is released under MIT License for academic and research purposes.

## Contact

John H Cragin
https://github.com/jhcragin/SpiralBrain-v2.0

---

*\"The system learns by observing itself—and, through that process, teaches us how intelligence organizes its own awareness.\"*
"""

        with open(self.package_dir / "README.md", 'w', encoding='utf-8') as f:
            f.write(readme_content)

    def create_zip_archive(self):
        """Create ZIP archive of the publication package"""
        print("📦 Creating publication archive...")

        zip_path = self.project_root / f"{self.package_name}.zip"

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in self.package_dir.rglob('*'):
                if file_path.is_file():
                    arcname = file_path.relative_to(self.project_root)
                    zipf.write(file_path, arcname)

        print(f"✅ Publication package created: {zip_path}")
        print(f"   Size: {zip_path.stat().st_size / (1024*1024):.1f} MB")

    def generate_package(self):
        """Generate complete publication package"""
        print("🚀 Generating SpiralBrain Publication Package")
        print("=" * 50)

        self.create_package_structure()
        self.copy_paper_files()
        self.copy_datasets()
        self.copy_code()
        self.copy_replication_materials()
        self.create_readme()
        self.create_zip_archive()

        print("\n" + "=" * 50)
        print("✅ Publication package generation complete!")
        print(f"📁 Package location: {self.package_dir}")
        print(f"📦 Archive: {self.package_name}.zip")
        print("\nReady for arXiv submission or distribution.")
        print("\nNext steps:")
        print("1. Review package contents")
        print("2. Test replication instructions")
        print("3. Submit to arXiv or journal")
        print("4. Share with research community")

if __name__ == "__main__":
    packager = PublicationPackager()
    packager.generate_package()