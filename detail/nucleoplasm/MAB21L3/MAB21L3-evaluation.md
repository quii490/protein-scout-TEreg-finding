---
type: protein-evaluation
gene: "MAB21L3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAB21L3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAB21L3 / C1orf161 |
| 蛋白名称 | Protein mab-21-like 3 |
| 蛋白大小 | 362 aa / 42.4 kDa |
| UniProt ID | Q8N8X9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 362 aa / 42.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR046903, IPR046906, IPR024810; Pfam: PF03281, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **137.5/180** | |
| **归一化总分** | | | **76.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
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
| PubMed strict count | 5 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf161 |

**关键文献**:
1. The Male Abnormal Gene Family 21 (Mab21) Members Regulate Eye Development.. *Current molecular medicine*. PMID: 27558071
2. Global gene expression changes in the prefrontal cortex of rabbits with hypercholesterolemia and/or hypertension.. *Neurochemistry international*. PMID: 27890723
3. Structural and biochemical characterization of the cell fate determining nucleotidyltransferase fold protein MAB21L1.. *Scientific reports*. PMID: 27271801
4. Potential Roles of Long Non-coding RNAs in the Pathogenesis of Periodontitis: Inflammation Response, Immune Infiltration, Collagen Fibers Synthesis, and Bone Remodeling.. *Current medicinal chemistry*. PMID: 39108010
5. mab21-l3 regulates cell fate specification of multiciliate cells and ionocytes.. *Nature communications*. PMID: 25598413

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.4 |
| 高置信度残基 (pLDDT>90) 占比 | 76.0% |
| 置信残基 (pLDDT 70-90) 占比 | 18.2% |
| 中等置信 (pLDDT 50-70) 占比 | 3.9% |
| 低置信 (pLDDT<50) 占比 | 1.9% |
| 有序区域 (pLDDT>70) 占比 | 94.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.4，有序区 94.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR046903, IPR046906, IPR024810; Pfam: PF03281, PF20266 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ADAMTSL3 | 0.631 | 0.000 | — |
| AGGF1 | 0.629 | 0.629 | — |
| MB21D2 | 0.601 | 0.000 | — |
| STAC3 | 0.559 | 0.556 | — |
| TMEM212 | 0.558 | 0.000 | — |
| TBC1D8B | 0.527 | 0.000 | — |
| FSIP2 | 0.510 | 0.048 | — |
| SLC22A15 | 0.494 | 0.000 | — |
| LARP6 | 0.494 | 0.000 | — |
| GMNC | 0.493 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.4 + PDB: 无 | pLDDT=90.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MAB21L3 — Protein mab-21-like 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小362 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N8X9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173212-MAB21L3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAB21L3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N8X9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000173212-MAB21L3/subcellular

![](https://images.proteinatlas.org/39551/1541_A8_1_red_green.jpg)
![](https://images.proteinatlas.org/39551/1541_A8_3_red_green.jpg)
![](https://images.proteinatlas.org/39551/1542_A8_1_red_green.jpg)
![](https://images.proteinatlas.org/39551/1542_A8_2_red_green.jpg)
![](https://images.proteinatlas.org/39551/1558_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/39551/1558_B3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N8X9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
