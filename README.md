# pypreproc - Python website preprocessor

Really simple website preprocessor, enabling you to use includes on a static site. 

The preprocessor script expects a `src` directory, which it scans and then copies the contents 
to a `dest` directory, preprocessing any HTML files using the class in `tokenprocessor.py`. 
The source directory can contain any combination of files and directories you like. 

For example, a file containing these `{% include %}` tokens:

```
<!doctype html>
<html lang=en>
<head>
  <meta charset=utf-8>
  <title>Website title</title>
  {% include inc/head.html %}
</head>
<body id="home">
  <div id="content">
    <h1>Title</h1>
    <p>Content</p>
  </div>

  {% include inc/footer.html %}
</body>
</html>
```

...would result in those tokens being relpaced with the contents of the specified files. 

Here's the code for include:

```
    def include(self, file):
        with open(os.path.join(self.src_root, file)) as f:
            return f.read()
```


# Tokens

Take a look at the [`tokenprocessor.py`](blob/master/tokenprocessor.py) module to see the supported tags. 

# Motivation

It was quicker to write this than find a good solution to the simple problem I had: how to host a site on a static server (AWS S3 in my case) and use includes to factor out common page elements. 

# Requirements

* Python3
* `diff` command for validation -- but you could easily remove this bit if you don't want it. 
