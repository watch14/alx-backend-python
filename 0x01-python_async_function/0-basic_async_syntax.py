#!/usr/bin/env python3
""" async """
import asyncio
import random


async def wait_random(max_delay=10):
    """ random async """
    rando = random.random() * max_delay
    await asyncio.sleep(rando)
    return rando
