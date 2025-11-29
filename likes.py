def likes_msg(names: list[str]):
    """
    Construct a summary of the likes on a social media post using a list
    of names in string format. The proper template for the summary is
    dependent on the number of indices in the list.

    Return the summary message in string format.
    """
    match len(names):
        case 0:
            return "no one likes this"
        case 1:
            return f"{names[0]} likes this"
        case 2:
            return f"{names[0]} and {names[1]} like this"
        case 3:
            return f"{names[0]}, {names[1]} and {names[2]} like this"
    return f"{names[0]}, {names[1]} and {len(names[2:])} others like this"
