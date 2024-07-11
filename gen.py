import os
import markdown

for art in os.listdir("articles/math"):
    path = os.path.join("articles/math", art)
    html_path = os.path.join("public/math/", os.path.splitext(art)[0] + ".html")

    with open(path, "r") as file:
        content = file.read()
        article_html = markdown.markdown(content, extensions=["mdx_math"], extension_configs={"mdx_math": {"enable_dollar_delimiter": True}})

    with open("public/math/article.html", "r") as file:
        template_html = file.read()

    corpus_marker = r"[[CORPUS]]"

    parts = template_html.split(corpus_marker)

    if len(parts) != 2:
        raise ValueError(f"Corpus marker '{corpus_marker}' not found in template HTML.")

    new_html_content = parts[0] + article_html + parts[1]

    with open(html_path, "w") as file:
        file.write(new_html_content)
