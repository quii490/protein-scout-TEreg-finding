---
type: protein-evaluation
gene: "SATL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SATL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SATL1 |
| 蛋白名称 | Spermidine/spermine N(1)-acetyltransferase-like protein 1 |
| 蛋白大小 | 695 aa / 75.8 kDa |
| UniProt ID | Q86VE3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 695 aa / 75.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=47.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016181, IPR051016, IPR000182; Pfam: PF00583 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129/180** | |
| **归一化总分** | | | **71.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Loss-of-function variant in spermidine/spermine N1-acetyl transferase like 1 (SATL1) gene as an underlying cause of autism spectrum disorder.. *Scientific reports*. PMID: 38459140
2. Histone and N-terminal acetyltransferases play important roles in female reproduction and embryogenesis of the red flour beetle Tribolium castaneum.. *Insect molecular biology*. PMID: 40437965

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 47.7 |
| 高置信度残基 (pLDDT>90) 占比 | 21.9% |
| 置信残基 (pLDDT 70-90) 占比 | 2.3% |
| 中等置信 (pLDDT 50-70) 占比 | 0.4% |
| 低置信 (pLDDT<50) 占比 | 75.4% |
| 有序区域 (pLDDT>70) 占比 | 24.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=47.7），有序残基占 24.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016181, IPR051016, IPR000182; Pfam: PF00583 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| POF1B | 0.627 | 0.000 | — |
| APOOL | 0.613 | 0.000 | — |
| DACH2 | 0.609 | 0.069 | — |
| FAM47B | 0.609 | 0.079 | — |
| SMCO3 | 0.607 | 0.000 | — |
| ZNF711 | 0.605 | 0.053 | — |
| KLHL4 | 0.589 | 0.000 | — |
| CPXCR1 | 0.583 | 0.000 | — |
| CYLC1 | 0.583 | 0.053 | — |
| OR1J4 | 0.544 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=47.7 + PDB: 无 | pLDDT=47.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SATL1 — Spermidine/spermine N(1)-acetyltransferase-like protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小695 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=47.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86VE3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184788-SATL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SATL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86VE3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000184788-SATL1/subcellular

![](https://images.proteinatlas.org/60369/2205_C8_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/60369/2205_C8_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/60369/1918_E3_15_cr5cb4839e520f7_red_green.jpg)
![](https://images.proteinatlas.org/60369/1918_E3_6_cr5cb4839e51889_red_green.jpg)
![](https://images.proteinatlas.org/60369/1967_H2_2_red_green.jpg)
![](https://images.proteinatlas.org/60369/1967_H2_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86VE3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
