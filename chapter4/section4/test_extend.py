import os
import jinja2

def render(tpl_path, **kwargs):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(**kwargs)


def test_extend():
    result = render('index.html')
    print(result)

if __name__ == '__main__':
    test_extend()
