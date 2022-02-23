def Urlify(sen,l):
    url = sen.replace(' ','%20')
    return url.strip('%20')
 
def urlify_py(text, length):
    return text[:length].replace(" ", "%20")

