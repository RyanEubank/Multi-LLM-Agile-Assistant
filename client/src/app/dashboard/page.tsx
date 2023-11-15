"use client";
import Image from "next/image";
import { NextPage } from "next";
import { Footer } from "../components/layouts/footer";
import Link from "next/link";
import OutputBlock from "../components/llm_output/outputBlock";
import LlmInputSearchToolbar from "../components/llm_input/llm-input-search-toolbar";
import { useLLMStore } from "../zustand-stores/page/store/LLM-store";

const multiLLM: NextPage = () => {
  const outputData = useLLMStore.use.outputData();

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-12">
      <div className="w-full items-center justify-between font-mono text-sm lg:flex">
        <Link
          className="fixed left-0 top-0 flex w-full justify-center border-b border-gray-300 bg-gradient-to-b from-zinc-200 pb-6 pt-8 backdrop-blur-2xl dark:border-neutral-800 dark:bg-zinc-800/30 dark:from-inherit lg:static lg:w-auto  lg:rounded-xl lg:border lg:bg-gray-200 lg:p-4 lg:dark:bg-zinc-800/30"
          href={"/"}
        >
          MultiLLM
        </Link>
        <div className="fixed bottom-0 left-0 flex h-48 w-full items-end justify-center bg-gradient-to-t from-white via-white dark:from-black dark:via-black lg:static lg:h-auto lg:w-auto lg:bg-none">
          <a
            className="pointer-events-none flex place-items-center gap-2 p-8 lg:pointer-events-auto lg:p-0"
            href="https://argodata.com/"
            target="_blank"
            rel="noopener noreferrer"
          >
            <Image
              src="http://localhost:3000/argo.svg"
              alt="argo logo"
              className="dark:invert"
              width={80}
              height={24}
              priority
            />
          </a>
        </div>
      </div>
      <LlmInputSearchToolbar></LlmInputSearchToolbar>
      {!!outputData && (
        <div className="Outputs flex flex-row">
          {outputData.map(({ model, response }) => (
            <OutputBlock
              key={model}
              llm={model}
              output={response}
            ></OutputBlock>
          ))}
        </div>
      )}
      <Footer></Footer>
    </main>
  );
};

export default multiLLM;
