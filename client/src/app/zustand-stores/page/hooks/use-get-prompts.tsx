"use client";
import axios from "axios";
import { setPrompts, getCookie } from "../store/LLM-store";
import { useEffect } from "react";

// Custom hook with useEffect
const useGetPrompts = () => {
  useEffect(() => {
    const fetchData = async () => {
      try {
        const csrftoken = getCookie("csrftoken");
        const config = {
          headers: {
            "content-type": "application/json",
            "X-CSRFToken": csrftoken,
          },
        };
        const response = await axios.get("/prompts.json", config);
        const data = response.data;

        setPrompts(data);
      } catch (err) {
        console.log(err);
      }
    };

    fetchData();
  }, []); // Empty dependencies array ensures this effect runs once on mount
};

export default useGetPrompts;
