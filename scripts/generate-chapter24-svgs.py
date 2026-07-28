#!/usr/bin/env python3
"""Chapter 24 SVGs: four node types + edge contract, and the delegation decision tree. zh + en."""
from pathlib import Path

PUBLIC = Path("public/diagrams")

L = {
    "zh": {
        "nd_label": "四类节点与边上必带的五要素",
        "nd_title": "图工程：四类节点 + 一条边的五要素",
        "nd_sub": "组织工作 = 把活分给四类节点，再把每条交接边说清楚。重点是分工与交接，不是某个图框架",
        "nodes": [("Agent 节点", "带自主循环的模型执行", "贵 · 慢 · 会即兴", "#dbeafe"),
                  ("代码节点", "确定性代码", "便宜 · 快 · 可测试", "#dcfce7"),
                  ("工具节点", "面向模型的代码接口 ACI", "确定性 · 迁就模型习惯", "#fef9c3"),
                  ("人工节点", "审批 / 拿主意 / 补信息", "最慢最贵 · 守边界", "#fee2e2")],
        "edge_head": "一条委派边必带五要素",
        "edge": [("目标 goal", "要达成什么，不是怎么做"),
                 ("上下文 context", "需要知道的背景，仅此而已"),
                 ("权限 toolset", "白名单——且只收窄，不放宽"),
                 ("预算 budget", "最多跑多少步 / 花多少"),
                 ("输出格式", "回什么形状，含依据不止结论")],
        "nd_note": "缺目标会跑偏 · 缺上下文会瞎猜 · 缺权限会越权 · 缺预算会跑飞 · 缺格式会重复劳动",
        "tr_label": "该不该拆图的决策树",
        "tr_title": "决策树：先问该不该拆，再问怎么拆",
        "tr_sub": "默认答案是「不拆」——每条边都是一次上下文复述，多 agent 的 token 成本是成倍的",
        "q0": "一个循环 + 好工具能干完吗？",
        "yes": "能",
        "no": "不能——是哪个信号逼你拆？",
        "single": "不拆。单循环。（默认答案）",
        "signals": [("步骤固定已知", "流水线 + 闸门", "crewAI Process.sequential"),
                    ("子任务运行时才知道", "调度者 + 工人", "crewAI hierarchical + 效力刻度"),
                    ("要多轮打磨到达标", "评审回路", "带硬轮次上限"),
                    ("有人要中途决策", "人工节点", "审批回父 · 带超时兜底")],
        "tr_note": "拆了就上硬防护栏：深度上限、递归禁令、并发上限、预算随边下发——全写进代码，不写进 prompt",
    },
    "en": {
        "nd_label": "Four node types and the five elements every edge must carry",
        "nd_title": "Graph engineering: four node types + an edge's five elements",
        "nd_sub": "Organizing work = split it across four node types, then spell out every handoff edge. About division & handoff, not a graph framework",
        "nodes": [("Agent node", "model execution with its own loop", "costly · slow · improvises", "#dbeafe"),
                  ("Code node", "deterministic code", "cheap · fast · testable", "#dcfce7"),
                  ("Tool node", "model-facing code interface (ACI)", "deterministic · fits the model", "#fef9c3"),
                  ("Human node", "approvals / judgment / info", "slowest, priciest · holds lines", "#fee2e2")],
        "edge_head": "one delegation edge carries five elements",
        "edge": [("goal", "what to achieve, not how"),
                 ("context", "what it needs to know, nothing more"),
                 ("toolset", "allowlist — and only narrows, never widens"),
                 ("budget", "max steps / spend"),
                 ("output format", "the shape back — evidence, not just a verdict")],
        "nd_note": "No goal → drift · no context → guess · no perms → overreach · no budget → runaway · no format → duplicated work",
        "tr_label": "Decision tree for whether to split into a graph",
        "tr_title": "Decision tree: first whether to split, then how",
        "tr_sub": "Default answer is DON'T — every edge is a context retelling, and multi-agent token cost is multiplied",
        "q0": "Can one loop + good tools finish it?",
        "yes": "yes",
        "no": "no — which signal forced the split?",
        "single": "Don't split. Single loop. (default)",
        "signals": [("steps fixed & known", "pipeline + gates", "crewAI Process.sequential"),
                    ("subtasks known at runtime", "orchestrator + workers", "crewAI hierarchical + effort scale"),
                    ("multi-pass to hit quality", "review loop", "with a hard round cap"),
                    ("a human decides mid-flow", "human node", "approval to parent · timeout fallback")],
        "tr_note": "Once you split, hard guardrails: depth cap, recursion ban, concurrency cap, budgets down edges — all in code, not prompts",
    },
}


