import re
import yaml

# Function to extract YAML blocks from AsciiDoc
def extract_yaml_blocks_from_asciidoc(asciidoc_content):
    return re.findall(r'\[source,yaml\]\n----\n(.*?)\n----', asciidoc_content, re.DOTALL)

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
            print(f"In the {kind_value} resource: Suggestion: metadata.name should be '{expected_name}' instead of '{metadata_name}'")
        else:
            print(f"In the {kind_value} resource: metadata.name is correctly set to '{metadata_name}'")
    else:
        print("YAML structure is missing required fields.")

# Function to check for public IP addresses
def check_public_ip_addresses(yaml_content, kind_value):
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    private_ip_ranges = [
        re.compile(r'^10\.(?:[0-9]{1,3}\.){2}[0-9]{1,3}$'),
        re.compile(r'^172\.(?:1[6-9]|2[0-9]|3[0-1])\.(?:[0-9]{1,3}\.)[0-9]{1,3}$'),
        re.compile(r'^192\.168\.(?:[0-9]{1,3}\.)[0-9]{1,3}$')
    ]
    reserved_doc_ip_blocks = [
        '192.0.2.0/24',
        '198.51.100.0/24',
        '203.0.113.0/24'
    ]
    public_ips = []
    for ip in ip_pattern.findall(yaml_content):
        if not any(private_ip.match(ip) for private_ip in private_ip_ranges):
            public_ips.append(ip)
    
    if public_ips:
        print(f"In the {kind_value} resource: Public IP addresses found: {', '.join(public_ips)}")
        print(f"Suggestion: Replace public IP addresses with reserved documentation addresses from blocks: {', '.join(reserved_doc_ip_blocks)}")

# Function to provide a warning for sensitive data
def sensitive_data_warning_for_yaml(data):
    if 'kind' in data:
        kind_value = data['kind']
        print(f"You added the following YAML resource: {kind_value}. Ensure any resources you define in YAML do not inadvertently describe or name new or unreleased Red Hat, customer, or partner features or products.")

# Read AsciiDoc content from file
asciidoc_file_path = 'source-full.adoc'
with open(asciidoc_file_path, 'r') as file:
    asciidoc_content = file.read()

yaml_blocks = extract_yaml_blocks_from_asciidoc(asciidoc_content)
if yaml_blocks:
    for index, yaml_content in enumerate(yaml_blocks):
        try:
            data = load_yaml(yaml_content)
            print("")
            print("Checking metadata.name with best practices...")
            check_metadata_name(data)
            print("")
            print("Checking for public IP addresses in YAML...")
            check_public_ip_addresses(yaml_content, data.get('kind', f'code block {index + 1}'))
            print("")
            print("Checking if YAML resource added...")
            sensitive_data_warning_for_yaml(data)
            print("")
            print("#####################################")
        except yaml.YAMLError as e:
            print(f"Error parsing YAML content in code block {index + 1}: {e}")
else:
    print("No YAML content found in AsciiDoc.")
