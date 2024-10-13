/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./introduction/introduction/static/js/introduction.js":
/*!*************************************************************!*\
  !*** ./introduction/introduction/static/js/introduction.js ***!
  \*************************************************************/
/***/ (() => {

eval("let check = false\r\nlet copyContentValue = null\r\n\r\nwindow.addEventListener(\"scroll\", function() {\r\n  const element = document.querySelector(\".offcanvas-body ul\");\r\n  const scrollPosition = window.scrollY;\r\n  const elementPosition = element.offsetTop;\r\n\r\n  if (scrollPosition > elementPosition) {\r\n    element.classList.add(\"offcanvas_on-scroll\");\r\n  } else {\r\n    element.classList.remove(\"offcanvas_on-scroll\");\r\n    element.style.transition=\"none\";\r\n  }\r\n});\r\n\r\n\r\nvar offcanvasButton = document.getElementById('offcanvasButton');\r\nvar offcanvasElement = document.getElementById('closecanvas_btn');\r\n\r\noffcanvasButton.addEventListener('click', function () {\r\n    offcanvasButton.classList.add('move-right');\r\n    offcanvasButton.classList.remove('delay');\r\n});\r\n\r\noffcanvasElement.addEventListener('click', function () {\r\n    offcanvasButton.classList.add('delay');\r\n    offcanvasButton.classList.remove('move-right');\r\n\r\n\r\n});\r\n\r\nfunction copyContent() {\r\n\r\n    const scrollWrapper = document.getElementById('scroll-wrapper');\r\n    if (!check) {\r\n        if (window.innerWidth > 1350) {\r\n            check = true;\r\n            const scrollContainer = document.getElementById('scroll-container');\r\n            copyContentValue = scrollContainer.cloneNode(true);\r\n            scrollWrapper.appendChild(copyContentValue);\r\n            }\r\n        } else {\r\n            if (window.innerWidth < 1350) {\r\n                check = false\r\n                if (copyContentValue) {\r\n                    scrollWrapper.removeChild(copyContentValue);\r\n                }\r\n            }\r\n        }\r\n\r\n\r\n\r\n    }\r\n\r\n    window.addEventListener('resize', () => {\r\n        copyContent(check)\r\n    });\r\n\r\n    document.addEventListener('DOMContentLoaded', () => {\r\n        copyContent(check)\r\n    });\r\n\r\n\r\n    document.querySelectorAll('a[href^=\"#\"]').forEach(anchor => {\r\n        anchor.addEventListener('click', function (e) {\r\n            e.preventDefault();\r\n\r\n            document.querySelector(this.getAttribute('href')).scrollIntoView({\r\n                behavior: \"smooth\"\r\n            });\r\n        });\r\n    });\n\n//# sourceURL=webpack:///./introduction/introduction/static/js/introduction.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./introduction/introduction/static/js/introduction.js"]();
/******/ 	
/******/ })()
;