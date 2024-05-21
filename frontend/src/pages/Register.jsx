import { LogoSena } from "@/assets/icons/LogoSena";
import { processApi, METHODS } from "@/utils/API";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { removeHighlightFields } from "../utils/formFields";
import { redirect } from "../utils/API";

export function Register() {
    const [typesDocument, setTypesDocuments] = useState(null);
    useEffect(() => {
        async function getResources() {
            const typesDocument = await processApi({
                apiUrl: "http://localhost:8000/resources/types_document",
                methods: METHODS.GET,
            });
            setTypesDocuments(typesDocument);
        }

        getResources();
    }, []);

    async function handleSubmit(e) {
        e.preventDefault();
        const { target } = e;
        const name = target.name.value;
        const lastname = target.lastname.value;
        const email = target.email.value;
        const type_document = target.type_document.value;
        const document = target.document.value;
        const phone = target.phone.value;
        const password = target.password.value;
        const confirm_password = target.confirm_password.value;

        if (
            type_document === "" ||
            document === "" ||
            password === "" ||
            confirm_password === "" ||
            name === "" ||
            lastname === "" ||
            email === "" ||
            phone === ""
        ) {
            alert("Por favor complete todos los campos");
            return;
        }

        if (password !== confirm_password) {
            alert("Las contraseñas no coinciden");
            return;
        }

        const data = await processApi({
            apiUrl: "http://localhost:8000/user/register",
            method: METHODS.POST,
            object: {
                name,
                lastname,
                email,
                type_document,
                document,
                phone,
                password,
            },
        });

        // TODO -> Change the alert to a toast

        if (data) {
            redirect({ to: "/login", message: "Usuario registrado" })
        }
    }

    removeHighlightFields();

    return (
        <>
            <div className="w-screen min-h-[100dvh] flex items-center justify-center">
                <div className="w-11/12 max-w-[900px] bg-gray-400/10 backdrop-blur-sm flex flex-row m-md:flex-col">
                    <div className="w-1/3 flex flex-col items-center justify-center px-8 py-3 gap-4 m-md:w-full">
                        <LogoSena className="size-32 m-sm:size-22" />
                        <h1 className="text-2xl font-semibold text-gray-100/90 text-center text-pretty m-sm:text-xl">
                            Centro de Gestión Agroempresarial del oriente
                        </h1>
                    </div>
                    <div className="w-2/3 flex flex-col items-center justify-center px-8 py-6 m-md:w-full">
                        <h1 className="text-4xl m-sm:text-3xl font-bold text-gray-100/70">
                            Registro
                        </h1>
                        <form
                            className="form_register w-full grid gap-x-4"
                            onSubmit={handleSubmit}
                            autoComplete="off"
                        >
                            <div className="flex flex-col mt-4 w-full">
                                <label className="text-gray-100" htmlFor="name">
                                    Nombre
                                </label>
                                <input
                                    className="w-full p-2 mt-1 text-gray-900 bg-gray-400/90 rounded min-w-[250px]"
                                    type="text"
                                    id="name"
                                    name="name"
                                />
                            </div>
                            <div className="flex flex-col mt-4 w-full">
                                <label
                                    className="text-gray-100"
                                    htmlFor="lastname"
                                >
                                    Apellido
                                </label>
                                <input
                                    className="w-full p-2 mt-1 text-gray-900 bg-gray-400/90 rounded min-w-[250px]"
                                    type="text"
                                    id="lastname"
                                    name="lastname"
                                />
                            </div>
                            <div className="flex flex-col mt-4 w-full">
                                <label
                                    className="text-gray-100"
                                    htmlFor="email"
                                >
                                    Correo
                                </label>
                                <input
                                    className="w-full p-2 mt-1 text-gray-900 bg-gray-400/90 rounded min-w-[250px]"
                                    type="text"
                                    id="email"
                                    name="email"
                                />
                            </div>
                            <div className="flex flex-col mt-4 w-full">
                                <label
                                    className="text-gray-100"
                                    htmlFor="username"
                                >
                                    Tipo de documento
                                </label>
                                <select
                                    className="w-full p-2 mt-1 text-gray-900 bg-gray-400/90 rounded min-w-[250px]"
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
                            <div className="flex flex-col mt-4 w-full">
                                <label
                                    className="text-gray-100"
                                    htmlFor="username"
                                >
                                    Documento
                                </label>
                                <input
                                    className="w-full p-2 mt-1 text-gray-900 bg-gray-400/90 rounded min-w-[250px] "
                                    type="number"
                                    id="document"
                                    name="document"
                                />
                            </div>
                            <div className="flex flex-col mt-4 w-full">
                                <label
                                    className="text-gray-100"
                                    htmlFor="phone"
                                >
                                    Telefono
                                </label>
                                <input
                                    className="w-full p-2 mt-1 text-gray-900 bg-gray-400/90 rounded min-w-[250px]"
                                    type="text"
                                    id="phone"
                                    name="phone"
                                />
                            </div>
                            <div className="flex flex-col mt-4 w-full">
                                <label
                                    className="text-gray-100"
                                    htmlFor="password"
                                >
                                    Contraseña
                                </label>
                                <input
                                    className="w-full p-2 mt-1 text-gray-900 bg-gray-400/90 rounded min-w-[250px]"
                                    type="password"
                                    id="password"
                                    name="password"
                                />
                            </div>
                            <div className="flex flex-col mt-4 w-full">
                                <label
                                    className="text-gray-100"
                                    htmlFor="confirm_password"
                                >
                                    Confirmar contraseña
                                </label>
                                <input
                                    className="w-full p-2 mt-1 text-gray-900 bg-gray-400/90 rounded min-w-[250px]"
                                    type="password"
                                    id="confirm_password"
                                    name="confirm_password"
                                />
                            </div>
                            <div className="flex flex-col mt-4 w-full col-start-1 col-end-[-1]">
                                <button
                                    className="w-full p-2 text-gray-100 bg-gray-800 rounded"
                                    type="submit"
                                >
                                    Registrarse
                                </button>
                            </div>
                            <div className="link">
                                <Link to="/login">Iniciar sesión</Link>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </>
    );
}
