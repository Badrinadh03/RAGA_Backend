"""
agents/resume_templates.py — Resume structure/format templates

These are NOT visual/design templates (no fonts, colors, or PDF layout —
the app has no document-rendering pipeline). Each entry is a structural
instruction set the builder/optimizer agents follow when writing resume
text, so the same real content gets organized differently depending on
what the candidate needs (career change, technical depth, leadership, ATS
safety, etc.).
"""

RESUME_TEMPLATES = {
    "CHRONOLOGICAL": {
        "label": "Chronological",
        "description": "Standard reverse-chronological work history. The default — works for most roles and most ATS systems.",
        "guidance": """Structure (in this order): Contact → Summary → Experience (reverse-chronological, most recent first) → Skills → Projects → Education → Certifications.
Emphasize steady career progression — each role should show growth from the previous one. Best default for candidates with a consistent, uninterrupted work history.""",
    },
    "FUNCTIONAL": {
        "label": "Skills-Based / Functional",
        "description": "Groups content by skill category instead of job history. Best for career changers, employment gaps, or role pivots.",
        "guidance": """Structure (in this order): Contact → Summary → Core Skills (grouped by category, each with 1-2 supporting achievement bullets) → Relevant Experience (condensed — titles, companies, dates only, no bullets) → Education.
De-emphasize employment dates and job-title sequence. Emphasize transferable skills and achievements grouped thematically (e.g. "Project Management", "Data Analysis") rather than by employer. Never hide or omit dates — group by skill, don't hide the timeline.""",
    },
    "TECHNICAL": {
        "label": "Technical / Engineering",
        "description": "Optimized for software/engineering roles — leads with technical depth and project specifics.",
        "guidance": """Structure (in this order): Contact → Summary → Technical Skills (grouped: Languages / Frameworks / Databases / Tools / Cloud) → Experience (each bullet includes a technical mechanism + measurable outcome) → Projects (with tech stack and GitHub/live links) → Education.
Every experience and project bullet must name the actual technical mechanism (what was built, which system, how) — never a vague outcome-only bullet like "improved performance". Lead bullets with strong technical action verbs (Architected, Implemented, Optimized, Debugged).""",
    },
    "EXECUTIVE": {
        "label": "Executive / Leadership",
        "description": "For senior, management, or leadership roles — leads with strategic scope and business outcomes over day-to-day tasks.",
        "guidance": """Structure (in this order): Contact → Executive Summary (leadership scope, team size, budget/P&L if applicable) → Core Competencies (strategic areas, not tools) → Professional Experience (business-impact metrics: revenue, team size, org scale, cost savings) → Board/Advisory roles if any → Education.
Emphasize scope of ownership, strategic decisions, and business outcomes. De-emphasize hands-on/individual-contributor tasks unless directly relevant. Never invent metrics or team sizes not confirmed by the candidate.""",
    },
    "ATS_MINIMAL": {
        "label": "ATS-Minimal",
        "description": "Stripped-down formatting for maximum ATS-parsing safety — no tables, columns, icons, or graphics-dependent layout.",
        "guidance": """Structure (in this order): Contact → Summary → Skills (plain comma-separated list, no icons) → Experience → Education → Certifications.
Use exactly these standard section header names: "Experience", "Education", "Skills", "Summary", "Certifications" — nothing stylized. No tables, no multi-column references, no icons/emoji in headers, no special characters. Single-column, plain-text-first formatting throughout — this is the safest structure for older/simpler ATS parsers.""",
    },
    "COMPACT": {
        "label": "Compact",
        "description": "Space-efficient format for candidates with extensive experience (10+ years) — fits a long career into a tight, dense layout without feeling cluttered.",
        "guidance": """Structure (in this order): Contact → Summary (2-3 lines max, no more) → Core Skills (single dense line, comma-separated) → Experience (most recent 3 roles get full detail; every role before that condensed to ONE line each: "Title, Company (Years) — key scope/impact") → Education (one line: degree, institution, year).
Limit each recent role to 2-3 high-impact bullets, not 5-6 — cut anything that isn't a top achievement. Merge short-tenure or minor roles into a single "Additional Experience" line rather than giving each its own block. Prioritize breadth of career shown over exhaustive detail per role — the goal is a long career on one page.""",
    },
    "FIRST_JOB": {
        "label": "First Job / Entry-Level",
        "description": "For students, freshers, and first-time job seekers with little or no formal work experience — leads with education and projects instead of a thin work history.",
        "guidance": """Structure (in this order): Contact → Summary (career objective, 2 lines) → Education (degree, institution, graduation year, GPA if strong, relevant coursework) → Projects (academic, personal, or hackathon — this is the MOST detailed section) → Skills → Experience (internships, part-time work, volunteering — even if brief) → Leadership/Activities (clubs, competitions, college societies).
Lead with Education and Projects since work history is thin or absent — this is expected and should not be apologized for or padded. A strong, detailed Projects section outweighs a weak or irrelevant Experience section for this profile. Never fabricate work experience to fill space.""",
    },
    "CREATIVE": {
        "label": "Creative",
        "description": "For design, marketing, media, writing, and other creative-industry roles — more narrative tone, room for personality, and portfolio-forward.",
        "guidance": """Structure (in this order): Contact (include portfolio/Behance/Dribbble/personal site link prominently, right under name) → Summary (written with personality and voice, not just keyword-stuffed) → Portfolio Highlights (2-3 flagship projects/campaigns, each told as a brief story: challenge → approach → result) → Experience → Skills (tools + soft skills like storytelling, art direction, brand strategy) → Education.
Allow a more conversational, personality-driven tone in the summary than other templates — this is one place where "corporate voice" should be relaxed. Always surface a portfolio link near the top: for creative roles, the work samples matter more than the bullet list.""",
    },
}

DEFAULT_TEMPLATE = "CHRONOLOGICAL"


def get_template_guidance(template_key: str) -> str:
    """Return the structural instruction block for a template key (falls back to default)."""
    t = RESUME_TEMPLATES.get((template_key or "").upper(), RESUME_TEMPLATES[DEFAULT_TEMPLATE])
    return f"\n\n═══════════════════════════════════════════════════\nRESUME TEMPLATE — {t['label']}\n═══════════════════════════════════════════════════\n{t['guidance']}"


def list_templates_text() -> str:
    """Human-readable list of available templates, for chat display."""
    lines = ["## 📄 Available Resume Templates\n"]
    for key, t in RESUME_TEMPLATES.items():
        lines.append(f"**{t['label']}** (`{key}`) — {t['description']}")
    lines.append("\nSay something like *\"use the technical template\"* or *\"switch to executive format\"* to apply one.")
    return "\n".join(lines)
