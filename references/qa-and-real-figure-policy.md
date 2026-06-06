# QA And Real Figure Policy

Use this reference after every generated slide and before any PPTX packaging.

## Per-Slide QA Checklist

Inspect each generated slide for:

- Correct 16:9 aspect ratio.
- Approved title preserved exactly or semantically identical when exact rendering is impossible.
- Chinese text readable, non-garbled, non-warped, and free of obvious wrong characters.
- No fake citations, numbers, experiment results, author names, or dataset names.
- Key points match the approved slide content spec.
- Layout is not crowded, stretched, or visibly distorted.
- Main visual supports the slide's core point.
- Text and image are balanced.
- Style matches the approved sample and deck system contract.
- Required source images appear in the correct slide and role.
- Strict experiment/data figures preserve internal pixels.
- No watermark, random logo, unintended page marker, or extra unrelated text.

Reject and revise the slide when any hard failure occurs.

## Chinese Text Failure Labels

Use concrete labels in QA notes:

- `garbled_chinese`
- `wrong_character`
- `warped_font`
- `title_changed`
- `tiny_text`
- `single_character_wrap`
- `unreadable_label`
- `mixed_font_drift`

For severe Chinese text failures, reduce text per slide or move detailed text into speaker notes before regenerating.

## Source Faithfulness QA

Compare generated content against the approved production pack:

- If the source does not provide a number, remove the number.
- If the source has a real figure, do not ask the image model to redraw it.
- If a claim is an inference, mark it as interpretation in the brief and avoid visual certainty.
- If source images are missing, block the slide instead of inventing substitute evidence.

## Real Experiment/Data Figure Policy

Classify strict figures before generation:

- real experiment plots;
- quantitative charts;
- microscopy / medical / lab images;
- screenshots of actual systems/results;
- tables or result grids;
- any figure where internal text, curves, axes, legends, values, or pixels matter.

For strict figures:

- Preserve internal pixels.
- Allow only proportional scaling.
- Allow crop only when user approves and no information is removed.
- Do not stretch, distort, redraw, recolor, translate, relabel, smooth, denoise, or restyle.
- Do not regenerate the figure as an illustration.
- Do not alter axes, legends, labels, numbers, lines, dots, bars, or captions inside the figure.

Use this instruction in prompts:

```text
The uploaded experiment/data figure is a real result. Use it only as an inserted source image. Preserve its internal pixels, text, axes, curves, legends, labels, and numbers exactly. Only scale proportionally or place it in a clean frame. Do not redraw, reinterpret, restyle, translate, recolor, crop away information, or modify any internal content.
```

## Strict Figure Backend Gate

If the image backend may alter the strict figure:

1. Stop full-slide image generation for that slide.
2. Ask whether to place the strict figure mechanically in a reconstruction/layout phase.
3. Optionally generate a textless/figureless background with reserved area.
4. Composite or place the strict figure only through deterministic PPT/image placement, not through model redraw.

Record the limitation as `strict_figure_requires_mechanical_placement`.

## Deck-Level QA

After all slides pass individual QA:

- Build or view a contact sheet.
- Check title scale consistency.
- Check style/palette consistency.
- Check page marker consistency.
- Check that dense pages do not become sparse posters.
- Check that no slide has a new unrelated motif.
- Check that all strict figures are accounted for.

Do not package a deck that passes file checks but fails visible contact-sheet consistency.
