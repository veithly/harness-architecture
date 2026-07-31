#!/usr/bin/env node
/**
 * 校验正式章节是否具备最小的编辑结构。
 *
 * 这里故意不规定统一标题。不同主题应该有不同叙事顺序；脚本只检查
 * 元数据、可导航性与证据入口，避免再次把 22 篇文章压成同一张表格。
 */
import { readFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const PATTERN_DIRS = [
  'src/content/docs/patterns',
  'src/content/docs/en/patterns',
];

const SUPPORT_FILES = [
  ...listMdx('src/content/docs/systems'),
  ...listMdx('src/content/docs/en/systems'),
  'src/content/docs/interview.mdx',
  'src/content/docs/en/interview.mdx',
  'src/content/docs/skill.mdx',
  'src/content/docs/en/skill.mdx',
];

function listMdx(dir) {
  return readdirSync(dir)
    .filter((file) => file.endsWith('.mdx'))
    .map((file) => join(dir, file));
}

function isStub(content) {
  return /^🚧\s*WIP/m.test(content) && !/^##\s+/m.test(content);
}

function frontmatter(content) {
  return content.match(/^---\r?\n([\s\S]*?)\r?\n---/)?.[1] ?? '';
}

function h2s(content) {
  return [...content.matchAll(/^##\s+(.+)$/gm)].map((match) => match[1].trim());
}

function hasEvidence(content) {
  return (
    content.includes('<SourceTrail') ||
    content.includes('<SourceBlock') ||
    /^##\s+(研究底稿|Research notes)/m.test(content) ||
    /\[[^\]]+\]\(https?:\/\//.test(content)
  );
}

let failures = 0;
for (const file of PATTERN_DIRS.flatMap(listMdx)) {
  const content = readFileSync(file, 'utf8');
  if (isStub(content)) {
    console.log(`⏭  ${file} — stub, skipped`);
    continue;
  }

  const problems = [];
  const meta = frontmatter(content);
  const headings = h2s(content);
  const duplicates = headings.filter((heading, index) => headings.indexOf(heading) !== index);

  if (!/^title:\s*.+$/m.test(meta)) problems.push('missing title in frontmatter');
  if (!/^description:\s*.+$/m.test(meta)) problems.push('missing description in frontmatter');
  if (headings.length < 4) problems.push(`only ${headings.length} H2 sections; expected at least 4`);
  if (duplicates.length > 0) problems.push(`duplicate H2 headings: ${[...new Set(duplicates)].join(', ')}`);
  if (!hasEvidence(content)) problems.push('missing a source block, source trail, research note, or external citation');
  if (/^##\s+§\d+/m.test(content)) problems.push('numbered template heading remains');
  if (/30 秒速读|30-second read/.test(content)) problems.push('duplicated 30-second summary remains');
  if (/^##\s+(?:面试题|Interview drill|Interview Drill)/m.test(content)) problems.push('review questions must live in an appendix');
  const interviewAnchors = content.match(/id=["']interview-drill["']/g)?.length ?? 0;
  if (interviewAnchors !== 1) problems.push(`expected one stable interview-drill anchor; found ${interviewAnchors}`);

  if (problems.length > 0) {
    console.error(`❌ ${file}`);
    problems.forEach((problem) => console.error(`   ${problem}`));
    failures++;
  } else {
    console.log(`✅ ${file} — editorial contract satisfied`);
  }
}

for (const file of SUPPORT_FILES) {
  const content = readFileSync(file, 'utf8');
  const problems = [];
  const meta = frontmatter(content);
  const headings = h2s(content);
  const duplicates = headings.filter((heading, index) => headings.indexOf(heading) !== index);

  if (!/^title:\s*.+$/m.test(meta)) problems.push('missing title in frontmatter');
  if (!/^description:\s*.+$/m.test(meta)) problems.push('missing description in frontmatter');
  if (headings.length < 4) problems.push(`only ${headings.length} H2 sections; expected at least 4`);
  if (duplicates.length > 0) problems.push(`duplicate H2 headings: ${[...new Set(duplicates)].join(', ')}`);
  if (/^##\s+§\d+/m.test(content)) problems.push('numbered template heading remains');
  if (/#11--/.test(content)) problems.push('stale link to the old numbered interview section remains');

  if (problems.length > 0) {
    console.error(`❌ ${file}`);
    problems.forEach((problem) => console.error(`   ${problem}`));
    failures++;
  } else {
    console.log(`✅ ${file} — supporting page satisfies the editorial contract`);
  }
}

if (failures > 0) {
  console.error(`\n${failures} chapter(s) failed the editorial contract.`);
  process.exit(1);
}

console.log('\nAll chapters satisfy the editorial contract.');
