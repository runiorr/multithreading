import datetime
import threading

def func_info(original_func):
    def get_status(*args, **kwargs):
        result = original_func(*args, **kwargs)
        thread_id = threading.get_native_id()
        thread_name = threading.current_thread().getName()
        print(f'Function: {original_func.__name__}\nThread: {thread_name} of id {thread_id}')
        return result
    return get_status

def time_elapsed(original_func):
    def get_time(*args, **kwargs):
        start = datetime.datetime.now()
        result = original_func(*args, **kwargs)
        end = datetime.datetime.now()
        elapsed_time = (end-start).total_seconds()
        print(f'Time to run: {elapsed_time:.2f} seconds')
        return result
    return get_time

def type_check(*types):
    def check_accepts(function):
        assert len(types) == function.__code__.co_argcount,\
            "Number of typed inputs must match the function inputs"
        def new_function(*args, **kwargs):
            for (a, t) in zip(args, types):
                assert isinstance(a, t), \
                       "arg %r does not match %s" % (a,t)
            return function(*args, **kwargs)
        return new_function
    return check_accepts
