'use client'

import Course from "@/components/Course";
import NavBar from "@/components/NavBar";
import Image from "next/image";
import { useState } from "react";

export default function Home() {
  const classes = [
    "SENG-350", "CSC-350", "CSC-305", "SENG-330", "SENG-360", "SENG-320", "SENG-310", "SENG-340", "SENG-380", "SENG-390", "SENG-400", "SENG-410", "SENG-420", "SENG-430", "SENG-440", "SENG-450", "SENG-460", "SENG-470", "SENG-480", "SENG-490"
  ]

  const [search, setSearch] = useState("");

  const handleChange = (e: any) => {
    setSearch(e.target.value);
  }

  return (
    <div className="topnav">
      <input type="text" placeholder="Search.." value={search} onChange={handleChange}>

      </input>
      {
        classes
        .filter((course) => search.length == 0 || course.toLowerCase().includes(search.toLowerCase()))
        .map((course) => {
          return <Course name={course} />
        })
      }
    </div>
  );
}
