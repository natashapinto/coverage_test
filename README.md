# coverage_test
Python script takes in output from Sambamba and returns a report with a list of genes with &lt;100% coverage at 30x

Usage 
> python coverage.py -i [input_file]

The script creates two csv files 

1. gene_names.csv = Contains a list of genes with less than 100% coverage at 30x
2. low_coverage_summary.csv = Coverage summary for the exons in the genes in gene_names.csv





