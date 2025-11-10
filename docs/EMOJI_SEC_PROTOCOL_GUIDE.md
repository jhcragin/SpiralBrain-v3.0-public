# Emoji & SEC Protocol Guide

**SpiralCortex v2.0 - Symbolic-Emotional Calibration System**  
*Last Updated: October 27, 2025*

---

## Table of Contents

1. [What is SEC?](#what-is-sec)
2. [How Emojis Work](#how-emojis-work)
3. [SEC Vector Structure](#sec-vector-structure)
4. [The SEC Protocol](#the-sec-protocol)
5. [Unicode Handling](#unicode-handling)
6. [Practical Usage](#practical-usage)
7. [Training & Evolution](#training--evolution)
8. [Troubleshooting](#troubleshooting)

---

## What is SEC?

**SEC = Symbolic-Emotional Calibration**

SEC is SpiralCortex's system for translating emotional symbols (emojis) into **multi-dimensional emotion vectors** that modulate cognitive pathways. Instead of treating emojis as simple icons, SEC interprets them as rich emotional signals that influence how the system processes information.

### Core Concept

```
😊 → SEC Vector → Pathway Modulation → Cognitive Processing
```

**Example:**
```python
😊 (happy face) → {
    valence: +0.8,        # Positive emotion
    arousal: +0.6,        # Moderately excited
    hazard_sensitivity: 0.2,  # Low threat perception
    elasticity: 0.7,      # Flexible thinking
    torque: 0.5           # Moderate dynamism
} → Activates positive pathways → Optimistic reasoning
```

### Why It Matters

Traditional AI treats emotions as labels (happy/sad/angry). SEC treats them as **continuous multidimensional states** that:

- **Modulate attention** (what you focus on)
- **Adjust risk assessment** (how careful you are)
- **Change flexibility** (how creative vs. rigid)
- **Influence decision-making** (optimistic vs. pessimistic)

---

## How Emojis Work

### Emoji as Emotional Shorthand

In SpiralCortex, emojis serve as **compact emotional instructions** to the cognitive system:

```python
"Calculate my crypto taxes 😰"  # Anxiety → cautious, careful processing
"Calculate my crypto taxes 😎"  # Confidence → efficient, streamlined processing
```

Same task, different emotional context → different cognitive strategies.

### The Flow

1. **Input Text + Emoji**
   ```python
   user_input = "I need to handle this deadline 😰"
   ```

2. **Emoji Extraction**
   ```python
   # System extracts: 😰
   ```

3. **SEC Lookup**
   ```python
   sec_vector = sec_manager.get_sec_vector("😰")
   # Returns: valence=-0.6, arousal=0.7, hazard=0.8, elasticity=0.3
   ```

4. **Pathway Modulation**
   ```python
   # High hazard → Activate caution pathways
   # Low elasticity → Reduce creative options
   # High arousal → Increase attention
   ```

5. **Contextualized Processing**
   ```python
   # System processes deadline with heightened caution
   # Suggests conservative, well-tested approaches
   # Avoids risky optimizations
   ```

---

## SEC Vector Structure

### The 8 Dimensions

Every emoji maps to a **SECVector** with 8 dimensions:

```python
@dataclass
class SECVector:
    valence: float              # -1.0 to 1.0
    arousal: float              # 0.0 to 1.0
    hazard_sensitivity: float   # 0.0 to 1.0
    elasticity: float           # 0.0 to 1.0
    torque: float               # 0.0 to 1.0
    alpha_rhythm: float         # 0.0 to 1.0
    beta_rhythm: float          # 0.0 to 1.0
    attention_entropy: float    # 0.0 to 1.0
```

### Dimension Explanations

#### 1. Valence (-1.0 to 1.0)
**What:** Emotional positivity/negativity  
**Range:** -1.0 (very negative) → 0.0 (neutral) → +1.0 (very positive)

**Examples:**
- 😊 Happy: +0.8 (positive)
- 😢 Sad: -0.7 (negative)
- 😐 Neutral: 0.0 (neutral)

**Effect:** Positive valence → optimistic reasoning, negative → cautious/conservative

#### 2. Arousal (0.0 to 1.0)
**What:** Emotional intensity/energy  
**Range:** 0.0 (calm/relaxed) → 1.0 (excited/intense)

**Examples:**
- 😴 Tired: 0.2 (low arousal)
- 😊 Happy: 0.6 (moderate arousal)
- 😠 Angry: 0.9 (high arousal)

**Effect:** High arousal → faster processing, higher attention; Low → relaxed, contemplative

#### 3. Hazard Sensitivity (0.0 to 1.0)
**What:** Threat awareness/caution level  
**Range:** 0.0 (safe/trusting) → 1.0 (danger-aware/cautious)

**Examples:**
- ❤️ Love: 0.2 (low hazard)
- 😰 Anxious: 0.8 (high hazard)
- 😨 Fearful: 0.9 (very high hazard)

**Effect:** High hazard → activate safety checks, conservative strategies, risk avoidance

#### 4. Elasticity (0.0 to 1.0)
**What:** Cognitive flexibility  
**Range:** 0.0 (rigid/fixed) → 1.0 (flexible/adaptive)

**Examples:**
- 😠 Angry: 0.3 (rigid)
- 🤔 Thoughtful: 0.9 (flexible)
- ❤️ Love: 0.8 (flexible)

**Effect:** High elasticity → creative solutions, adaptability; Low → stick to rules, procedures

#### 5. Torque (0.0 to 1.0)
**What:** Dynamic change potential  
**Range:** 0.0 (stable/steady) → 1.0 (dynamic/volatile)

**Examples:**
- 😐 Neutral: 0.3 (stable)
- 😠 Angry: 0.8 (dynamic)
- 😅 Nervous laugh: 0.6 (moderate)

**Effect:** High torque → rapid state changes, volatility; Low → consistent, predictable processing

#### 6. Alpha Rhythm (0.0 to 1.0)
**What:** Neural relaxation/calm processing  
**Range:** 0.0 (minimal) → 1.0 (maximal)

**Examples:**
- 😌 Relieved: 0.8 (high alpha)
- 😰 Anxious: 0.2 (low alpha)

**Effect:** High alpha → relaxed attention, big-picture thinking; Low → focused, detail-oriented

#### 7. Beta Rhythm (0.0 to 1.0)
**What:** Active cognitive engagement  
**Range:** 0.0 (minimal) → 1.0 (maximal)

**Examples:**
- 🎯 Focused: 0.9 (high beta)
- 😴 Tired: 0.2 (low beta)

**Effect:** High beta → analytical thinking, problem-solving; Low → passive processing

#### 8. Attention Entropy (0.0 to 1.0)
**What:** Focus vs. creativity balance  
**Range:** 0.0 (narrow focus) → 1.0 (broad/creative)

**Examples:**
- 🎯 Target: 0.2 (narrow focus)
- 🤔 Thinking: 0.8 (broad exploration)

**Effect:** Low entropy → tunnel vision, precision; High → divergent thinking, creativity

---

## The SEC Protocol

### What is the SEC Protocol?

The SEC Protocol is a **versioned, continuously-learning database** of emoji→SEC vector mappings.

**Location:** `nexus/emotional/emotional_intelligence.py`

### Core Components

#### 1. SECProtocolManager

The manager handles all emoji-emotion mappings:

```python
from nexus.emotional.emotional_intelligence import SECProtocolManager

# Initialize manager
sec_manager = SECProtocolManager(protocol_file="sec_protocol_v1.0.json")

# Get vector for emoji
vector = sec_manager.get_sec_vector("😊")
print(f"Valence: {vector.valence}, Arousal: {vector.arousal}")

# Update mapping (continuous learning)
sec_manager.update_emoji_vector(
    emoji="😊",
    new_vector=SECVector(
        valence=0.85,
        arousal=0.65,
        hazard_sensitivity=0.15,
        elasticity=0.75,
        torque=0.5
    ),
    reason="improved_training_data",
    confidence=0.9
)
```

#### 2. Versioning System

Every update creates a new version:

```python
# Current version
version = sec_manager.get_current_version()  # "1.0"

# After update
sec_manager.update_emoji_vector(...)
new_version = sec_manager.get_current_version()  # "1.1"

# Rollback if needed
sec_manager.rollback_to_version("1.0")
```

**Version History:**
```json
{
  "version_history": ["1.0", "1.1", "1.2", "1.3"],
  "entries": {
    "😊": {
      "version": "1.3",
      "last_updated": "2025-10-27T14:30:00",
      "update_reason": "goemotions_training",
      "confidence": 0.92
    }
  }
}
```

#### 3. Emoji Blending

Combine multiple emojis into a composite emotional state:

```python
# Multiple emojis in input
blended_vector = sec_manager.blend_emojis(["😊", "😰", "💪"])

# Result: weighted average of all three
# Example: cautious optimism with determination
```

### Default Mappings

The protocol comes with default mappings for common emojis:

| Emoji | Valence | Arousal | Hazard | Elasticity | Meaning |
|-------|---------|---------|--------|------------|---------|
| 😊 | +0.8 | 0.6 | 0.2 | 0.7 | General happiness |
| 😢 | -0.7 | 0.3 | 0.4 | 0.3 | Sadness |
| 😠 | -0.8 | 0.8 | 0.7 | 0.4 | Anger |
| 😨 | -0.9 | 0.7 | 0.9 | 0.2 | Fear |
| ❤️ | +0.9 | 0.5 | 0.3 | 0.8 | Love |
| 😮 | +0.1 | 0.8 | 0.5 | 0.9 | Surprise |
| 😐 | 0.0 | 0.2 | 0.5 | 0.5 | Neutral |
| 🤔 | +0.2 | 0.4 | 0.4 | 0.9 | Contemplation |

### Protocol Evolution

The SEC protocol **continuously learns** from multiple sources:

#### From Training Data

```python
# Load emotion datasets
updated_count = sec_manager.load_from_goemotions(split="train[:5%]")
print(f"Updated {updated_count} emoji mappings from GoEmotions")

# Other sources
sec_manager.load_from_emotag()  # Context-based emoji usage
sec_manager.load_from_meld()    # Multimodal emotion data
sec_manager.load_from_xed()     # Cross-cultural emotions
```

#### From Usage Patterns

```python
# System learns from actual usage
for transaction in user_transactions:
    emoji = extract_emoji(transaction.text)
    outcome = analyze_outcome(transaction)
    
    if outcome.successful:
        # Reinforce current mapping
        sec_manager.update_emoji_vector(
            emoji,
            current_vector,
            reason=f"successful_use_in_{transaction.context}",
            confidence=0.8
        )
```

---

## Unicode Handling

### The Unicode Problem

Emojis are Unicode characters, and Python/Windows can have encoding issues:

**Common Errors:**
```python
UnicodeEncodeError: 'charmap' codec can't encode character '\U0001f60a'
UnicodeDecodeError: 'ascii' codec can't decode byte 0xf0 in position 0
```

### Solution 1: File Encoding

**Always use UTF-8 encoding** when reading/writing files with emojis:

```python
# ✅ CORRECT
with open("data.json", "w", encoding="utf-8") as f:
    json.dump({"emoji": "😊", "mood": "happy"}, f, ensure_ascii=False)

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# ❌ WRONG (will crash on Windows)
with open("data.json", "w") as f:  # Uses system default encoding
    json.dump({"emoji": "😊"}, f)
```

### Solution 2: Console Output (Windows)

Windows PowerShell/CMD need special configuration:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# Windows UTF-8 support for emoji output
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

# Now safe to print emojis
print("Processing emotional state: 😊")
```

**Alternative: PowerShell Configuration**
```powershell
# Set console to UTF-8
$OutputEncoding = [console]::InputEncoding = [console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
```

### Solution 3: JSON with Emojis

```python
import json

# ✅ CORRECT: ensure_ascii=False preserves emojis
data = {"protocol": {"😊": {"valence": 0.8}}}
with open("sec_protocol.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Result in file:
# {
#   "protocol": {
#     "😊": {"valence": 0.8}
#   }
# }

# ❌ WRONG: ensure_ascii=True (default) converts to escape codes
json.dump(data, f, indent=2)  # Creates: "\ud83d\ude0a" instead of "😊"
```

### Solution 4: String Literals

```python
# ✅ CORRECT: Direct emoji in strings
emoji = "😊"
message = f"User mood: {emoji}"

# ✅ CORRECT: Unicode escape sequences
emoji = "\U0001f60a"  # Same as 😊
emoji = "\N{SMILING FACE WITH SMILING EYES}"  # Named Unicode

# ❌ WRONG: Trying to encode/decode unnecessarily
emoji = "😊".encode("utf-8").decode("ascii")  # Will crash!
```

### Solution 5: Regex with Emojis

Extract emojis from text:

```python
import re

def extract_emojis(text: str) -> list[str]:
    """Extract all emojis from text using Unicode ranges."""
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # Emoticons
        "\U0001F300-\U0001F5FF"  # Symbols & Pictographs
        "\U0001F680-\U0001F6FF"  # Transport & Map
        "\U0001F1E0-\U0001F1FF"  # Flags
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0001F251"  # Enclosed characters
        "]+",
        flags=re.UNICODE
    )
    return emoji_pattern.findall(text)

# Usage
text = "I'm so happy 😊 about this! 🎉"
emojis = extract_emojis(text)
print(emojis)  # ['😊', '🎉']
```

### Best Practices Checklist

✅ **Always specify `encoding="utf-8"` when opening files**  
✅ **Use `ensure_ascii=False` in `json.dump()` for emoji preservation**  
✅ **Add UTF-8 header to Python files: `# -*- coding: utf-8 -*-`**  
✅ **Reconfigure stdout/stderr on Windows with `sys.stdout.reconfigure(encoding="utf-8")`**  
✅ **Use raw Unicode strings or direct emoji literals, not byte sequences**  
✅ **Test emoji handling on Windows (most restrictive)**  

❌ **Don't rely on system default encoding**  
❌ **Don't use `open()` without `encoding=` parameter**  
❌ **Don't use `str.encode()`/`str.decode()` unless necessary**  
❌ **Don't assume ASCII compatibility**  

---

## Practical Usage

### Basic Emoji Processing

```python
from nexus.emotional.emotional_intelligence import SECProtocolManager, SECVector

# Initialize
sec_manager = SECProtocolManager()

# Process user input
user_input = "I need help with my taxes 😰"

# Extract emoji (simplified)
import re
emojis = re.findall(r'[\U0001F600-\U0001F64F]', user_input)

if emojis:
    # Get SEC vector
    sec_vector = sec_manager.get_sec_vector(emojis[0])
    
    print(f"Detected emotion: {emojis[0]}")
    print(f"Valence: {sec_vector.valence:.2f}")
    print(f"Arousal: {sec_vector.arousal:.2f}")
    print(f"Hazard sensitivity: {sec_vector.hazard_sensitivity:.2f}")
    
    # Adapt processing based on emotion
    if sec_vector.hazard_sensitivity > 0.7:
        print("→ Activating cautious processing mode")
        # Use conservative, careful algorithms
    
    if sec_vector.valence < 0:
        print("→ Providing extra reassurance")
        # Add supportive messaging
```

### Pathway Modulation

```python
def modulate_pathways(sec_vector: SECVector) -> dict:
    """Adjust cognitive pathway weights based on emotion."""
    
    pathways = {
        "attention": 0.5,
        "caution": 0.5,
        "creativity": 0.5,
        "speed": 0.5
    }
    
    # High arousal → more attention, faster processing
    pathways["attention"] += sec_vector.arousal * 0.4
    pathways["speed"] += sec_vector.arousal * 0.3
    
    # High hazard → more caution, less speed
    pathways["caution"] += sec_vector.hazard_sensitivity * 0.5
    pathways["speed"] -= sec_vector.hazard_sensitivity * 0.3
    
    # High elasticity → more creativity
    pathways["creativity"] += sec_vector.elasticity * 0.4
    
    # Normalize to [0, 1]
    for key in pathways:
        pathways[key] = max(0.0, min(1.0, pathways[key]))
    
    return pathways

# Usage
sec_vector = sec_manager.get_sec_vector("😰")  # Anxiety
pathways = modulate_pathways(sec_vector)

print(f"Attention: {pathways['attention']:.2f}")
print(f"Caution: {pathways['caution']:.2f}")
print(f"Creativity: {pathways['creativity']:.2f}")
print(f"Speed: {pathways['speed']:.2f}")
```

### Multi-Emoji Blending

```python
# User sends multiple emojis
user_input = "Excited but nervous about the deadline! 😊😰🎯"

# Extract all emojis
emojis = ["😊", "😰", "🎯"]

# Blend into composite state
composite_vector = sec_manager.blend_emojis(emojis)

print("Composite emotional state:")
print(f"  Valence: {composite_vector.valence:.2f}")
print(f"  Arousal: {composite_vector.arousal:.2f}")
print(f"  Hazard: {composite_vector.hazard_sensitivity:.2f}")

# Result: Mixed positive/negative valence, high arousal, moderate hazard
# Interpretation: "Excited but cautious optimism with focused determination"
```

### Creating Custom SEC Vectors

```python
# Define custom emotional state
custom_vector = SECVector(
    valence=0.3,           # Mildly positive
    arousal=0.4,           # Calm
    hazard_sensitivity=0.2,  # Low threat
    elasticity=0.8,        # Highly flexible
    torque=0.3,            # Stable
    alpha_rhythm=0.7,      # Relaxed
    beta_rhythm=0.5,       # Moderate engagement
    attention_entropy=0.6  # Somewhat broad focus
)

# Register custom emoji
sec_manager.update_emoji_vector(
    emoji="🧘",  # Meditation emoji
    new_vector=custom_vector,
    reason="custom_relaxation_state",
    confidence=1.0
)
```

---

## Training & Evolution

### Loading Training Data

The SEC protocol can be updated from multiple emotion datasets:

#### 1. GoEmotions (Google Research)

```python
# Load GoEmotions dataset
updated_count = sec_manager.load_from_goemotions(split="train[:5%]")
print(f"Updated {updated_count} emoji mappings from GoEmotions")

# How it works:
# - Extracts emojis from text
# - Maps to emotion labels (joy, sadness, anger, fear, surprise, love, etc.)
# - Converts emotions to SEC vectors using Plutchik's wheel
# - Updates protocol with weighted averages
```

#### 2. EmoTag (Context-based)

```python
# Load context-based emoji usage
updated_count = sec_manager.load_from_emotag(split="train[:5%]")

# How it works:
# - Analyzes emoji usage in various contexts
# - Learns emotional associations from co-occurrence
# - Updates SEC vectors based on contextual patterns
```

#### 3. MELD (Multimodal Emotion)

```python
# Load multimodal emotion data
updated_count = sec_manager.load_from_meld(split="train[:1%]")

# How it works:
# - Processes text, audio, and visual emotion data
# - Extracts emojis and their multimodal contexts
# - Creates richer SEC mappings from cross-modal signals
```

#### 4. XED (Cross-cultural Emotions)

```python
# Load cross-cultural emotion expressions
updated_count = sec_manager.load_from_xed(language="en", split="train[:1%]")

# How it works:
# - Learns emoji meanings across different cultures
# - Adjusts SEC vectors for cultural variations
# - Improves generalization across demographics
```

### Continuous Learning Loop

```python
from nexus.core.unified_training_system import ContinuousLearningTrainer

# Initialize continuous learning
trainer = ContinuousLearningTrainer(sec_manager=sec_manager)

# Train continuously from streaming data
for batch in data_stream:
    # 1. Process batch
    predictions = trainer.process_batch(batch)
    
    # 2. Compute loss
    loss = trainer.compute_loss(predictions, batch['labels'])
    
    # 3. Update model
    trainer.update(loss)
    
    # 4. Every 500 steps: validate and evolve SEC protocol
    if trainer.step % 500 == 0:
        validation_accuracy = trainer.validate()
        
        if validation_accuracy > trainer.best_accuracy:
            # Performance improved → update SEC protocol
            trainer.evolve_sec_protocol()
            print(f"SEC protocol evolved to v{sec_manager.get_current_version()}")
```

### Protocol Evolution Strategy

The SEC protocol evolves through:

1. **Confidence-weighted blending:**
   ```python
   # New vector doesn't replace old one completely
   # Instead: blend based on confidence
   blended = old_vector.blend(new_vector, confidence=0.8)
   # 20% old, 80% new if confidence=0.8
   ```

2. **Usage tracking:**
   ```python
   # Track which emojis are used most
   stats = sec_manager.get_protocol_stats()
   print(f"Most used emoji: {stats['most_used_emoji']}")
   print(f"Usage count: {stats['max_usage']}")
   ```

3. **Version control:**
   ```python
   # Every update creates new version
   # Can rollback if performance degrades
   if validation_accuracy < previous_best:
       sec_manager.rollback_to_version(previous_version)
   ```

---

## Troubleshooting

### Problem 1: UnicodeEncodeError on Windows

**Error:**
```
UnicodeEncodeError: 'charmap' codec can't encode character '\U0001f60a' in position 5
```

**Solution:**
```python
# Add at top of script
import sys
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
```

### Problem 2: Emoji Shows as ��� or ?

**Cause:** Terminal/console doesn't support Unicode

**Solution (PowerShell):**
```powershell
# Change console font to one with emoji support
# Settings → Appearance → Font → "Cascadia Code" or "Segoe UI Emoji"

# Or set encoding
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
```

**Solution (Python script):**
```python
# Fallback to ASCII representation
def safe_print_emoji(emoji: str):
    try:
        print(emoji)
    except UnicodeEncodeError:
        # Fallback to hex representation
        print(f"[Emoji: U+{ord(emoji):04X}]")
```

### Problem 3: JSON File Shows Escape Codes

**Problem:** File contains `\ud83d\ude0a` instead of 😊

**Cause:** `ensure_ascii=True` (default) in json.dump()

**Solution:**
```python
# Change this:
json.dump(data, f)

# To this:
json.dump(data, f, ensure_ascii=False, indent=2)
```

### Problem 4: SEC Vector Not Found

**Error:** `get_sec_vector("🤷") returns None`

**Cause:** Emoji not in protocol

**Solution:**
```python
# Check if emoji exists
vector = sec_manager.get_sec_vector("🤷")
if vector is None:
    # Add default or learn from context
    default_vector = SECVector(
        valence=0.0,
        arousal=0.5,
        hazard_sensitivity=0.5,
        elasticity=0.7,
        torque=0.5
    )
    sec_manager.update_emoji_vector("🤷", default_vector, reason="fallback")
    vector = default_vector
```

### Problem 5: Protocol File Corrupted

**Error:** `json.JSONDecodeError: Expecting property name`

**Solution:**
```python
# Reinitialize with default protocol
import os

# Backup corrupted file
os.rename("sec_protocol_v1.0.json", "sec_protocol_v1.0.json.backup")

# Create fresh protocol
sec_manager = SECProtocolManager()  # Automatically creates default
```

### Problem 6: Regex Not Matching Emojis

**Problem:** `re.findall()` misses some emojis

**Cause:** Incomplete Unicode range

**Solution:**
```python
import re

# Comprehensive emoji regex
emoji_pattern = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # Emoticons
    "\U0001F300-\U0001F5FF"  # Symbols & Pictographs
    "\U0001F680-\U0001F6FF"  # Transport & Map Symbols
    "\U0001F1E0-\U0001F1FF"  # Flags (iOS)
    "\U00002702-\U000027B0"  # Dingbats
    "\U000024C2-\U0001F251"  # Enclosed characters
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols
    "\U0001FA00-\U0001FA6F"  # Extended symbols
    "]+",
    flags=re.UNICODE
)

emojis = emoji_pattern.findall(text)
```

---

## Summary

### Key Concepts

✅ **SEC = Symbolic-Emotional Calibration**: Multi-dimensional emotion vectors  
✅ **8 Dimensions**: Valence, arousal, hazard, elasticity, torque, alpha/beta rhythms, attention entropy  
✅ **Protocol**: Versioned database of emoji→SEC mappings  
✅ **Evolution**: Continuously learns from training data and usage  
✅ **Unicode**: Always use UTF-8 encoding and `ensure_ascii=False`  

### Quick Reference

```python
# Initialize
from nexus.emotional.emotional_intelligence import SECProtocolManager
sec_manager = SECProtocolManager()

# Get vector
vector = sec_manager.get_sec_vector("😊")

# Update vector
sec_manager.update_emoji_vector(emoji, new_vector, reason, confidence)

# Blend emojis
composite = sec_manager.blend_emojis(["😊", "😰"])

# Load training data
sec_manager.load_from_goemotions(split="train[:5%]")

# Rollback if needed
sec_manager.rollback_to_version("1.0")

# UTF-8 handling (Windows)
import sys
sys.stdout.reconfigure(encoding="utf-8")

# File operations
with open("file.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

### Files to Review

- `nexus/emotional/emotional_intelligence.py` - Main SEC implementation
- `nexus/core/unified_training_system.py` - Continuous learning
- `nexus/utils/update_emoji_protocol.py` - Protocol update utility
- `docs/CONTINUOUS_LEARNING_ARCHITECTURE.md` - Training system details

---

## Next Steps

1. **Experiment with different emojis** in your inputs
2. **Monitor SEC evolution** during training
3. **Create custom emotional states** for domain-specific needs
4. **Track usage patterns** to understand emotion distribution
5. **Blend emojis** to express complex emotional states

The SEC system makes SpiralCortex emotionally intelligent, allowing it to adapt its cognitive processing to the emotional context of each task. Master emoji usage, and you master emotional modulation of AI reasoning.
