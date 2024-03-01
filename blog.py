import os
import markdown
from jinja2 import Template

markdown_dir = 'markdown_articles'
template_file = 'blog_template.html'

# Load the HTML template
with open(template_file, 'r') as file:
    template_html = file.read()

# Initialize Jinja2 template
template = Template(template_html)

# Read and convert Markdown files
# Read and convert Markdown files
markdown_files = [f for f in os.listdir(markdown_dir) if f.endswith('.md')]
markdown_content = []

for md_file in markdown_files:
    with open(os.path.join(markdown_dir, md_file), 'r') as file:
        md_content = file.read()
        html_content = markdown.markdown(md_content)
        markdown_content.append({'content': html_content})  # Store title and content

# Combine Markdown content with the HTML template
blog_html = template.render(articles=markdown_content)

# Save the generated blog
with open('generated_blog.html', 'w') as file:
    file.write(blog_html)

print("Blog generated successfully.")
