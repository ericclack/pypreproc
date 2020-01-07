# pypreproc - Python website preprocessor

Really simple website preprocessor, enabling you to use includes on a static site. 

The preprocessor expects a single `src` directory, which it scans and then copies the contents 
to a `dest` directory, preprocessing any HTML files that it finds using the class in `tokenprocessor.py`.

For example...

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

...would replace the tokens `{% include inc/head.html %}` with the contents of those files. 

# Motivation

It was quicker to write this than find a good solution to the simple problem I had: how to host a site on a static server (AWS S3 in my case) and use includes to factor out common page elements. 
