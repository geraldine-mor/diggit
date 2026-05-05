"""Helper functions for diggit/blog"""


def excerpt_generator(content):
    """
    Creates a 30 word excerpt for display on preview post lists

    Args:
        content (string): content field of :model:`Post`

    Returns:
        string: first 30 words of longer posts appended with ... or
        content where the length is <30 words
    """
    excerpt_list = content.split()[:30]
    if (len(excerpt_list) >= 30):
        excerpt = " ".join(excerpt_list)
        return excerpt + "..."
    else:
        return content
