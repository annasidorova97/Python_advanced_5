from decorator_logger_to_file_with_path import logger_to_file_with_path

nested_list = [
	'd',
	'f',
	['a', 'b', ['s', 'd'], 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


@logger_to_file_with_path(path='log_file.log')
def flat_generator(some_list):
	i = 0
	while i < len(some_list):
		if not isinstance(some_list[i], list):
			yield some_list[i]
			i += 1
		else:
			some_list = list(some_list[i]) + some_list[i+1:]
			i = 0


for item in flat_generator(nested_list):
	print(item)