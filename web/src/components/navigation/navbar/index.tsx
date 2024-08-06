'use client';

import { useState } from 'react';
import { Menu } from 'react-feather';

import { motion } from 'framer-motion';
import { Role } from './components';

import { NavbarNavigationButtons} from "@/components/navigation/navbuttons";
import {Button} from "@/components/button";
import {Separator} from "@/components/separator";
import Link from "next/link";
import Image from "next/image";
import { P } from "@/components/typography";
import {
    NavigationMenu, NavigationMenuContent,
    NavigationMenuItem,
    NavigationMenuList,
    NavigationMenuTrigger
} from "@/components/ui/navigation-menu";

export default function Navbar() {

    return (
        <div
            className={'flex-col flex sticky top-0 w-full h-fit z-[100] bg-transparent'}
        >
            <div className={'bg-[#0E4174] w-full text-neutral-100 p-2 h-12 text-center text-xs flex items-center justify-center'}>
                <p>
                    Powered by
                    <Link href={'https://www.depaul.edu'} className={'text-sm text-white font-bold hover:underline'}> DePaul University </Link>
                    and
                    <Link href={'https://www.rosalindfranklin.edu'} className={'text-sm text-white font-bold hover:underline'}> Rosalind Franklin University</Link>
                </p>
            </div>

            <aside className="flex flex-row shadow justify-between items-center px-6 py-4 w-full min-h-16">
                <div
                className={'flex items-center gap-2 text-black'}
                >
                    <Link
                        target={'_blank'}
                        href={'https://www.depaul.edu'}>
                        <Image
                            src={'/depaul.png'}
                            alt={'logo'}
                            className={'w-10 h-10'}
                            width={40}
                            height={40}
                        />
                    </Link>
                     <P
                    className={'text-xl font-light'}
                    >
                         x
                        </P>
                     <Link
                        target={'_blank'}
                        href={'https://www.rosalindfranklin.edu'}>
                        <Image
                            src={'/rosalind-franklin.png'}
                            alt={'logo'}
                            className={'w-10 h-10'}
                            width={40}
                            height={40}
                        />
                     </Link>
                    <Separator
                        orientation={'vertical'}
                        className={'h-6 bg-neutral-200 border border-neutral-200'}
                    />
                    <div>
                        <NavigationMenu>
                            <NavigationMenuList>
                                <NavigationMenuItem>
                                    <NavigationMenuTrigger>
                                        Data Pipeline
                                    </NavigationMenuTrigger>
                                    <NavigationMenuContent>
                                        test
                                    </NavigationMenuContent>
                                </NavigationMenuItem>
                                <NavigationMenuItem>
                                    <NavigationMenuTrigger>
                                        Brain Visualization
                                    </NavigationMenuTrigger>
                                    <NavigationMenuContent>
                                        test
                                    </NavigationMenuContent>
                                </NavigationMenuItem>
                            </NavigationMenuList>
                        </NavigationMenu>
                    </div>
                </div>
                <div className={'h-full items-center justify-center flex gap-2'}>
                     <Button
                        variant={"ghost"}
                        >
                        Data Pipeline
                    </Button>
                     <Button
                        variant={"ghost"}
                        >
                        Brain Visualization
                    </Button>

                    <Separator
                        orientation={'vertical'}
                        className={'h-6 bg-neutral-200 border border-neutral-200'}
                    />
                    <Button
                        variant={"ghost"}
                        >
                        Log in
                    </Button>
                    <Button
                        >
                        Create an account
                    </Button>
                </div>
            </aside>
        </div>
    );
}