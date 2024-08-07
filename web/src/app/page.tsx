import Image from "next/image";

export default function Home() {
  return (
    <main className="flex flex-col items-center justify-between">
        <div className={'flex flex-col items-center justify-center w-full h-[512px] bg-black'}>
            <Image src={"/abstract-brain.jpg"} alt={'abstract brain'}
            width={2000}
            height={2000}
                   className={'object-cover w-full h-full brightness-50 gradient'}
            />
        </div>

    </main>
  );
}
