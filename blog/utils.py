def excerpt_generator(content):
    excerpt_list = content.split()[:30]
    if (len(excerpt_list) >= 30):  
        excerpt = " ".join(excerpt_list)
        return excerpt + "..."
    else:
        return content

