const homeUrl = window.location.origin + '/start';

console.log(homeUrl)
console.log(window.location.href)

for (let input of document.querySelectorAll("input")){
        input.autocomplete = "off";
        input.inputMode = "numeric";
        input.pattern = "[0-9]*";
}

