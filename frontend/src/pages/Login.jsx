import { LogoSena } from "@/assets/icons/LogoSena";
import { processApi, setUser, redirect, METHODS } from "@/utils/API";
import { useEffect, useState } from "react";
import { removeHighlightFields } from "../utils/formFields";
import { Link } from "react-router-dom";

export function Login() {
    const [typesDocument, setTypesDocuments] = useState(null);
    useEffect(() => {
        async function getResources() {
            const typesDocument = await processApi({
                apiUrl: "http://localhost:8000/resources/types_document",
                method: METHODS.GET,
            });
            setTypesDocuments(typesDocument);
        }

        getResources();
    }, []);

    async function handleSubmit(e) {
        e.preventDefault();
        const { target } = e;
        const type_document = target.type_document.value;
        const document = target.document.value;
        const password = target.password.value;

        if (type_document === "" || document === "" || password === "") {
            alert("Por favor complete todos los campos");
            return;
        }

        const user = await processApi({
            apiUrl: "http://localhost:8000/user/login",
            method: METHODS.POST,
            object: {
                type_document,
                document,
                password,
            },
        });

        if (user) {
            const { Session: session } = user;

            console.log(session.expiration_date);

            setUser({
                user,
                sessionToken: session.token,
                expiresDate: session.expiration_date,
            });
            redirect({
                message: "Login exitoso",
                to: "/Dashboard",
            });
        }
    }

    removeHighlightFields();

    return (
        <>
            <div className="w-screen h-[100dvh] flex items-center justify-center">
                <div className="w-11/12 max-w-[750px] bg-gray-400/10 backdrop-blur-sm flex flex-row m-sm:flex-col">
                    <div className="w-1/2 flex flex-col items-center justify-center px-8 py-3 gap-4 m-sm:w-full">
                        <LogoSena className="size-32 m-sm:size-22" />
                        <h1 className="text-2xl font-semibold text-gray-100/90 text-center text-pretty m-sm:text-xl">
                            Centro de Gestión Agroempresarial del oriente
                        </h1>
                    </div>
                    <div className="w-1/2 flex flex-col items-center justify-center px-8 py-6 m-sm:w-full">
                        <h1 className="text-4xl m-sm:text-3xl font-bold text-gray-100/70">
                            Iniciar Sesión
                        </h1>
                        <form
                            className="w-full"
                            onSubmit={handleSubmit}
                            autoComplete="off"
                        >
                            <div className="flex flex-col mt-4 w-[300px]">
                                <label
                                    className="text-gray-100"
                                    htmlFor="type_document"
                                >
                                    Tipo de documento
                                </label>
                                <select
                                    className="w-full p-2 mt-1 text-gray-900 bg-gray-400/90 rounded"
                                    id="type_document"
                                    name="type_document"
                                >
                                    {typesDocument &&
                                        typesDocument.map((type) => {
                                            return (
                                                <option
                                                    key={type.id}
                                                    value={type.id}
                                                >
                                                    {type.name}
                                                </option>
                                            );
                                        })}
                                </select>
                            </div>
                            <div className="flex flex-col mt-4 w-[300px]">
                                <label
                                    className="text-gray-100"
                                    htmlFor="document"
                                >
                                    Documento
                                </label>
                                <input
                                    className="w-full p-2 mt-1 text-gray-900 bg-gray-400/90 rounded"
                                    type="number"
                                    id="document"
                                    name="document"
                                />
                            </div>
                            <div className="flex flex-col mt-4 w-[300px]">
                                <label
                                    className="text-gray-100"
                                    htmlFor="password"
                                >
                                    Contraseña
                                </label>
                                <input
                                    className="w-full p-2 mt-1 text-gray-900 bg-gray-400/90 rounded"
                                    type="password"
                                    id="password"
                                    name="password"
                                />
                            </div>
                            <div className="flex flex-col mt-4 w-[300px]">
                                <button
                                    className="w-full p-2 text-gray-100 bg-gray-800 rounded"
                                    type="submit"
                                >
                                    Iniciar Sesión
                                </button>
                            </div>
                            <div className="link">
                                <Link to="/register">Registrarse</Link>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </>
    );
}
