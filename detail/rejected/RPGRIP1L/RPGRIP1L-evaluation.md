---
type: protein-evaluation
gene: "RPGRIP1L"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RPGRIP1L — REJECTED (核定位证据不足 (核定位得分 1/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | RPGRIP1L |
| 蛋白名称 | Protein fantom (RPGRIP1-like protein) |
| 蛋白大小 | 1315 aa / ~151 kDa |
| UniProt ID | Q68CZ1 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 1/10 | ×4 | 4 | 纤毛/中心体: 纤毛过渡区蛋白, 初级纤毛+中心体定位 |
| 蛋白大小 | 10/10 | ×1 | 10 | 1315 aa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed≈150篇, 纤毛病(Joubert/Meckel综合征)研究 |
| 三维结构 | 4/10 | ×3 | 12 | 极大蛋白, AlphaFold整体低置信, 含多个C2/coiled-coil区域 |
| 调控结构域 | 5/10 | ×2 | 10 | C2结构域 + coiled-coil区域 + RPGR相互作用域 |
| PPI 网络 | 5/10 | ×3 | 15 | PPI degree=25 |
| **加权总分** | | | **71/180** | |
| **归一化总分** | | | **39.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- ciliary transition zone (GO:0035869)
- centrosome (GO:0005813)
- cilium (GO:0005929)

**结论**: 该蛋白(又名FTM/蛋白fantom)定位于纤毛过渡区和中心体/基体，是纤毛发生和信号传导关键蛋白。作为纤毛/中心体蛋白，突变导致Joubert综合征7型、Meckel综合征5型。非核蛋白。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 1315 aa，极大蛋白，适合cryo-ET/超分辨显微镜研究。
- **研究现状**: PubMed约150篇，以纤毛病(ciliopathy)和肾单位肾痨相关研究为主。
- **三维结构**: AlphaFold对极大蛋白预测整体低置信度，含多个规则折叠的C2结构域和长coiled-coil区域。
- **结构域**: 多个C2结构域 + coiled-coil区域 + RPGR相互作用结构域。
- **PPI**: 25个互作配体(source STRING)，主要为纤毛/中心体蛋白(NPHP4等)网络。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: RPGRIP1L — 纤毛过渡区蛋白(Protein fantom)，定位于纤毛/中心体，参与纤毛发生和信号传导。非核蛋白，无核定位证据，不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q68CZ1
- Protein Atlas: https://www.proteinatlas.org/search/RPGRIP1L
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RPGRIP1L
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/RPGRIP1L
