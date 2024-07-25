import re
import yaml

# Function to extract YAML from AsciiDoc
def extract_yaml_from_asciidoc(asciidoc_content):
    yaml_block = re.search(r'\[source,yaml\]\n----\n(.*?)\n----', asciidoc_content, re.DOTALL)
    if yaml_block:
        return yaml_block.group(1)
    return None

# Function to load YAML content
def load_yaml(yaml_content):
    return yaml.safe_load(yaml_content)

# Function to check metadata.name
def check_metadata_name(data):
    if 'kind' in data and 'metadata' in data and 'name' in data['metadata']:
        kind_value = data['kind']
        metadata_name = data['metadata']['name']
        expected_name = f"example-{kind_value}"
        if metadata_name != expected_name:
            print(f"Suggestion: metadata.name should be '{expected_name}' instead of '{metadata_name}'")
        else:
            print(f"metadata.name is correctly set to '{metadata_name}'")
    else:
        print("YAML structure is missing required fields.")

# Read AsciiDoc content from file
asciidoc_file_path = 'source-starter.adoc'
with open(asciidoc_file_path, 'r') as file:
    asciidoc_content = file.read()

yaml_content = extract_yaml_from_asciidoc(asciidoc_content)
if yaml_content:
    data = load_yaml(yaml_content)
    check_metadata_name(data)
else:
    print("YAML content not found in AsciiDoc.")
