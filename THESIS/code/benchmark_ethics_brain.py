#!/usr/bin/env python3
"""
Direct Brain Benchmark - No Server Required
Tests the unified brain v3.0 ethics reasoning directly
"""

import sys
import time
from pathlib import Path

# Add project root
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from domains.ethics.framework.meta_ethical_framework import EthicalDimension
from domains.ethics.temporal.temporal_moral_reasoner import UnifiedTemporalMoralReasoner


def benchmark_ethics_brain():
    """Benchmark the ethics brain directly"""
    print("🧠 Direct Ethics Brain Benchmark")
    print("=" * 40)

    # Initialize brain
    brain = UnifiedTemporalMoralReasoner()

    # Test scenarios
    scenarios = [
        {
            'action': 'implement_surveillance_system',
            'context': 'corporate_privacy_policy',
            'stakeholders': ['employees', 'customers', 'company']
        },
        {
            'action': 'launch_ai_product',
            'context': 'market_competition',
            'stakeholders': ['users', 'competitors', 'investors']
        },
        {
            'action': 'reduce_workforce',
            'context': 'economic_downturn',
            'stakeholders': ['employees', 'company', 'community']
        }
    ]

    horizons = ['immediate', 'short_term', 'medium_term']
    total_time = 0
    scenario_results = []

    for i, scenario in enumerate(scenarios, 1):
        print(f"\n📊 Scenario {i}: {scenario['action']}")

        # Extract context as string for the brain
        context_str = f"{scenario['action']} in {scenario['context']} context"
        ethical_state = {EthicalDimension.AUTONOMY: 0.5, 
                        EthicalDimension.BENEFICENCE: 0.5,
                        EthicalDimension.JUSTICE: 0.5,
                        EthicalDimension.TRANSPARENCY: 0.5}

        start_time = time.time()
        result = brain.cognitive_temporal_reasoning(ethical_state, context_str, horizons)
        elapsed = time.time() - start_time
        total_time += elapsed

        # Extract key metrics
        coherence = result.get('emotional_coherence', 0)
        efficiency = result.get('learning_efficiency', 0)
        confidence = result.get('moral_confidence', 0)

        print(".3f")
        print(".3f")
        print(".3f")
        print(".3f")

        scenario_results.append({
            'scenario': scenario['action'],
            'time': elapsed,
            'coherence': coherence,
            'efficiency': efficiency,
            'confidence': confidence
        })

    # Summary
    avg_time = total_time / len(scenarios)
    print("\n🎯 Benchmark Summary")
    print(f"   Average processing time: {avg_time:.3f}s")
    print(f"   Scenarios tested: {len(scenarios)}")
    print("   ✅ All scenarios processed successfully")
    print("\n💡 Perfect for benchmarking - no network latency!")
    return scenario_results

if __name__ == "__main__":
    results = benchmark_ethics_brain()