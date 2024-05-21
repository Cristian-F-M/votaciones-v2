import { loginRequired } from "@/utils/API";

export function Home() {

    loginRequired()

    return (
    <>
        <h1>Home</h1>

        {
            a.map(b => {
                return <li>{b}</li>
            })
        }
    </>
    );
}