def nodes(t):
    ns = ""
    for i, (name, desc, tag, fill) in enumerate(t["nodes"]):
        x = 30 + i * 210
        ns += f'''
    <rect x="{x}" y="86" width="190" height="118" rx="12" fill="{fill}" stroke="#1e293b" stroke-width="1.8" />
    <text x="{x + 95}" y="116" class="lbl" text-anchor="middle">{name}</text>
    <foreignObject x="{x + 12}" y="128" width="166" height="40"><p xmlns="http://www.w3.org/1999/xhtml" style="font:10.5px sans-serif;color:#475569;margin:0;line-height:1.3;text-align:center">{desc}</p></foreignObject>
    <text x="{x + 95}" y="192" class="t-s" text-anchor="middle">{tag}</text>'''
    edges = ""
    for i, (name, desc) in enumerate(t["edge"]):
        y = 280 + i * 52
        edges += f'''
    <rect x="250" y="{y}" width="180" height="42" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.5" />
    <text x="340" y="{y + 26}" class="lbl" text-anchor="middle">{name}</text>
    <foreignObject x="450" y="{y + 4}" width="380" height="40"><p xmlns="http://www.w3.org/1999/xhtml" style="font:11px sans-serif;color:#475569;margin:0;line-height:1.3">{desc}</p></foreignObject>'''
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 570" role="img" aria-label="{t['nd_label']}">
  <defs>
    <filter id="wb24"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="241" /><feDisplacementMap in="SourceGraphic" scale="1.5" /></filter>
    <style>
      .h   {{ font: 600 14px sans-serif; fill: #1e293b; }}
      .lbl {{ font: 700 11.5px sans-serif; fill: #1e293b; }}
      .t-s {{ font: 10.5px sans-serif; fill: #64748b; }}
    </style>
  </defs>
  <text x="440" y="26" class="h" text-anchor="middle">{t['nd_title']}</text>
  <text x="440" y="44" class="t-s" text-anchor="middle">{t['nd_sub']}</text>
  <g filter="url(#wb24)">
    {ns}
    <text x="60" y="256" class="lbl">{t['edge_head']}</text>
    {edges}
  </g>
  <text x="440" y="552" class="t-s" text-anchor="middle">{t['nd_note']}</text>
</svg>
'''


def tree(t):
    sig = ""
    for i, (cond, topo, impl) in enumerate(t["signals"]):
        y = 210 + i * 78
        sig += f'''
    <rect x="360" y="{y}" width="180" height="60" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.5" />
    <foreignObject x="370" y="{y + 6}" width="160" height="30"><p xmlns="http://www.w3.org/1999/xhtml" style="font:700 10.5px sans-serif;color:#1e293b;margin:0;line-height:1.25">{cond}</p></foreignObject>
    <text x="450" y="{y + 52}" class="t-s" text-anchor="middle" font-style="italic">{cond and ""}</text>
    <line x1="540" y1="{y + 30}" x2="566" y2="{y + 30}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#ar24t)" />
    <rect x="570" y="{y}" width="180" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="660" y="{y + 26}" class="lbl" text-anchor="middle">{topo}</text>
    <text x="660" y="{y + 46}" class="t-s" text-anchor="middle">{impl}</text>
    <line x1="330" y1="196" x2="356" y2="{y + 30}" stroke="#b45309" stroke-width="1.2" stroke-dasharray="3 3" marker-end="url(#ar24t)" />'''
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 560" role="img" aria-label="{t['tr_label']}">
  <defs>
    <filter id="wb24t"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="247" /><feDisplacementMap in="SourceGraphic" scale="1.5" /></filter>
    <marker id="ar24t" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h   {{ font: 600 14px sans-serif; fill: #1e293b; }}
      .lbl {{ font: 700 11.5px sans-serif; fill: #1e293b; }}
      .t-s {{ font: 10.5px sans-serif; fill: #64748b; }}
      .ok  {{ font: 700 11px sans-serif; fill: #15803d; }}
      .no  {{ font: 700 11px sans-serif; fill: #b45309; }}
    </style>
  </defs>
  <text x="440" y="26" class="h" text-anchor="middle">{t['tr_title']}</text>
  <text x="440" y="44" class="t-s" text-anchor="middle">{t['tr_sub']}</text>
  <g filter="url(#wb24t)">
    <rect x="150" y="86" width="300" height="50" rx="10" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.8" />
    <text x="300" y="116" class="lbl" text-anchor="middle">{t['q0']}</text>

    <text x="120" y="150" class="ok">{t['yes']}</text>
    <line x1="230" y1="136" x2="150" y2="168" stroke="#15803d" stroke-width="1.8" marker-end="url(#ar24t)" />
    <rect x="20" y="172" width="260" height="46" rx="8" fill="#dcfce7" stroke="#15803d" stroke-width="2" />
    <text x="150" y="200" class="lbl" text-anchor="middle">{t['single']}</text>

    <text x="360" y="160" class="no">{t['no']}</text>
    <line x1="330" y1="136" x2="330" y2="200" stroke="#b45309" stroke-width="1.8" marker-end="url(#ar24t)" />
    {sig}
  </g>
  <text x="440" y="544" class="t-s" text-anchor="middle">{t['tr_note']}</text>
</svg>
'''


def write(path: Path, svg: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(svg, encoding="utf-8")
    print(f"wrote {path} ({path.stat().st_size} bytes)")


if __name__ == "__main__":
    write(PUBLIC / "24-nodes-edges.svg", nodes(L["zh"]))
    write(PUBLIC / "24-delegation-tree.svg", tree(L["zh"]))
    write(PUBLIC / "en" / "24-nodes-edges.svg", nodes(L["en"]))
    write(PUBLIC / "en" / "24-delegation-tree.svg", tree(L["en"]))
