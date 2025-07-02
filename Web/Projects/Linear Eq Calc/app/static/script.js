const homeUrl = window.location.origin + '/start';

console.log(homeUrl)
console.log(window.location.href)

function ping(){
        fetch('/ping')
                .then(res => {
                        if (res.status === 440){
                                window.location.href = '/offline';
                        }
                })
}

for (let input of document.querySelectorAll("input")){
        input.autocomplete = "off";
        input.inputMode = "numeric";
        input.pattern = "[0-9]*";
}

ping();
setInterval(() => ping(), 5000);

