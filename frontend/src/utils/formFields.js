export function highlightFields (field){
    const fieldElement = document.getElementById(field)
    fieldElement.classList.add('error')
    fieldElement.focus() 
}



export function removeHighlightFields (){
    const fields = document.querySelectorAll("input, select");
    fields.forEach((field) => {
        field.addEventListener("input", () => {
            field.classList.remove("error");
        });
    });
}