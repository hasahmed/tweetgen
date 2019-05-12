'''Utilities for storing objects on disk'''

# writes an object to disk in a binary format
def write_obj_to_disk(object, file_name):
    import pickle
    f = open(file_name, "wb")
    pickle.dump(object, f)
    f.close()

# reads an object from disk that has been written there using write_obj_to_disk
def read_obj_from_disk(file_name):
    import pickle
    f = open(file_name, "rb")
    obj = pickle.load(f)
    f.close()
    return obj


def decode_byte_string_array(byte_array):
    for i in range(0, len(byte_array)):
        byte_array[i] = byte_array[i].decode("utf-8")

