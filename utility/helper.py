def trailing_slash(url):
	if url[-1] == "/":
		url = url[:-1]
	else:
		url = url

	return url