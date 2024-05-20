import { highlightFields } from "./formFields";


export function getApi(API_URL){
    const data = fetch(API_URL)
    .then(async res => {
        if (!res.ok) {
            const data = await res.json();
            alert(data.message)
            return 
        }
        
        const data = await res.json();
        return data

    })
    .then(data => {
        return data;
    })
    .catch(error => {
        console.error(error.message); 
    });

    return data
}


export function postApi(API_URL, object){
    const session_token = getCookie('session_token')

    return fetch(API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(object)
    })
    .then(async res => {
        
        if (!res.ok) {
            const { message, field} = await res.json();
            alert(message);
            
            if(field){
                highlightFields(field)
            }


            return null
        }
        
        const data = await res.json();
        return data
    })
    .catch(error => {
        console.error(error); 
    });
}

const getSessionToken = () => {
    return getCookie('session_token') ?? null
}


const getCookie = (cookieName) => {
    const value = document.cookie.split(';').find(c => c.startsWith(cookieName + '='));
    return value
}



export const loginRequired = () => {
    const session_token = getSessionToken()
    if(!session_token){
        window.location.replace("/login")
    }
}