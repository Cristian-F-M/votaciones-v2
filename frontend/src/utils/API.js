import { highlightFields } from "./formFields";

export const METHODS = {
    POST: postToApi,
    GET: getToApi
}

async function getToApi(API_URL){
    return fetch(API_URL)
    .then(res => res.json())
    .then(data => data)
    .catch(error => {
        // console.log(error) // TODO -> Hacer que se envién los errores a un servidor
        console.error("Ocurrio un error, intentalo más tarde"); 
    });
}


async function postToApi(API_URL, object){
    return fetch(API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(object)
    })
    .then(res => {
        if(!res.ok) return null
        return res.json()
    })
    .then(data => data)
    .catch(error => {
        console.log(error)
        console.error("Ocurrio un error, intentalo más tarde"); 
    });
}

const getSessionToken = () => {
    return getCookie('session_token') ?? null
}


const getCookie = (cookieName) => {
    const value = document.cookie.split(';').find(c => c.startsWith(cookieName + '='));
    return value
}

export function redirect(to){
    window.location.replace(to)
}

export const loginRequired = () => {
    const session_token = getSessionToken()
    if(!session_token){
        window.location.replace("/login")
    }
}

export async function processApi({ apiUrl, method, object }){
    const res = await method(apiUrl, object)
    if(!res || !res.ok){
        // TODO -> Hacer alerta con el error => alert()
        return null
    }
    return res.data
}


export function setUser(){

}