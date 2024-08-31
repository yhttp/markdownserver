function resize(e) {
  const size = `${e.x}px`;
  sidebar.style.flexBasis = size;
}


function iconCreate(name, href, id) {
  var anchor = document.createElement('a');
  anchor.id = id;
  anchor.href = href;
  anchor.classList.add('icon');
 
  var svg = anchor.appendChild(
    document.createElementNS('http://www.w3.org/2000/svg', 'svg'));
  var use = svg.appendChild(
    document.createElementNS('http://www.w3.org/2000/svg', 'use'));
  use.setAttribute('href', `#icon-${name}`);
  return anchor;
}


function headerLinks(header) {
  var parent = header.parentNode;
  var loc = window.location;
  var href = `${loc.origin}${loc.pathname}#${header.id}`
  var icon = iconCreate('link', href, `ymdlinker-${header.id}`);
  
  header.prepend(icon);
}


const resizer = document.querySelector("#splitter");
const sidebar = document.querySelector("aside");
const headers = document.querySelectorAll(
  'main h1, main h2, main h3, main h4, main h5, main h6');


headers.forEach((v, _, __) => headerLinks(v));


resizer.addEventListener("mousedown", (event) => {
  document.addEventListener("mousemove", resize, false);
  document.addEventListener("mouseup", () => {
    document.removeEventListener("mousemove", resize, false);
  }, false);
});
