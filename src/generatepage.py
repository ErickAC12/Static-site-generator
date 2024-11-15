from markdowntohtmlnode import markdown_to_html_node
from extracttitle import extract_title
import os


def generate_page_recursively(dir_path_content, template_path, dest_dir_path):
    def generate_page(from_path, template_path, dest_path):
        print(f"Generating page from {from_path} to {dest_path} using {template_path}")

        with open(from_path, 'r') as file:
            markdown_content = file.read()

        with open(template_path, 'r') as file:
            template_content = file.read()

        html_content = markdown_to_html_node(markdown_content).to_html()

        title = extract_title(markdown_content)

        filled_template = template_content.replace('{{ Title }}', title).replace('{{ Content }}', html_content)

        dest_dir = os.path.dirname(dest_path)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        with open(dest_path, 'w') as file:
            file.write(filled_template)

    def crawl_directory(current_dir, current_dest_dir):
        for entry in os.listdir(current_dir):
            entry_path = os.path.join(current_dir, entry)
            entry_dest_path = os.path.join(current_dest_dir, entry)

            if os.path.isdir(entry_path):
                crawl_directory(entry_path, entry_dest_path)
            elif entry_path.endswith('.md'):
                html_dest_path = entry_dest_path[:-3] + '.html'
                generate_page(entry_path, template_path, html_dest_path)

    crawl_directory(dir_path_content, dest_dir_path)
