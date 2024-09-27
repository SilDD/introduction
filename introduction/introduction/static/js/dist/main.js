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

eval("const container = document.getElementById('scrollContainer');\r\n\r\ncontainer.addEventListener('scroll', function() {\r\n  if (container.scrollLeft + container.clientWidth >= container.scrollWidth) {\r\n   \r\n    loadMoreItems();\r\n  }\r\n});\r\n\r\nfunction loadMoreItems() {\r\n  for (let i = 0; i < 5; i++) {\r\n    const newItem = document.createElement('div');\r\n    newItem.className = 'scroll-item';\r\n    newItem.textContent = `Item ${document.querySelectorAll('.scroll-item').length + 1}`;\r\n    container.appendChild(newItem);\r\n  }\r\n}\r\n\n\n//# sourceURL=webpack:///./introduction/introduction/static/js/introduction.js?");

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