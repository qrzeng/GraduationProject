import codecs
import sys

def character_split(input_file, output_file):
	input_data = codecs.open(input_file, 'r', 'utf-8')
	output_data = codecs.open(output_file, 'w', 'utf-8')
	for line in input_data.readlines():
		words = line.split()
		if not words:
			output_data.write('\n')
		elif words[2] == 'B' or words[2] == 'M':
			output_data.write(words[0])
		elif words[2] == 'E' or words[2] == 'S':
			output_data.write(words[0]+'\t')
	input_data.close()
	output_data.close()

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print("pls use: python make_crf_test_data.py input output")
		sys.exit()
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	character_split(input_file, output_file)