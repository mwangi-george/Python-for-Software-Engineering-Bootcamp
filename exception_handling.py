sample_dict = {"a", 1}

try:
    # Some code that might cause an exception (error)
    print(sample_dict["b"])
except Exception as e:
    print(e)
