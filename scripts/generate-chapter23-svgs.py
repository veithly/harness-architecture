#!/usr/bin/env python3
"""Chapter 23 SVGs: loop anatomy (four deaths -> five components) + budget/breaker flow. zh + en."""
from pathlib import Path

PUBLIC = Path("public/diagrams")

L = {
    "zh": {
        "an_label": "裸循环的四种死法与五个部件的对应关系",
        "an_title": "循环解剖：四种死法 → 五个部件",
        "an_sub": "左边是裸循环在生产环境的死法，右边是救它的部件；中间是那十行循环本体",
        "deaths": [("不会停", "stop_reason 不可靠，单信号判停必卡死"),
                   ("一错到底", "原始错误栈塞回上下文，模型原样重试"),
                   ("上下文爆掉", "长任务只增不减，爆前先变笨"),
                   ("断了回不来", "进程挂掉，内存状态全丢")],
        "loop_steps": ["组装上下文", "调用模型", "执行工具", "结果回填", "判停 / 继续"],
        "comps": [("1 · 停止条件", "多信号互相兜底：final_answer 工具 + 完成检查 + 硬上限"),
                  ("2 · 预算", "步数 / 美元 / 墙钟三维，耗尽前留一次 grace call"),
                  ("3 · 错误分类", "实现错误上抛；模型错误压缩喂回；连续同类走断路器"),
                  ("4 · 轨迹落盘", "每步 finally 写盘，退出是消息不是异常"),
                  ("5 · 验证器", "完成与否由循环外的事实裁决，硬度决定自主权")],
        "an_note": "对应：死法 1 → 部件 1/5 · 死法 2 → 部件 3 · 死法 3 → 部件 2 · 死法 4 → 部件 4",
        "loop_head": "十行循环本体",
        "bd_label": "三维预算与断路器在一轮循环里的检查顺序",
        "bd_title": "预算与断路器：一轮循环的检查顺序",
        "bd_sub": "预算在调模型之前查（mini-swe-agent 模式）；断路器数的是「连续」失败，成功一次就清零",
        "bd_start": "本轮开始",
        "bd_check": "预算检查（调模型前）",
        "bd_dims": ["步数 max_turns", "成本 max_cost_usd（美元）", "墙钟 max_wall_seconds"],
        "bd_ok": "未超限",
        "bd_over": "耗尽",
        "bd_model": "调用模型",
        "bd_tools": "执行工具",
        "bd_err": "全部失败？",
        "bd_streak": "error_streak += 1",
        "bd_reset": "清零 streak",
        "bd_trip": "连续 ≥ 3 次",
        "bd_repeated": "repeated_errors 退出",
        "bd_grace": "grace turn：只许总结，不派新工具",
        "bd_exceeded": "budget_exceeded 退出",
        "bd_note": "两个退出都带 transition_reason 落盘——事后看一眼就知道这一趟是怎么结束的",
    },
    "en": {
        "an_label": "How the four bare-loop deaths map to the five components",
        "an_title": "Loop anatomy: four deaths → five components",
        "an_sub": "Left: how a bare loop dies in production. Right: the components that save it. Middle: the ten-line loop itself",
        "deaths": [("Won't stop", "stop_reason unreliable; single-signal stops jam"),
                   ("One error forever", "raw stack fed back, model retries verbatim"),
                   ("Context blowup", "long tasks only grow; dumber before it dies"),
                   ("Crash loses all", "process dies, in-memory state gone")],
        "loop_steps": ["assemble context", "call model", "run tools", "append results", "stop / continue"],
        "comps": [("1 · Stop conditions", "multiple signals: final_answer tool + checks + hard cap"),
                  ("2 · Budgets", "steps / dollars / wall-clock, one grace call before cutoff"),
                  ("3 · Error taxonomy", "impl errors raise; model errors compacted; breaker on streaks"),
                  ("4 · Trajectory", "every step saved in finally; exit is a message"),
                  ("5 · Verifier", "completion ruled by facts outside the loop")],
        "an_note": "Mapping: death 1 → comps 1/5 · death 2 → comp 3 · death 3 → comp 2 · death 4 → comp 4",
        "loop_head": "the ten-line loop",
        "bd_label": "Where budgets and the breaker sit inside one iteration",
        "bd_title": "Budgets & breaker: check order in one iteration",
        "bd_sub": "Budgets are checked BEFORE the model call (mini-swe-agent); the breaker counts CONSECUTIVE failures, any success resets",
        "bd_start": "iteration start",
        "bd_check": "budget check (pre-call)",
        "bd_dims": ["steps max_turns", "cost max_cost_usd (dollars)", "wall max_wall_seconds"],
        "bd_ok": "within budget",
        "bd_over": "exhausted",
        "bd_model": "call model",
        "bd_tools": "run tools",
        "bd_err": "all failed?",
        "bd_streak": "error_streak += 1",
        "bd_reset": "reset streak",
        "bd_trip": "3 in a row",
        "bd_repeated": "exit: repeated_errors",
        "bd_grace": "grace turn: summarize only, no new tools",
        "bd_exceeded": "exit: budget_exceeded",
        "bd_note": "Both exits land in the trajectory with a transition_reason — one glance tells you how the run ended",
    },
}

