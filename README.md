# LossyTextCompressor
DLAI Project 23/24
## Overview
This project explores **lossy text compression** using deep learning-based models, focusing on the impact of **quantization** on text reconstruction. By leveraging **semantic embeddings** generated using the GTR-T5 Base model and compressing them at different quantization levels, we analyze the trade-off between storage efficiency and text quality.

## Features
- Uses **GTR-T5 Base** for embedding generation
- Implements **quantization** (2, 4, 6, 8, 10, 12, 14, 16 bits) for compression
- Reconstructs text using the **Vec2Text** model
- Evaluates reconstruction quality using:
  - **Cosine Similarity**
  - **BLEU Score**
  - **ROUGE-L Score**
- Determines the optimal quantization level for balancing accuracy and efficiency

## Results
Our findings indicate that **6–8 bit quantization** offers the best trade-off between **semantic integrity and compression efficiency**, while higher levels lead to significant text degradation.

## Future Work
- Experiment with hybrid quantization methods
- Fine-tune models for domain-specific text
- Explore lossy compression techniques beyond quantization



