from datetime import datetime
from functools import wraps


def logger_to_file_with_path(path):
    def _logger_to_file_with_path(old_function):

        @wraps(old_function)
        def new_function(*args, **kwargs):

            time = datetime.now()
            with open(path, 'a', encoding='utf-8') as file:
                file.write(f'Function "{old_function.__name__}" was called {time}\n')
                file.write(f'with arguments: {args}, {kwargs}.\n')

            result = old_function(*args, **kwargs)

            with open(path, 'a', encoding='utf-8') as file:
                file.write(f'Was returned {result}.\n\n')

            return result

        return new_function

    return _logger_to_file_with_path
