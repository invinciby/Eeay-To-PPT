# 示例PPT标题

## Deck Metadata
- Audience: 课题组汇报
- Use case: 10分钟研究进展汇报
- Page count: 6
- Language: 中文为主，保留英文技术术语
- Style: 清爽学术风，参考 `assets/reference_style.png`
- Output: slide PNGs + optional editable PPTX

## Slide 1: 研究背景与核心问题
### Page Role
background

### Core Point
现有方法在复杂场景下仍存在鲁棒性和解释性不足的问题。

### Source Basis
- 原始材料第 1 节：研究背景
- 原始材料第 2 段：现有方法限制

### Page Content
- 任务场景从单一输入扩展到多源复杂输入
- 现有方法在噪声、遮挡和跨域变化下性能下降
- 本工作关注鲁棒建模与可解释机制设计

### Suggested Visual
左侧问题场景示意图，右侧三项挑战分层结构。

### Required Images
- style: assets/reference_style.png - 仅参考整体风格

### Open Uncertainties
- 暂无明确量化指标，不生成性能数字。

## Slide 2: 方法框架
### Page Role
method

### Core Point
提出的框架通过特征编码、关系建模和结果校准三个模块完成端到端推理。

### Source Basis
- 原始材料方法部分
- Figure 1 方法图

### Page Content
- 输入首先经过统一特征编码模块
- 中间层显式建模样本间关系
- 输出端通过校准模块提升稳定性

### Suggested Visual
SCI 风格三阶段 pipeline，细线箭头，模块标签清晰。

### Required Images
- strict: assets/figure_1_method.png - 真实论文方法图，只能等比插入，不可重画

### Open Uncertainties
- 如果原图中文字过密，保留为原图并在旁边增加解释性 callout。
