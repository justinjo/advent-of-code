import { readFileSync } from "fs";

const input: string[] = readFileSync("./src/2025/advent_2025_day_01.txt", "utf-8").trim().split('\n')

function modulo(a: number, b: number) {
    return ((a % b) + b) % b;
}

function part1(): number {
    let password = 0;
    let dial = 50;
    for (const rotation of input) {
        dial += (rotation[0] == 'R') ? parseInt(rotation.slice(1)) : -parseInt(rotation.slice(1));
        password += (modulo(dial, 100) === 0) ? 1 : 0;
    }
    return password;
}

function part2(): number {
    let password = 0;
    let dial = 50;
    for (const rotation of input) {
        let delta = (rotation[0] == 'R') ? parseInt(rotation.slice(1)) : -parseInt(rotation.slice(1));
        password += Math.abs(Math.floor((dial + delta) / 100));
        if (delta < 0) {
            password -= (dial === 0) ? 1 : 0
            password += (modulo(dial + delta, 100) === 0) ? 1 : 0;
        }
        dial = modulo(dial + delta, 100);
    }
    return password;
}

console.log("Advent of Code 2025 - Day 1");
console.log(`Part 1: ${part1()}`);
console.log(`Part 2: ${part2()}`);