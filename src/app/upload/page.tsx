'use client'

import Image from "next/image";
import { FormEvent } from "react";

export default function Upload() {
    async function onSubmit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault();
        const formData = new FormData(event.currentTarget);
        const response = await fetch("/api/upload", {
            method: "POST",
            body: formData,
        });
        if (response.ok) {
            console.log("Uploaded successfully");
        }
        return null;
}
     return (   
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
        <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-lg flex flex-col text-center gap-8">
            <p className="text-2xl">Upload Document</p>
            {/* <label htmlFor="Resource Name">Resource Name:</label>
            <input type="text" id="resource" name="Resource Name" className="border border-1" ></input>
            <label htmlFor="Description">Description:</label>
            <input type="textarea" id="description" name="Description" className="border border-1" ></input>        
            <label htmlFor="File">File:</label>
            <input type="file" id="file" name="File" className="border border-1" ></input> 
            <input type="submit" value="Submit" className="border border-1 bg-blue-300 hover:bg-grey-300 text-white font-bold py-2 px-4 border border-grey-300 rounded" ></input> */}
            <form className="flex flex-col items-start gap-4" onSubmit={onSubmit}>
                <label htmlFor="Resource Name">Resource Name:</label>
                <input type="text" id="resource" name="Resource Name" className="border-gray-800 border w-full" ></input>
                <label htmlFor="Description">Description:</label>
                <input type="textarea" id="description" name="Description" className="border-gray-800 border w-full" ></input> 
                {/* <label htmlFor="file">Upload a file</label> */}
                <input type="file" id="file" name="file" />
                {/* <input type="submit" value="Submit" className="border border-1 bg-blue-300 hover:bg-grey-300 text-white font-bold py-2 px-4 border border-grey-300 rounded"/> */}
                <button type="submit" className="border border-1 bg-blue-600 hover:bg-blue-500 text-white font-bold py-2 px-4 rounded shadow-md active:shadow-none active:bg-blue-700">Submit</button>
            </form>
        </div>   
    </main>
  );
}