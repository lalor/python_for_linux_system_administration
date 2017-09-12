import os
import jinja2

def render(tpl_path, **kwargs):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(**kwargs)

def test_simple():
    title = "Title  H   "
    items = [{'href':'a.com', 'caption':'ACaption'}, {'href':'b.com', 'caption':'Bcaption'}]
    content="This is content"
    result = render('simple.html', **locals())
    print(result)

if __name__ == '__main__':
    test_simple()
