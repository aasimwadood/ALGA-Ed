# Adaptive Learning with Generative AI for Customized Educational Aids for Students with Disabilities

## Overview

This repository contains the code for implementing **Adaptive Learning with Generative AI** to create **Customized Educational Aids** for students with disabilities. The system leverages the power of Generative AI to adapt learning materials according to the specific needs of students with visual disabilities.

The goal of this project is to provide personalized educational aids, improving accessibility and learning outcomes for students who require customized content.

## Features

- **Adaptive Learning System**: Utilizes AI to adapt educational content based on the student's progress and learning style.
- **Generative AI Models**: Generate customized visual aids for students with visual impairments, including text-to-image and image-to-text features.
- **Personalized Educational Content**: The system generates and customizes educational content for students with disabilities, ensuring that it suits their specific learning needs.
- **User-Centric Design**: The interface and content delivery are designed to be intuitive and accessible for all users.

## Installation

### Prerequisites

Before using this code, ensure that the following are installed:

- Python 3.x
- PyTorch
- Transformers
- NumPy
- Matplotlib
- Other required libraries (listed in requirements.txt)

### Steps to Install

1. Clone the repository:

   ```bash
   git clone https://github.com/aasimwadood/adaptive-learning-generative-ai.git
   cd adaptive-learning-generative-ai  

2. Install dependencies:

   ```bash
   pip install -r requirements.txt  

3. Ensure that you have the necessary AI models downloaded (refer to the Model Documentation section for more details).

## Usage
1. **Train the AI Model**: To train the model on the provided dataset:

    ```bash
    python train_model.py --config config.yaml 
  
2. **Generate Customized Educational Aids**: Use the following command to generate educational content:

    ```bash
    python generate_aid.py --input "input_text_or_image" --output "output_path" 

3. **Evaluate the System**: To evaluate the performance of the model:

    ```bash
    python evaluate_model.py --input "test_data_path" 

## Code and Data Availability
The code and dataset for this project will be made publicly available after the publication of the associated research article. Please stay tuned for updates and the official release.

Once the article is published, you will be able to access the complete source code, pretrained models, and dataset through this repository.

## Model Documentation
The core AI model consists of a Generative Adversarial Network (GAN) that is trained on a dataset of educational materials tailored for students with visual disabilities. The model adapts content dynamically based on individual student needs, using a combination of text, images, and other multimedia elements.

## Model Architecture
**Generator**: Responsible for creating customized educational content.
**Discriminator**: Evaluates the authenticity of the generated content.
**Adaptive Learning Algorithm**: Adjusts content generation based on the student’s progress.
## Data
The dataset used to train the model includes various educational materials and visual aids. For privacy and ethical reasons, the dataset is anonymized and contains only publicly available educational resources. The data will be made available after the publication of the article.

## Contributing
We welcome contributions from the community. If you’d like to contribute, please fork this repository and submit a pull request with your proposed changes.

Please ensure that your changes adhere to the coding standards and include appropriate tests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any inquiries, feel free to contact us at:

Email: aasim.wadood@gmail.com
GitHub: https://github.com/aasimwadood/
