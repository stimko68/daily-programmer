"""
HTML Markup Generator
Given an input string, automatically generate a working HTML webpage with
some predefined CSS templating.
"""
import time

paragraph = raw_input("Enter your paragraph: ")
output_webpage = ("""
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Auto-generated Webpage</title>
        <link href="auto.css" rel="stylesheet">
    </head>
    <body>
        <p>%s</p>
    </body>
</html>
""") % paragraph

css = """
html {
    font-family: sans-serif;
    -webkit-text-size-adjust: 100%;
        -ms-text-size-adjust: 100%;

body {
    margin: 0;
}

p {
    margin: 0 0 10px;
}
"""

with open(time.strftime('%m_%d_%Y_%H%M%S') + '_auto_generated_index.html', 'w+') as webpage:
    webpage.write(output_webpage)

with open('auto.css', 'w+') as c:
    c.write(css)