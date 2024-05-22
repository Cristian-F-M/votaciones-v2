import { highlightFields } from "./formFields";

export const METHODS = {
    POST: postToApi,
    GET: getToApi
}

async function getToApi(API_URL){
    return fetch(API_URL, {
        headers: {
        }
    })
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

export const getSessionToken = () => {
    return getCookie('session_token') ?? null
}


const getCookie = (cookieName) => {
    const value = document.cookie.split(';').find(c => {
        c = c.trim()
        return c.startsWith(cookieName)
    })?.trim()
    return value || null
}



export const loginRequired = (message="Debes iniciar sesión para acceder a esta página") => {
    const sessionToke = getSessionToken()
    if(!sessionToke){
        redirect({ to: "/login", message })
        return 
    }
    processApi({ apiUrl: `http://localhost:8000/user/validate-token/${sessionToke}`, method: METHODS.GET })
    redirect({ to: "/Dashboard" })   
}

export async function processApi({ apiUrl, method, object }){
    const res = await method(apiUrl, object)
    if(!res || !res.ok){
        // TODO -> Hacer alerta con el error => alert()
        return null
    }
    return res.data
}


export function redirect({ message, to }){
    if(message) {
        showNotification(message)
        setTimeout(() => {
        }, 1500)    
    }
    if(window.location.pathname === to) return
    window.location.replace(to);
}

export function showNotification(message){
    alert(message)
} 

// TODO -> Use that information from cookie from the server
export function saveSessionToken(session_token){
    document.cookie = `session_token=${session_token}; path=/; expires=Thu, 18 Dec 2021 12:00:00 UTC; SameSite=Lax`;
}

// TODO -> Use that information from cookie from the server
export function removeSessionToken(){
    document.cookie = `session_token=; path=/; expires=Thu, 01 Jan 1970 00:00:00 UTC; SameSite=Lax`;
}

export function setUser({ user, sessionToken, expiresDate }){
    const expiresDateGMT = isoToGmt(expiresDate)
    document.cookie = `user=${JSON.stringify(user)}; expires=${expiresDateGMT}; SameSite=Lax`;
    document.cookie = `session_token=${sessionToken}; expires=${expiresDateGMT}; SameSite=Lax`;
}

export function getUser(){
    const [, user] = getCookie('user')?.split('=')
    if(user){
        return JSON.parse(user)
    }
    return null
}




function isoToGmt(isoString) {
    var date = new Date(isoString);
    return date.toUTCString();
}