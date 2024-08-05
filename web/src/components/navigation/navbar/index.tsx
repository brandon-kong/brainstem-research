'use client';

import { useState } from 'react';
import { Menu } from 'react-feather';

import { motion } from 'framer-motion';
import { Role } from './components';

import { NavbarNavigationButtons} from "@/components/navigation/navbuttons";

export default function Navbar() {
    const [open, setOpen] = useState(false);

    return (
        <div
            className={'flex-col flex sidebar-shown:hidden relative shadow-md'}
        >
            <aside className="z-[100] bg-background flex flex-row justify-center fixed py-3 px-6 icon-only:px-6 w-full h-navbar">
                <Role />

                <div className={'h-full items-center justify-center flex'}>
                    <button
                        onClick={() => setOpen(!open)}
                        className={
                            'group cursor-pointer flex items-center justify-center rounded-xl w-10 h-10 p-1 bg-transparent transition-colors duration-300'
                        }
                    >
                        <Menu className="w-6 h-6 stroke-accent-foreground" />
                    </button>
                </div>
            </aside>

            <motion.div
                initial={{ opacity: 0, visibility: 'hidden' }}
                animate={{
                    opacity: open ? 1 : 0,
                    visibility: open ? 'visible' : 'hidden',
                }}
                exit={{ opacity: 0, visibility: 'hidden' }}
                transition={{
                    opacity: { duration: 0.2 },
                    visibility: { delay: open ? 0 : 0.2 },
                }}
                className={
                    'fixed top-0 left-0 w-full h-full bg-black/50 z-[99]'
                }
                onClick={() => setOpen(false)}
            >
                <div
                    className={
                        'flex-col items-center justify-center flex bg-background px-6 pb-4 pt-navbar pointer-events-auto'
                    }
                >
                    <NavbarNavigationButtons />
                </div>
            </motion.div>
        </div>
    );
}