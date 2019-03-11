#!/usr/bin/env/ python

"""
This script uses the output from Sambamba to generate 
a report of a list of genes with coverage <100% at 30x 

Author: Natasha Pinto
Python version: 2.7 
Date created: 10/03/2019
"""
import sys
import pandas as pd
import argparse
import numpy


class Coverage(object):

	def __init__(self, input_file, output_file):
		self.input_file = input_file
		self.output_file = output_file 

#Load data from input file into pandas dataframe and assign column headers

	def read_file(self):
		self.data = pd.read_csv(self.input_file, sep="\t", comment='#', header=None)
		self.data.columns = ["chromosome", "start_pos", "end_pos", "full_pos",
		"NotUsed", "NotUsed", "GeneSys_Accession", "size", "read_count", "meanCoverage",
		"percentage30", "sampleName"]	
		self.data['GeneName'], self.data['Accession'] = self.data['GeneSys_Accession'].str.split(';', 1).str
	
#Use the percentage30 column to get rows with less than 100% coverage at 30x
		self.low_coverage = self.data.loc[self.data['percentage30'] <100]

#Pull through GeneNames with low coverage
		self.low_gene_list = self.low_coverage['GeneName']
		self.low_gene_list_nodup = self.low_gene_list.drop_duplicates()
		#print self.low_gene_list_nodup

#Convert dataframes into csv files; one file contains only gene names and the other contains more information about the partially covered exons
		self.low_gene_list_nodup.to_csv('gene_names.csv', sep='\t', index=False)
		self.low_coverage.to_csv('low_coverage_summary.csv', sep='\t', index=False)

#Allows script to be run from command line and specifies arguments
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Insert input file name and output file name")
	parser.add_argument('-i', action='store', dest='input_file', required='TRUE', help='Sambamba ouput file location')
	parser.add_argument('-o', action='store', dest='output_file', default = 'geneNames.pdf', help='Output file location')

	args = parser.parse_args()
	final_coverage = Coverage(args.input_file, args.output_file)
	final_coverage.read_file()










	




