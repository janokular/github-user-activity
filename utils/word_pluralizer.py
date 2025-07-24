def pluralize(word: str, count: int):
    '''Pluralize word when count is more than 1'''
    return word if count == 1 else word + 's'
