# pandoc-markdown-admonitions

Python script that handles the convertion of admonitions from Markdown to LaTeX

## Useful informations

1. You must know that this script converts Adinitions into LaTeX following Markdown Extended synthax (An admonition is thus marked with "!!!") and LaTeX package "tcolorbox". You'll need to include this package in your final tex file.
2. You'll need to define what color you want for each type of admonition. This script conversion set the uppercase admonition name as the frame color. You must define those colors in you final tex file. For exemple :
  ```tex
  \definecolor{NOTES}{cmyk}{0.80, 0.13, 0.14, 0.04, 1.00}
  ```
3. This script will produce anitermediary file that you can convert in full LaTeX with Pandoc
