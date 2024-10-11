let check = false
let copyContentValue = null

function copyContent() {

    const scrollWrapper = document.getElementById('scroll-wrapper');
    if (!check) {
        if (window.innerWidth > 768) {
            check = true;
            const scrollContainer = document.getElementById('scroll-container');
            copyContentValue = scrollContainer.cloneNode(true); // Liste duplizieren
            scrollWrapper.appendChild(copyContentValue);
            }
        } else {
            if (window.innerWidth < 768) {
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