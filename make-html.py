import os

TEMPLATE_TOP = """<!DOCTYPE html>
<html lang="uk">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
body {{
    background-color: #000000;
    color: #00ff00;
    font-family: "Courier New", monospace;
    font-size: 22px;
    margin: 40px;
}}

a {{
    color: #00ff00;
    text-decoration: none;
}}

a:hover {{
    background-color: #003300;
}}

.back {{
    display: block;
    margin-bottom: 30px;
}}

h2 {{
    border-bottom: 1px solid #00ff00;
    padding-bottom: 5px;
}}

.section {{
    margin-top: 30px;
}}

.site {{
    margin: 10px 0;
}}

.desc {{
    font-size: 18px;
    opacity: 0.8;
    margin-left: 40px;
}}

.desc::before {{
    content: "> ";
}}
</style>
</head>
<body>

<a class="back" href="index.html">← BACK TO TERMINAL</a>
"""

TEMPLATE_BOTTOM = """
</body>
</html>
"""


def generate_html(txt_file):
    html_file = txt_file.replace(".txt", ".html")

    with open(txt_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    html_content = TEMPLATE_TOP.format(
        title=html_file.replace(".html", "").upper()
    )

    for line in lines:
        line = line.strip()

        if not line:
            continue

        # === H2 ===
        if line.startswith("==="):
            text = line.replace("===", "").strip()
            html_content += f"\n<h2>=== {text} ===</h2>\n"

        # *** Section
        elif line.startswith("***"):
            section = line.replace("***", "").strip()
            html_content += f"""
<div class="section">
<h3>[ {section} ]</h3>
</div>
"""

        # Site line
        else:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) == 3:
                url, name, desc = parts
                html_content += f"""
<div class="site">
<a href="{url}" target="_blank">{name}</a>
<div class="desc">{desc}</div>
</div>
"""

    html_content += TEMPLATE_BOTTOM

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✓ Створено: {html_file}")


if __name__ == "__main__":
    for file in os.listdir():
        if file.endswith(".txt"):
            generate_html(file)