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


let offcanvasButton = document.getElementById('offcanvasButton');
let offcanvasElement = document.getElementById('closecanvas_btn');


offcanvasButton.addEventListener('click', (e) => {
    e.stopPropagation();
    offcanvasButton.classList.add('move-right');
    offcanvasButton.classList.remove('delay');
});

offcanvasElement.addEventListener('click', (e) => {
    e.stopPropagation();
    offcanvasButton.classList.add('delay');
    offcanvasButton.classList.remove('move-right');
});

document.addEventListener('DOMContentLoaded', () => {

    document.addEventListener('click', (e) => {

        if (!offcanvasButton.contains(e.target) && !offcanvasElement.contains(e.target)) {
            if (offcanvasButton.classList.contains('move-right')) {

                offcanvasButton.classList.add('delay');
                offcanvasButton.classList.remove('move-right');
            }
        }
    });
});


document.addEventListener('DOMContentLoaded', () => {
    const body = document.querySelector('body');

    body.addEventListener('click', () => {
        if (offcanvasButton.classList.contains('move-right')) {
            console.log('test');
            offcanvasButton.classList.add('delay');
            offcanvasButton.classList.remove('move-right');
        }
    });
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