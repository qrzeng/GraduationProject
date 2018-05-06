import codecs
import sys
import os

base_dir = 'tmp'
output_file_path = '.\\tmp\\test.utf8'
crfpp_test_path = '..\\libs\\crf_test'
model_path = '..\\model\\msr_model'
result_path = '..\\result\\msr_reuslt.utf8'
crfpp_commond = crfpp_test_path + ' -m '+ model_path + ' ' + output_file_path +' > '+result_path

# 输入暂存到文件中，通过文件来进行处理
def input_to_file(input):
	if not os.path.isdir(base_dir):
		os.mkdir(base_dir)
	output_file = codecs.open(output_file_path, 'w', 'utf-8')
	input = input.strip()
	for word in input:
		output_file.write(word + "\tB\n")
	output_file.close()

# 打印输出结果
def output_result(result_file):
	result_data = codecs.open(result_file, 'r', 'utf-8')
	for line in result_data.readlines():
		words = line.split()
		if not words:
			print('')
		elif words[2] == 'B' or words[2] == 'M':
			print(words[0], end='')
		elif words[2] == 'E' or words[2] == 'S':
			print(words[0]+'\t', end='')
	result_data.close()

if __name__ == '__main__':
	input_to_file('海运业雄踞全球之首，按吨位计占世界总数的１７％。')
	os.system(crfpp_commond)
	output_result(result_path)