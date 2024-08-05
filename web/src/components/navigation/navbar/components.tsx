import { H4 } from '@/components/typography';
import Image from 'next/image';

export function Role() {
    return (
        <div className={'flex flex-col items-center justify-center w-full'}>
            <div className={'flex items-center justify-center'}>
                <Image
                    src="/images/profile-picture.webp"
                    width={100}
                    height={100}
                    alt="logo"
                    priority
                    className="w-12 h-12 icon-only:h-14 icon-only:w-14 rounded-full aspect-square"
                />
            </div>

            <div
                className={
                    'flex-col items-center justify-center mt-5 hidden icon-only:flex'
                }
            >
                <H4 className="text-md font-medium">Brandon Kong</H4>
                <H4 className="mt-1 text-sm tracking-[0] font-normal text-accent-foreground">
                    Full-stack Developer
                </H4>
            </div>
        </div>
    );
}