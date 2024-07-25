# check-yaml-in-asciidoc
This is a very limited script to show how a python script might run in our CI. This would check updated content for the presence of a YAML codeblock, then lint the codeblock to validate that certain fields, such as `metadata.name`, follow a set pattern, such as `example-<kind_vale>`. 

This could be run in the CI only when a writer comments, `merge-review-needed`, for example.

This script currently checks `source-starter.adoc`. A script could also be extended to flag IP addresses, web domains etc. for final review by the writer before merging. 

```
$ python check_metadata_name.py
Suggestion: metadata.name should be 'example-ConfigMap' instead of 'myconfigmap'
```
