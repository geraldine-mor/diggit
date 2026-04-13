def excerpt_generator(content):
    excerpt_list = content.split()[:50]
    if (len(excerpt_list) >= 50):  
        excerpt = " ".join(excerpt_list)
        return excerpt + "..."
    else:
        return content

