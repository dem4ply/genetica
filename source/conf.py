# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'genetica'
copyright = '2023, rafael barron'
author = 'rafael barron'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.githubpages',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig',
    #'sphinx.ext.mathbase',
    #'sphinxcontrib.jsmath',
    # 'sphinxcontrib.httpdomain',
    'sphinxcontrib.plantuml',
    'rst2pdf.pdfbuilder',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# inside conf.py
latex_engine = 'xelatex'
imgmath_latex_preamble=r'\usepackage{mhchem}'
imgmath_image_format='svg'
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',
    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '12pt',
    'fontpkg': r'''
\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
''',
    'preamble': r'''
\setlength\parindent{1zw}
\renewcommand{\baselinestretch}{0.8}

\usepackage[titles]{tocloft}
\usepackage[version=4]{mhchem}
\usepackage{siunitx}
\usepackage{chemfig}

\makeatletter
\renewcommand{\maketitle}{
\begin{center}
    {\Large \@title} \par
\end{center}
\begin{flushright}
    \@date \hspace{3zw} \@author \par
\end{flushright}
}

\@addtoreset{equation}{section} \def\theequation{\thesection.\arabic{equation}}

\makeatother

\pagestyle{plain}
\thispagestyle{plain}
''',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex',
}
latex_show_urls = 'footnote'

pdf_documents = [('index', u'rst2pdf', u'Sample rst2pdf doc', u'Your Name'),]
