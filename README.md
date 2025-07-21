# Adaptive Learning with Generative AI for Customized Educational Aids for Students with Disabilities

## Overview

This repository implements **Adaptive Learning with Generative AI (ALGA-Ed)**, a novel educational framework tailored for students with disabilities. It integrates reinforcement learning, generative models (GPT, DALL·E, Whisper), and multimodal data inputs to deliver dynamically personalized and accessible educational content.

The goal is to improve learning outcomes, accessibility, and engagement through an AI-powered, inclusive learning environment.

## Key Features

- **Reinforcement Learning (RL) Module**: Dynamically adjusts content difficulty based on student engagement and performance.
- **Multimodal Generative AI**: Uses GPT for text, DALL·E for visual aids, and Whisper for audio synthesis.
- **User Profiling & Assistive Tech**: Supports eye-tracking, Braille, and haptic inputs for real-time user feedback.
- **Synthetic Data Simulation**: Simulates learning patterns for students with disabilities (e.g., ADHD, dyslexia, visual impairment).
- **Visual Engagement Analytics**: Generates visualizations of learning behavior segmented by disability type.
- **Streamlit UI (User-Centric Design)**: Intuitive interface to input learning materials and deliver customized aids.

## Installation

### Prerequisites

- Python 3.8+
- PyTorch
- Transformers
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Other dependencies in `requirements.txt`

### Steps to Install

```bash
git clone https://github.com/aasimwadood/ALGA-Ed.git
cd ALGA-Ed
pip install -r requirements.txt
```

## Usage

### 1. Train the AI Model

```bash
python train_model.py --config config.yaml
```

### 2. Generate Customized Educational Aids

```bash
python generate_aid.py --input "input_text_or_image" --output "output_path"
```

### 3. Evaluate the System

```bash
python evaluate_model.py --input "test_data_path"
```

### 4. Run the Streamlit UI

```bash
streamlit run interface_app.py
```

## Directory Structure

```
ALGA-Ed/
│
├── train_model.py              # Model training
├── generate_aid.py             # Generates AI-powered content
├── evaluate_model.py           # Evaluation logic
├── preprocess.py               # Preprocessing input data
├── models.py                   # Model definitions
├── data_loader/                # Dataset loaders for EdNet and ASSISTments
├── config.yaml                 # Training configuration
├── interface_app.py            # Streamlit UI
├── synthetic_data_generator.py # For simulating disabilities
├── requirements.txt
├── README.md
```

## Datasets

- **EdNet**: [https://github.com/riiid/ednet](https://github.com/riiid/ednet)
- **ASSISTments**: [https://www.assistments.org](https://www.assistments.org)
- **Synthetic Disability Data**: [https://github.com/aasimwadood/ALGA-Ed](https://github.com/aasimwadood/ALGA-Ed)

Datasets are anonymized and comply with GDPR and HIPAA standards.

## Evaluation Metrics

- Learning gain (pre-/post-test)
- Engagement rate
- Content adaptability ratio
- Accessibility usability score

## Contact

Email: aasim.wadood@gmail.com  
GitHub: [aasimwadood](https://github.com/aasimwadood)

## License

MIT License
