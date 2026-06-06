# Style And Image Generation

Use this reference before sample generation, prompt writing, or batch slide image generation.

## Style Extraction

When a reference PPT screenshot is provided, inspect it visually and extract:

- background color and surface treatment;
- title position, scale, weight, and alignment;
- body text style and density;
- accent colors and usage ratio;
- diagram style: flat, vector-like, hand-drawn, SCI figure, dashboard, editorial;
- line weight, arrow style, node/card shape;
- image crop style;
- page number/footer/source-note system;
- whitespace and grid rhythm.

Treat the reference as a style master, not a layout clone. Preserve visual identity while varying composition by slide content.

## Academic Chinese Default Style

When no style is provided, use:

- 16:9 landscape, white or very light background.
- Chinese Heiti-style sans typography; avoid font deformation.
- Clear hierarchy: strong title, compact subtitle if needed, readable labels.
- Fine vector-like scientific diagrams: clean lines, precise arrows, restrained color.
- Diagram and image balanced with text; no text-only pages unless unavoidable.
- Palette: charcoal text, light gray structure, one restrained academic accent, optional second warm marker.
- Avoid decorative gradients, stock photo mood, flashy commercial poster style, and generic three-card templates.

## Sample Selection

Generate 1-2 samples:

- one page that tests the visual style;
- one dense content/result/method page if the deck includes dense pages.

Show the sample image(s) and ask for approval before batch generation.

## Deck System Contract

After sample approval, write a short deck-level contract and include it in every later prompt:

- title location, width, weight, and approximate scale;
- body text scale and density;
- page marker rule: none or consistent marker;
- footer/source-note rule;
- visual diagram style;
- color palette and accent usage;
- bottom summary/takeaway rule;
- strict image placement rule.

Do not let later slides invent new header/footer systems, title scales, or unrelated palettes.

## Image Prompt Shape

Use structured prompts rather than a flat paragraph:

```text
Create one complete 16:9 Chinese academic PowerPoint slide image.

Slide title:
<exact approved title; do not rewrite>

Slide role:
<role in reporting logic>

Core point:
<one sentence>

Content to include:
- <bullet 1>
- <bullet 2>
- <bullet 3>

Main visual / proof object:
<diagram, figure, flow, chart, comparison, architecture map>

Required source images:
<strict/style/content references and rules>

Style reference:
<reference PPT screenshot style summary or approved sample style>

Deck System Contract:
<repeat contract>

Design requirements:
- Keep all content faithful to supplied material.
- Use Chinese Heiti-style typography; avoid garbled, warped, or misspelled Chinese.
- Use clean SCI/academic figure style where illustrations are needed.
- Keep image and text balanced; no crowded layout, no stretched elements.
- Preserve strict experiment/data figures without internal modification.
- Use 4K-quality visual language: crisp fine lines, high clarity, polished academic layout.
- No watermark, no unrelated logo, no random page number unless specified.
```

## Backend Requirements

Use a native full-slide image generation backend:

- built-in Image2/Nano2/image generation tool when available;
- configured API/CLI fallback only when built-in backend is unavailable or user requests it.

Record:

- backend name;
- model if exposed;
- prompt file path;
- output image path;
- required input images;
- QA note.

## Batch Generation Rules

- Generate final slide images as `slide_01.png`, `slide_02.png`, etc.
- Keep rejected variants outside the final image directory.
- Include the approved sample as style reference when possible.
- Regenerate individual failed slides instead of weakening the whole deck style.
- Do not change the approved title or content in the image prompt without user approval.
