---
type: protein-evaluation
gene: "FAM181B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM181B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM181B |
| 蛋白名称 | FAM181B (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | FAM181B |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Mitochondria; 额外: Nuclear membrane; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **106/180** | |
| **归一化总分** | | | **58.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nuclear membrane | Approved |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Analysis of the Fam181 gene family during mouse development reveals distinct strain-specific expression patterns, suggesting a role in nervous system development and function.. *Gene*. PMID: 26407640
2. GRK5 as a Novel Therapeutic Target for Immune Evasion in Testicular Cancer: Insights from Multi-Omics Analysis and Immunotherapeutic Validation.. *Biomedicines*. PMID: 40722845
3. Knockout of the family with sequence similarity 181, member A (Fam181a) gene does not impair spermatogenesis or male fertility in the mouse.. *Reproduction, fertility, and development*. PMID: 34253288
4. Morphological Observation and Transcriptome Analysis of Ciliogenesis in Urechis unicinctus (Annelida, Echiura).. *International journal of molecular sciences*. PMID: 37511295
5. Identification of FAM181A and FAM181B as new interactors with the TEAD transcription factors.. *Protein science : a publication of the Protein Society*. PMID: 31697419

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TEAD4 | 0.901 | 0.900 | — |
| ZNF536 | 0.523 | 0.000 | — |
| PRCP | 0.509 | 0.000 | — |
| NABP1 | 0.500 | 0.000 | — |
| TMEM101 | 0.477 | 0.000 | — |
| WFDC10B | 0.471 | 0.000 | — |
| FHAD1 | 0.451 | 0.000 | — |
| CIB4 | 0.434 | 0.000 | — |
| PRSS23 | 0.434 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 9，IntAct interactions: 0
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Mitochondria; 额外: Nuclear membrane | 待确认 |
| PPI | STRING + IntAct | 9 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FAM181B — FAM181B (UniProt未获取)，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/FAM181B
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182103-FAM181B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM181B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/FAM181B
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (approved)。来源: https://www.proteinatlas.org/ENSG00000182103-FAM181B/subcellular

![](https://images.proteinatlas.org/66861/1374_C7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/66861/1374_C7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/66861/1376_C7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/66861/1376_C7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/66861/1422_A4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/66861/1422_A4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
