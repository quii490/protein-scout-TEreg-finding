---
type: protein-evaluation
gene: "SCGN"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SCGN — REJECTED (核定位证据不足 (核定位得分 1/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | SCGN |
| 蛋白名称 | Secretagogin |
| 蛋白大小 | 276 aa / ~32 kDa |
| UniProt ID | O76038 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 1/10 | ×4 | 4 | 胞质/分泌: EF-hand钙结合蛋白, 胞质定位, 可分泌 |
| 蛋白大小 | 5/10 | ×1 | 5 | 276 aa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed≈180篇, 糖尿病/神经内分泌研究 |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold预测良好, 6个EF-hand规则排列 |
| 调控结构域 | 5/10 | ×2 | 10 | 6个EF-hand钙结合模体(IPR002048), 钙信号感应 |
| PPI 网络 | 3/10 | ×3 | 9 | PPI degree=8 |
| **加权总分** | | | **69/180** | |
| **归一化总分** | | | **38.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular region (GO:0005576)
- secretory granule (GO:0030141)

**结论**: 该蛋白为六EF-hand钙结合蛋白，定位于细胞质并在神经内分泌细胞中可分泌。作为胰岛素结合蛋白和钙信号感应蛋白，分布空间为胞质/分泌途径。非核蛋白。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 276 aa，较小,6个EF-hand模体的典型大小。
- **研究现状**: PubMed约180篇，以糖尿病β细胞功能、神经内分泌和孤独症研究为主。
- **三维结构**: AlphaFold预测良好，6个EF-hand钙结合模体规则排列，高置信度。
- **结构域**: 6个串联EF-hand钙结合模体(IPR002048) + 分泌信号相关区域。
- **PPI**: 8个互作配体(source STRING)，包括胰岛素、SNAP-25和突触蛋白等。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: SCGN — Secretagogin，六EF-hand钙结合蛋白，定位于胞质/分泌颗粒，在胰岛素分泌和神经内分泌功能中发挥钙感应作用。非核蛋白，无核定位证据，不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O76038
- Protein Atlas: https://www.proteinatlas.org/search/SCGN
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SCGN
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/SCGN
