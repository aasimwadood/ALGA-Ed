
import torch
from transformers import pipeline

def generate_aid(input_text, output_path):
    generator = pipeline("text-generation", model="gpt2")
    output = generator(input_text, max_length=100)[0]["generated_text"]
    with open(output_path, "w") as f:
        f.write(output)
    print(f"Generated aid saved to {output_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()
    generate_aid(args.input, args.output)
