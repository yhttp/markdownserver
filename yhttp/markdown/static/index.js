async function load() {
}


const resizer = document.querySelector("#splitter");
const sidebar = document.querySelector("aside");

resizer.addEventListener("mousedown", (event) => {
  document.addEventListener("mousemove", resize, false);
  document.addEventListener("mouseup", () => {
    document.removeEventListener("mousemove", resize, false);
  }, false);
});

function resize(e) {
  const size = `${e.x}px`;
  sidebar.style.flexBasis = size;
}


// sidebar.style.flexBasis = '325px';
