# We import the markdown library
import markdown
from flask import Flask
from flask import render_template
from flask import Markup
import sys
from fileSelector import file_selector

app = Flask(__name__)


@app.route('/')
def index():
	dirname = './markdown-files/'
	filename = file_selector(dirname)
	content = ''
	fi = open(filename, encoding='utf-8')
	line = fi.readline()
	while line:
		content += line
		line = fi.readline()
	fi.close()
	md = markdown.Markdown(extensions=['markdown.extensions.tables'])
	content = Markup(md.convert(content))
	return render_template('template_markdown.html', **locals())
	'''
	md_file_list = ls_md_files('./markdown-files/')
	links = ''
	for i in range(0, md_file_list):
		link = '<a href="./{}">{}</a>'.format(i, i)
		links = links + link
	return render_template('index.html', **locals())
	'''

@app.route('/<filename>')
def anki(filename):
	dirname = './markdown-files/'
	filename = dirname + filename
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
