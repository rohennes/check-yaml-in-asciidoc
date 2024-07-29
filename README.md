# check-yaml-in-asciidoc
This is a very limited script to show how a python script might run in our CI. This would check updated content for the presence of a YAML codeblock, then lint the codeblock to validate for against YAML codeblock best practices, for example, that certain fields, such as `metadata.name`, follow a set pattern, such as `example-<kind_vale>`. 

This could be run in the CI only when a writer comments, `merge-review-needed`, for example.

This script currently runs the following validation checks on `source-full.adoc`:
* metadata.name format
* public IP addresses
* if a YAML resource if found, reminds the writer to check for sensitive info

## Example output
```
$ python check_asciidoc_yaml.py 

Checking metadata.name with best practices...
In the ConfigMap resource: Suggestion: metadata.name should be 'example-ConfigMap' instead of 'myconfigmap'

Checking for public IP addresses in YAML...
In the ConfigMap resource: Public IP addresses found: 203.0.113.5
Suggestion: Replace public IP addresses with reserved documentation addresses from blocks: 192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24

Checking if YAML resource added...
You added the following YAML resource: ConfigMap. Ensure any resources you define in YAML do not inadvertently describe or name new or unreleased Red Hat, customer, or partner features or products.

#####################################

Checking metadata.name with best practices...
In the Pod resource: Suggestion: metadata.name should be 'example-Pod' instead of 'dapi-env-test-pod'

Checking for public IP addresses in YAML...
In the Pod resource: Public IP addresses found: 198.51.100.1
Suggestion: Replace public IP addresses with reserved documentation addresses from blocks: 192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24

Checking if YAML resource added...
You added the following YAML resource: Pod. Ensure any resources you define in YAML do not inadvertently describe or name new or unreleased Red Hat, customer, or partner features or products.

#####################################
```
