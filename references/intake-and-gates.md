# Intake And Gates

Use this reference before producing any deck artifacts.

## Minimum Intake

Collect or infer only when explicitly permitted:

- Source material: document, code, paper, experiment notes, Markdown, or pasted text.
- Target use: academic report, lab meeting, thesis defense, project update, product/technical report, or standalone reading deck.
- Audience: supervisor, reviewers, classmates, team, investors, or public portfolio.
- Page count: exact count or maximum.
- Language: Chinese, English, bilingual, or Chinese-dominant with English technical terms.
- Style source: user-provided PPT screenshot, selected style template, palette, or "use defaults".
- Required images: experiment figures, result plots, screenshots, photos, diagrams, logos.
- Output format: slide PNGs, image-only PPTX, editable PPTX, or both.

Ask only for missing high-impact items. If the user says "use defaults", default to:

- Chinese academic/report deck.
- 16:9.
- 8-12 slides unless source size suggests otherwise.
- Clear academic style: white or light background, black/gray Heiti-style Chinese text, one restrained accent color, fine vector-like diagrams.
- Image-only PPTX unless editable PPTX is requested.

## Approval Gates

Do not advance until each gate is approved.

1. **Outline gate**
   - Show deck title, core reporting logic, slide count, and page list.
   - Include each slide's role and whether it requires source images.
   - Wait for approval before per-slide content specs.

2. **Per-slide content gate**
   - Show each slide's core point, key bullets, source basis, and suggested visual.
   - Wait for approval or accept page-specific revisions.

3. **Style gate**
   - Show extracted visual rules from reference PPT screenshots or selected style.
   - Confirm palette, typography mood, density, illustration/diagram style, and page chrome.

4. **Sample gate**
   - Generate 1-2 representative samples only after content and style approval.
   - Use one dense content page and optionally cover/opening page.
   - Wait for sample approval before full-deck generation.

5. **Per-slide image gate**
   - For each generated slide image, inspect and either approve, revise, or mark blocked.

6. **PPTX/editable gate**
   - Ask whether to package image-only PPTX or run editable reconstruction.
   - If editable mode is requested, record expected limitations before reconstruction.

## Forbidden Early Artifacts

Before outline approval, do not create:

- final production pack;
- final slide jobs;
- image prompts;
- sample images;
- generated slide images;
- PPTX packaging plan;
- editable reconstruction plan.

Draft notes are allowed only when clearly marked as draft.

## User-Facing Outline Handoff

Use this compact approval block:

```markdown
需要你批准的是这套 PPT 大纲：

Deck title:
<title>

Reporting logic:
<one paragraph>

Slide list:
1. <title> - <role / proof object / required images>
2. <title> - <role / proof object / required images>

Recommended sample pages:
- <page number and why>

请回复“批准”或指出需要修改的页；批准前不生成逐页内容、图片 prompt、样张或 PPTX。
```

## State Tracking

Maintain a simple run state whenever the task spans multiple turns:

- `alignment`: pending/approved
- `outline`: draft/approved
- `content_specs`: draft/approved
- `style`: draft/approved
- `sample`: pending/approved
- `slide_images`: pending/in_review/approved
- `pptx`: not_requested/image_only/editable

Record unresolved blockers explicitly instead of silently changing route.
