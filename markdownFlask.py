# We import the markdown library
import markdown
import urllib.parse
from flask import Flask
from flask import render_template
from flask import Markup
import sys
from fileSelector import file_selector
from fileSelector import ls_md_files

app = Flask(__name__)


@app.route('/')
def index():
	dirname = './markdown-files/'
	files = ls_md_files(dirname)
	content = '<ul>'
	for a_file in files:
		content += "<li><a href=./{}>{}</a></li>\n".format(a_file, a_file)
	content += "</ul>"
	content = Markup(content)
	return render_template('index.html', content=content)


@app.route('/<filename>')
def anki(filename):
	dirname = './markdown-files/'
	filename = dirname + urllib.parse.unquote(filename)
	content = ''
	fi = open(filename, encoding='utf-8')
	line = fi.readline()
	while line:
		content += line
		line = fi.readline()
	fi.close()
	md = markdown.Markdown(extensions=['tables'])
	content = Markup(md.convert(content))
	return render_template('template_markdown.html', **locals())

if __name__ == "__main__":
	app.run()
