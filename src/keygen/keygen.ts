import { input } from "@inquirer/prompts";
import generator from "generate-password";
import * as sqlite3 from "sqlite3";
import { open } from "sqlite";

async function openDb() {
    return open({
        filename: 'keys.db',
        driver: sqlite3.Database,
    });
}

async function generateKeys(count: number) {
    return generator.generateMultiple(count, {
        length: 24,
        numbers: true,
        uppercase: true,
        lowercase: false,
    });
}

async function getAnswer(question: string) {
    return Number(await input({ message: question }));
}

async function main() {
    const db = await openDb();

    // Создание таблицы keys, если она не существует
    await db.exec(`
        CREATE TABLE IF NOT EXISTS keys (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT NOT NULL,
            activated_by TEXT
        )
    `);

    const count = await getAnswer("Enter the number of keys to be generated: ");

    const keys = await generateKeys(count);

    for (const key of keys) {
        await db.run(`
            INSERT INTO keys (key, activated_by) 
            VALUES (?, ?)`, key, false);
    }

    console.log(`${count} keys were successfully recorded into the database.`);

    await db.close();
}

main();
