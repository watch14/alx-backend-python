#!/usr/bin/env python3
""" async """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ random async """
    rando = random.random() * max_delay
    await asyncio.sleep(rando)
    return rando
