'use client';

import { Home, Briefcase, User, PenTool, Mail, Moon } from 'react-feather';
import { usePathname } from 'next/navigation';
import { Button, NavbarButton, SidebarButton } from '../button';

import {
    Tooltip,
    TooltipContent,
    TooltipProvider,
    TooltipTrigger,
} from '@/components/tooltip';

import { useTheme } from 'next-themes';
import React, {ReactElement} from "react";

const navItems = (baseUrl: string = '') => [
    {
        name: 'Homepage',
        href: `${baseUrl}/`,
        icon: <Home size={20} />,
    },
    {
        name: 'Projects',
        href: `${baseUrl}/projects`,
        icon: <Briefcase size={20} />,
    },
    {
        name: 'About',
        href: `${baseUrl}/about`,
        icon: <User size={20} />,
    },
    {
        name: 'Blog',
        href: `${baseUrl}/blog`,
        icon: <PenTool size={20} />,
    },
    {
        name: 'Contact',
        href: `${baseUrl}/contact`,
        icon: <Mail size={20} />,
    },
];

type FooterNavigationButtonsProps = {
    baseUrl?: string;
    selected?: string;
};

export function FooterNavigationButtons({
    baseUrl,
    selected,
}: FooterNavigationButtonsProps): JSX.Element {
    const pathname = usePathname();

    return (
        <TooltipProvider>
            <nav className={'h-auto w-full flex-1'}>
                <ul className="mt-8 flex flex-col items-center h-full gap-1 px-2">
                    {navItems(baseUrl).map((item, index) => {
                        const firstPath = '/' + pathname.split('/')[1];
                        const isSelected = selected
                            ? item.name.toLowerCase() === selected.toLowerCase()
                            : pathname === item.href || firstPath === item.href;

                        return (
                            <li
                                key={index}
                                className="aspect-square icon-only:aspect-auto icon-only:w-full cursor-pointer"
                            >
                                <Tooltip delayDuration={0}>
                                    <TooltipTrigger asChild>
                                        <SidebarButton
                                            active={isSelected}
                                            icon={item.icon}
                                            label={item.name}
                                            href={item.href}
                                        />
                                    </TooltipTrigger>
                                    <TooltipContent
                                        className={'icon-only:hidden'}
                                        side={'right'}
                                    >
                                        {item.name}
                                    </TooltipContent>
                                </Tooltip>
                            </li>
                        );
                    })}
                </ul>
            </nav>
        </TooltipProvider>
    );
}

export function NavbarNavigationButtons({
    baseUrl,
    selected,
}: FooterNavigationButtonsProps): ReactElement {
    const pathname = usePathname();

    return (
        <nav className={'h-auto w-full flex-1 pt-4'}>
            <ul className="flex flex-col items-center h-full gap-1 px-2">
                {navItems(baseUrl).map((item, index) => {
                    const firstPath = '/' + pathname.split('/')[1];
                    const isSelected = selected
                        ? item.name.toLowerCase() === selected.toLowerCase()
                        : pathname === item.href || firstPath === item.href;

                    return (
                        <li key={index} className="w-full cursor-pointer">
                            <NavbarButton
                                active={isSelected}
                                icon={item.icon}
                                label={item.name}
                                href={item.href}
                            />
                        </li>
                    );
                })}
            </ul>
        </nav>
    );
}

export type SocialLinkProps = {
    vertical?: boolean;
};

export function ThemeToggleButton(): JSX.Element {
    const { theme, setTheme } = useTheme();

    return (
        <TooltipProvider>
            <Tooltip delayDuration={0}>
                <TooltipTrigger asChild>
                    <Button
                        onClick={() =>
                            setTheme(theme === 'dark' ? 'light' : 'dark')
                        }
                        variant={'ghost'}
                        size={'icon'}
                        className="w-8 h-8 rounded-full aspect-square p-1 bg-transparent transition-colors duration-300 hover:bg-background-secondary-900"
                    >
                        <Moon size={24} className={'w-6 h-6'} />
                    </Button>
                </TooltipTrigger>
                <TooltipContent side={'right'}>Toggle Theme</TooltipContent>
            </Tooltip>
        </TooltipProvider>
    );
}