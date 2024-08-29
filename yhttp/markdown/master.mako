<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <link rel="stylesheet" href="/index.css" >
  <script>
    if (document.documentMode || /Edge/.test(navigator.userAgent)) {
        alert('Oh Sorry!\nWe\'re not taking care of the IE and Edge. '
          + 'So, you have two options:\n'
          + '1. Make your own ASCII diagram service for your environment.\n'
          + '2. Use a web browser, for example: Google Chrome, Firefox etc.\n'
          + '\nWe strongly recommend the second option.');
    }
  </script>
  <noscript>Please enable the Javascript to use ADia.</noscript>
</head>
<body onload="load()">

<nav>
  Logo
</nav>

<%def name="rendertoc(items)">
% if items:
  <ul>
  % for item in items:
    <li>
      <a href="${item['href']}">${item['title']}</a>
      ${rendertoc(item['children'])}
    </li>
  % endfor
  </ul>
% endif
</%def>


<div class="content">
  <!-- Sidebar -->
  <aside>
    <h3>Table of contents</h3>
    ${rendertoc(toc)}
    <h3>Navigation</h3>
    <ul>
    % for h in subdirs:
      <li><a href="${h}">${h}</a></li>
    % endfor
    </ul>

  </aside>
  <div id="splitter" > </div>
  <!-- main content -->
  <main>
    ${content}
  </main>
</div>
<script type="text/javascript" src="/static/index.js"></script>
</body>
</html>
