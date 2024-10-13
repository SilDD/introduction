let check = false
let copyContentValue = null

window.addEventListener("scroll", function() {
  const element = document.querySelector(".offcanvas-body ul");
  const scrollPosition = window.scrollY;
  const elementPosition = element.offsetTop;

  if (scrollPosition > elementPosition) {
    element.classList.add("offcanvas_on-scroll");
  } else {
    element.classList.remove("offcanvas_on-scroll");
    element.style.transition="none";
  }
});


var offcanvasButton = document.getElementById('offcanvasButton');
var offcanvasElement = document.getElementById('closecanvas_btn');

offcanvasButton.addEventListener('click', function () {
    offcanvasButton.classList.add('move-right');
    offcanvasButton.classList.remove('delay');
});

offcanvasElement.addEventListener('click', function () {
    offcanvasButton.classList.add('delay');
    offcanvasButton.classList.remove('move-right');


});

function copyContent() {

    const scrollWrapper = document.getElementById('scroll-wrapper');
    if (!check) {
        if (window.innerWidth > 1350) {
            check = true;
            const scrollContainer = document.getElementById('scroll-container');
            copyContentValue = scrollContainer.cloneNode(true);
            scrollWrapper.appendChild(copyContentValue);
            }
        } else {
            if (window.innerWidth < 1350) {
                check = false
                if (copyContentValue) {
                    scrollWrapper.removeChild(copyContentValue);
                }
            }
        }



    }

    window.addEventListener('resize', () => {
        copyContent(check)
    });

    document.addEventListener('DOMContentLoaded', () => {
        copyContent(check)
    });


    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: "smooth"
            });
        });
    });