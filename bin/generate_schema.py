import sys
import json
import os
from jsonschema import Draft7Validator

def generate_schema(markdown_file, output_file):
    # Aquí puedes definir cómo quieres generar el esquema a partir del archivo Markdown
    # Este es un ejemplo básico que crea un esquema vacío
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
    }

    with open(output_file, 'w') as f:
        json.dump(schema, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: generate_schema.py <input_markdown_file> <output_json_file>")
        sys.exit(1)

    input_markdown_file = sys.argv[1]
    output_json_file = sys.argv[2]

    generate_schema(input_markdown_file, output_json_file)
