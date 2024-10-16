const scrollWrapper = document.getElementById('scroll-wrapper');
const scrollContainer = document.getElementById("scroll-container");
const arrowLeft = document.getElementById("arrow-left");
const arrowRight = document.getElementById("arrow-right");



function isElementLeftInView(element) {
    if (element) {
        const rect = element.getBoundingClientRect();
        return rect.left >= 0;
    }
}

function isElementRightInView(element) {
    if (element) {
        const rect = element.getBoundingClientRect();

        return  rect.right <= window.innerWidth ;
    }


}

// Funktion, um Pfeile anzuzeigen oder auszublenden
function updateArrows() {
    const firstLi = scrollContainer.querySelector("li:first-child");
    const lastLi = scrollContainer.querySelector("li:nth-last-child(2)");



    // Überprüfen, ob das erste <li> sichtbar ist
    if (isElementLeftInView(firstLi)) {

        arrowLeft.classList.add('invisible');
        arrowLeft.classList.add('opacity-0');
        arrowLeft.classList.remove('visible');
        arrowLeft.classList.remove('opacity-100');
    } else {

        arrowLeft.classList.add("visible");
        arrowLeft.classList.add('opacity-100');
        arrowLeft.classList.remove('invisible');
        arrowLeft.classList.remove('opacity-0');
    }

    // Überprüfen, ob das letzte <li> sichtbar ist
    if (isElementRightInView(lastLi)) {
         arrowRight.classList.add('invisible');
         arrowRight.classList.add('opacity-0');
         arrowRight.classList.remove('visible')
         arrowRight.classList.remove('opacity-100');
    } else {
        arrowRight.classList.add("visible");
        arrowRight.classList.add('opacity-100');
        arrowRight.classList.remove('invisible');
        arrowRight.classList.remove('opacity-0');


    }
}

// Eventlistener für das Scrollen im Container
scrollContainer.addEventListener("scroll", () => {
    updateArrows();
});

// Initial aufrufen, um den korrekten Zustand beim Laden zu überprüfen
updateArrows();

// Optional: Funktionen, um nach links/rechts zu scrollen
arrowLeft.addEventListener("click", function () {

    scrollContainer.scrollBy({
        left: -200, // Anpassen nach Bedarf
        behavior: 'smooth'
    });
});

arrowRight.addEventListener("click", function () {

    scrollContainer.scrollBy({
        left: 200, // Anpassen nach Bedarf
        behavior: 'smooth'
    });
    console.log('clickright')
});


let check = false
let copyContentValue = null

window.addEventListener("scroll", function () {
    const element = document.querySelector(".offcanvas-body ul");
    const scrollPosition = window.scrollY;
    const elementPosition = element.offsetTop;

    if (scrollPosition > elementPosition) {
        element.classList.add("offcanvas_on-scroll");
    } else {
        element.classList.remove("offcanvas_on-scroll");
        element.style.transition = "none";
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