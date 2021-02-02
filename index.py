from flask import Flask, redirect

# webapp
app = Flask(__name__)
app.url_map.strict_slashes = False

utility_pages = ['about', 'contact', 'press', 'terms', 'blog', 'pricing', 'aftermarket']

@app.route('/')
def redirect_main():
	return redirect('https://www.oneword.domains/')

@app.route('/<url>')
def redirect_pages(url):
	if url in utility_pages:
		return redirect('https://www.oneword.domains/'+url)
	else:
		return redirect('https://www.oneword.domains/available-'+url+'-domains')

@app.route('/a/<domain>')
def redirect_domains(domain):
    return redirect('https://www.oneword.domains/a/'+domain)