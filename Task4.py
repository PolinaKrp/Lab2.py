import os
from typing import Optional


def get_next_element(class_mark: str) -> Optional[str]:
    """This function gradually returns us files of class"""
    path = os.path.join("dataset", class_mark)
    names_list = os.listdir(path)  
    names_list.append(None)
    my_generator = (item for item in names_list)
    for i in my_generator:
        yield i  