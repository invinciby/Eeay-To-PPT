# Slide Content Spec

Use this reference after outline approval and before style/image generation.

## Purpose

Convert approved slide titles into faithful, slide-ready content. Keep every slide grounded in source material and aligned to its title.

## Required Per-Slide Fields

For each slide, write:

- `slide_number`
- `approved_title`
- `page_role`: cover, background, method, architecture, experiment setup, result, ablation, comparison, discussion, limitation, conclusion, appendix
- `core_point`: one sentence explaining what the page should prove
- `source_basis`: exact source sections, paragraphs, tables, figures, code files, logs, or notes that support the page
- `key_points`: 3-5 slide-ready bullets, not long paper paragraphs
- `must_keep_terms`: exact names, formulas, metrics, method names, datasets, or labels that must not be changed
- `suggested_visual`: diagram, pipeline, comparison matrix, timeline, result figure, flow, architecture map, evidence table, or image collage
- `required_images`: strict assets and style-only references
- `open_uncertainties`: missing facts or data that must not be fabricated
- `speaker_note_hint`: optional short explanation for oral reporting

## Content Rules

- Preserve approved titles unless the user approves a title change.
- Use the user's source material as the only factual basis.
- Do not invent numbers, benchmarks, datasets, conclusions, ablation results, citations, user studies, or experiment outcomes.
- Mark a gap as "source not provided" instead of filling it.
- Prefer one core point per slide.
- Keep bullets short enough for PPT: usually 12-24 Chinese characters per bullet, longer only for dense report pages.
- Convert paper paragraphs into claims, mechanisms, evidence, and implications.
- Use English technical terms only where common or source-preserved.

## Suggested Visual Selection

Choose visuals by what the slide must prove:

- Background/problem: tension map, gap ladder, motivation stack.
- Method: pipeline, module architecture, input-output flow, algorithm loop.
- Experiment setup: dataset-task-metric table, protocol diagram.
- Main result: original result figure, bar/line chart, ranked evidence panel.
- Ablation: factor comparison, contribution stack, before/after layout.
- Case study: screenshot/figure plus annotated callouts.
- Limitation: risk/constraint map.
- Conclusion: thesis recap, contribution triad, next-step roadmap.

Do not default to three cards unless the content is genuinely three independent points.

## Markdown Production Pack Shape

After per-slide content is approved, consolidate into Markdown:

```markdown
# <PPT title>

## Deck Metadata
- Audience:
- Use case:
- Page count:
- Language:
- Style:
- Output:

## Slide 1: <approved title>
### Page Role
...
### Core Point
...
### Source Basis
...
### Page Content
- ...
- ...
### Suggested Visual
...
### Required Images
- strict: path/to/figure.png - preserve internal pixels
- style: path/to/reference.png - style only
### Open Uncertainties
- ...
```

## Source Image Mapping

Classify each image:

- `strict_input_asset`: real experiment/data figure; preserve internal pixels.
- `content_reference`: screenshot or figure that must be included but may be cropped proportionally.
- `style_reference`: reference PPT screenshot or visual mood only.
- `optional_inspiration`: can influence illustration but not mandatory.

Ask the user to confirm strict image mapping before image generation.
