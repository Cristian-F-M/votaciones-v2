import { useEffect } from "react"
import { getApi, getSessionToken } from "@/utils/API"

export function Dashboard() {

    useEffect(async () => {
        const data = await getApi("http://localhost:8000/user/test/login-required")
        console.log(data)

    }, [])


    return (
        <>
            <h1>Dashboard</h1>
        </>
    )
}