DEATH_FILL = "#fee2e2"
COMP_FILL = "#dcfce7"
LOOP_FILL = "#dbeafe"


def anatomy(t):
    deaths = ""
    for i, (name, desc) in enumerate(t["deaths"]):
        y = 96 + i * 118
        deaths += f'''
    <rect x="30" y="{y}" width="230" height="96" rx="10" fill="{DEATH_FILL}" stroke="#1e293b" stroke-width="1.6" />
    <text x="145" y="{y + 26}" class="lbl" text-anchor="middle">{name}</text>
    <foreignObject x="42" y="{y + 36}" width="206" height="56"><p xmlns="http://www.w3.org/1999/xhtml" style="font:10.5px sans-serif;color:#475569;margin:0;line-height:1.35">{desc}</p></foreignObject>'''
    steps = ""
    for i, s in enumerate(t["loop_steps"]):
        y = 130 + i * 82
        steps += f'''
    <rect x="330" y="{y}" width="200" height="46" rx="8" fill="{LOOP_FILL}" stroke="#1e293b" stroke-width="1.6" />
    <text x="430" y="{y + 28}" class="lbl" text-anchor="middle">{s}</text>'''
        if i < 4:
            steps += f'''
    <line x1="430" y1="{y + 46}" x2="430" y2="{y + 78}" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar23)" />'''
    steps += '''
    <path d="M 530 545 C 590 545 590 153 534 153" fill="none" stroke="#1e293b" stroke-width="1.4" stroke-dasharray="4 3" marker-end="url(#ar23)" />'''
    comps = ""
    for i, (name, desc) in enumerate(t["comps"]):
        y = 88 + i * 96
        comps += f'''
    <rect x="620" y="{y}" width="240" height="82" rx="10" fill="{COMP_FILL}" stroke="#1e293b" stroke-width="1.6" />
    <text x="740" y="{y + 22}" class="lbl" text-anchor="middle">{name}</text>
    <foreignObject x="632" y="{y + 30}" width="216" height="50"><p xmlns="http://www.w3.org/1999/xhtml" style="font:10.5px sans-serif;color:#475569;margin:0;line-height:1.35">{desc}</p></foreignObject>'''
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 620" role="img" aria-label="{t['an_label']}">
  <defs>
    <filter id="wb23"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="231" /><feDisplacementMap in="SourceGraphic" scale="1.5" /></filter>
    <marker id="ar23" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h   {{ font: 600 14px sans-serif; fill: #1e293b; }}
      .lbl {{ font: 700 11.5px sans-serif; fill: #1e293b; }}
      .t-s {{ font: 10.5px sans-serif; fill: #64748b; }}
    </style>
  </defs>
  <text x="440" y="26" class="h" text-anchor="middle">{t['an_title']}</text>
  <text x="440" y="44" class="t-s" text-anchor="middle">{t['an_sub']}</text>
  <g filter="url(#wb23)">
    {deaths}
    <text x="430" y="112" class="t-s" text-anchor="middle">{t['loop_head']}</text>
    {steps}
    {comps}
    <line x1="260" y1="144" x2="326" y2="150" stroke="#b91c1c" stroke-width="1.3" stroke-dasharray="3 3" marker-end="url(#ar23)" />
    <line x1="534" y1="200" x2="616" y2="130" stroke="#15803d" stroke-width="1.3" stroke-dasharray="3 3" marker-end="url(#ar23)" />
    <line x1="534" y1="380" x2="616" y2="310" stroke="#15803d" stroke-width="1.3" stroke-dasharray="3 3" marker-end="url(#ar23)" />
  </g>
  <text x="440" y="600" class="t-s" text-anchor="middle">{t['an_note']}</text>
</svg>
'''


def budget(t):
    dims = ""
    for i, d in enumerate(t["bd_dims"]):
        dims += f'<text x="250" y="{140 + i * 16}" class="t-s" text-anchor="middle">{d}</text>'
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 520" role="img" aria-label="{t['bd_label']}">
  <defs>
    <filter id="wb23b"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="237" /><feDisplacementMap in="SourceGraphic" scale="1.5" /></filter>
    <marker id="ar23b" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h   {{ font: 600 14px sans-serif; fill: #1e293b; }}
      .lbl {{ font: 700 11.5px sans-serif; fill: #1e293b; }}
      .t-s {{ font: 10.5px sans-serif; fill: #64748b; }}
      .tag {{ font: 700 10.5px sans-serif; fill: #b91c1c; }}
      .ok  {{ font: 700 10.5px sans-serif; fill: #15803d; }}
    </style>
  </defs>
  <text x="440" y="26" class="h" text-anchor="middle">{t['bd_title']}</text>
  <text x="440" y="44" class="t-s" text-anchor="middle">{t['bd_sub']}</text>
  <g filter="url(#wb23b)">
    <rect x="40" y="90" width="130" height="44" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="105" y="117" class="lbl" text-anchor="middle">{t['bd_start']}</text>
    <line x1="170" y1="112" x2="196" y2="112" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar23b)" />

    <rect x="200" y="82" width="100" height="110" rx="10" fill="#fef9c3" stroke="#1e293b" stroke-width="1.8" />
    <text x="250" y="106" class="lbl" text-anchor="middle">{t['bd_check']}</text>
    {dims}

    <text x="330" y="100" class="ok">{t['bd_ok']}</text>
    <line x1="300" y1="112" x2="392" y2="112" stroke="#15803d" stroke-width="1.8" marker-end="url(#ar23b)" />
    <rect x="396" y="90" width="110" height="44" rx="8" fill="#dbeafe" stroke="#1e293b" stroke-width="1.6" />
    <text x="451" y="117" class="lbl" text-anchor="middle">{t['bd_model']}</text>
    <line x1="506" y1="112" x2="546" y2="112" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar23b)" />
    <rect x="550" y="90" width="110" height="44" rx="8" fill="#dbeafe" stroke="#1e293b" stroke-width="1.6" />
    <text x="605" y="117" class="lbl" text-anchor="middle">{t['bd_tools']}</text>
    <line x1="660" y1="112" x2="706" y2="112" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar23b)" />
    <rect x="710" y="90" width="130" height="44" rx="8" fill="#fde68a" stroke="#1e293b" stroke-width="1.6" />
    <text x="775" y="117" class="lbl" text-anchor="middle">{t['bd_err']}</text>

    <line x1="775" y1="134" x2="775" y2="196" stroke="#b91c1c" stroke-width="1.6" marker-end="url(#ar23b)" />
    <rect x="700" y="200" width="150" height="40" rx="8" fill="#fee2e2" stroke="#1e293b" stroke-width="1.6" />
    <text x="775" y="225" class="lbl" text-anchor="middle">{t['bd_streak']}</text>
    <text x="640" y="270" class="tag">{t['bd_trip']}</text>
    <line x1="775" y1="240" x2="775" y2="292" stroke="#b91c1c" stroke-width="1.6" marker-end="url(#ar23b)" />
    <rect x="670" y="296" width="180" height="44" rx="8" fill="#fecaca" stroke="#b91c1c" stroke-width="2" />
    <text x="760" y="323" class="lbl" text-anchor="middle">{t['bd_repeated']}</text>

    <line x1="605" y1="134" x2="605" y2="200" stroke="#15803d" stroke-width="1.4" stroke-dasharray="3 3" marker-end="url(#ar23b)" />
    <rect x="540" y="204" width="120" height="36" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.4" />
    <text x="600" y="227" class="lbl" text-anchor="middle">{t['bd_reset']}</text>

    <text x="230" y="230" class="tag">{t['bd_over']}</text>
    <line x1="250" y1="192" x2="250" y2="292" stroke="#b91c1c" stroke-width="1.8" marker-end="url(#ar23b)" />
    <rect x="90" y="296" width="330" height="44" rx="8" fill="#ffedd5" stroke="#1e293b" stroke-width="1.8" />
    <text x="255" y="323" class="lbl" text-anchor="middle">{t['bd_grace']}</text>
    <line x1="255" y1="340" x2="255" y2="392" stroke="#b91c1c" stroke-width="1.6" marker-end="url(#ar23b)" />
    <rect x="150" y="396" width="210" height="44" rx="8" fill="#fecaca" stroke="#b91c1c" stroke-width="2" />
    <text x="255" y="423" class="lbl" text-anchor="middle">{t['bd_exceeded']}</text>
  </g>
  <text x="440" y="490" class="t-s" text-anchor="middle">{t['bd_note']}</text>
</svg>
'''


def write(path: Path, svg: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(svg, encoding="utf-8")
    print(f"wrote {path} ({path.stat().st_size} bytes)")


if __name__ == "__main__":
    write(PUBLIC / "23-loop-anatomy.svg", anatomy(L["zh"]))
    write(PUBLIC / "23-budget-breaker.svg", budget(L["zh"]))
    write(PUBLIC / "en" / "23-loop-anatomy.svg", anatomy(L["en"]))
    write(PUBLIC / "en" / "23-budget-breaker.svg", budget(L["en"]))
