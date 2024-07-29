# check-yaml-in-asciidoc
This is a very limited script to show how a python script might run in our CI. This scripts determines updated files in a commit, checks the updated files for the presence of a YAML codeblock, then lints YAML against YAML best practices, for example, that certain fields, such as `metadata.name`, follow a set pattern, such as `example-<kind_vale>`. 

This could be run in the CI only when a writer comments, `merge-review-needed`, for example.

This script currently checks:
* metadata.name format
* public IP addresses
* if a YAML resource if found, reminds the writer to check for sensitive info
* Flags any MAC address as potentially sensitive

## Example output
```
['source-full.adoc']
Processing file: source-full.adoc

Checking ConfigMap resource...
Suggestion: metadata.name should be 'example-ConfigMap' instead of 'myconfigmap'
Public IP addresses found: 203.0.113.5. Suggestion: Replace public IP addresses with reserved documentation addresses from blocks: 192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24
You added the following YAML resource: ConfigMap. Ensure any resources you define in YAML do not inadvertently describe or name new or unreleased Red Hat, customer, or partner features or products.
MAC addresses found in ConfigMap: 4D::5E. Ensure these are appropriate for the context.
#####################################

Checking Pod resource...
Suggestion: metadata.name should be 'example-Pod' instead of 'dapi-env-test-pod'
Public IP addresses found: 198.51.100.1. Suggestion: Replace public IP addresses with reserved documentation addresses from blocks: 192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24
You added the following YAML resource: Pod. Ensure any resources you define in YAML do not inadvertently describe or name new or unreleased Red Hat, customer, or partner features or products.
MAC addresses found in Pod: EE::FF. Ensure these are appropriate for the context.
#####################################

```
