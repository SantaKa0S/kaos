import sys
import json
import os
import re
from jsonschema import Draft7Validator

def generate_schema(markdown_file, output_file):
    # Leer el contenido del archivo Markdown
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Detectar propiedades del archivo Markdown
    properties = {}
    required = []

    # Función para normalizar nombres de propiedades
    def normalize_key(key):
        return re.sub(r'\W+', '_', key.lower()).strip('_')

    # Detectar encabezados como propiedades
    headers = re.findall(r'^(#+)\s+(.*)', content, re.MULTILINE)
    for header in headers:
        level, title = header
        key = normalize_key(title)
        properties[key] = {"type": "string"}
        required.append(key)

    # Detectar listas desordenadas
    unordered_lists = re.findall(r'^[-*+]\s+(.*)', content, re.MULTILINE)
    for i, item in enumerate(unordered_lists):
        key = f"unordered_list_item_{i+1}"
        properties[key] = {"type": "string"}
        required.append(key)

    # Detectar listas ordenadas
    ordered_lists = re.findall(r'^\d+\.\s+(.*)', content, re.MULTILINE)
    for i, item in enumerate(ordered_lists):
        key = f"ordered_list_item_{i+1}"
        properties[key] = {"type": "string"}
        required.append(key)

    # Detectar citas
    blockquotes = re.findall(r'^>\s+(.*)', content, re.MULTILINE)
    for i, quote in enumerate(blockquotes):
        key = f"blockquote_{i+1}"
        properties[key] = {"type": "string"}
        required.append(key)

    # Detectar código en bloque
    code_blocks = re.findall(r'```(.*?)```', content, re.DOTALL)
    for i, code in enumerate(code_blocks):
        key = f"code_block_{i+1}"
        properties[key] = {"type": "string"}
        required.append(key)

    # Detectar reglas horizontales
    horizontal_rules = re.findall(r'^\s*([-*_]){3,}\s*$', content, re.MULTILINE)
    for i, rule in enumerate(horizontal_rules):
        key = f"horizontal_rule_{i+1}"
        properties[key] = {"type": "string"}
        required.append(key)

    # Detectar enlaces
    links = re.findall(r'\[(.*?)\]\((.*?)\)', content)
    for i, link in enumerate(links):
        key = f"link_{i+1}"
        properties[key] = {
            "type": "object",
            "properties": {
                "text": {"type": "string"},
                "url": {"type": "string"}
            },
            "required": ["text", "url"]
        }
        required.append(key)

    # Detectar imágenes
    images = re.findall(r'!\[(.*?)\]\((.*?)\)', content)
    for i, image in enumerate(images):
        key = f"image_{i+1}"
        properties[key] = {
            "type": "object",
            "properties": {
                "alt_text": {"type": "string"},
                "url": {"type": "string"}
            },
            "required": ["alt_text", "url"]
        }
        required.append(key)

    # Crear el esquema JSON
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": os.path.basename(markdown_file),
        "type": "object",
        "properties": properties,
        "required": required
    }

    # Guardar el esquema en el archivo de salida
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(schema, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: generate_schema.py <input_markdown_file> <output_json_file>")
        sys.exit(1)

    input_markdown_file = sys.argv[1]
    output_json_file = sys.argv[2]

    generate_schema(input_markdown_file, output_json_file)
