const { Plugin, Notice } = require('obsidian');
const { exec } = require('child_process');
const path = require('path');

module.exports = class FlashcardSyncPlugin extends Plugin {
    async onload() {
        this.addCommand({
            id: 'sync-flashcards',
            name: '同步闪卡到 Anki',
            callback: () => this.sync(),
        });

        this.addRibbonIcon('book-open-check', '同步闪卡', () => this.sync());
    }

    async sync() {
        new Notice('正在同步闪卡...');
        const vaultPath = this.app.vault.adapter.basePath;
        const scriptPath = path.join(vaultPath, 'scripts', 'sync_flashcards.py');

        exec(`python "${scriptPath}"`, { cwd: vaultPath }, (error, stdout, stderr) => {
            if (error) {
                new Notice(`同步失败: ${error.message}`, 5000);
                console.error(stderr);
                return;
            }
            // Parse last line for summary
            const lines = stdout.trim().split('\n');
            const summary = lines[lines.length - 1] || '同步完成';
            new Notice(summary, 3000);
            console.log(stdout);
        });
    }
};
