---
type: protein-evaluation
gene: "FAM227A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM227A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM227A |
| 蛋白名称 | Protein FAM227A |
| 蛋白大小 | 570 aa / 66.2 kDa |
| UniProt ID | F5H4B4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 5/10 | ×4 | 20 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 570 aa / 66.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029417; Pfam: PF14922 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Uncertain |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据存在但较为混杂，部分数据源指向非核区室。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The tumor microenvironment reprograms FAM227A expression: Implications for CRC metastasis and diagnostic biomarker development.. *Biochemical and biophysical research communications*. PMID: 41145065
2. Genetic variant in a BaP-activated super-enhancer increases prostate cancer risk by promoting AhR-mediated FAM227A expression.. *Journal of biomedical research*. PMID: 38410974

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.6 |
| 高置信度残基 (pLDDT>90) 占比 | 13.3% |
| 置信残基 (pLDDT 70-90) 占比 | 34.4% |
| 中等置信 (pLDDT 50-70) 占比 | 22.5% |
| 低置信 (pLDDT<50) 占比 | 29.8% |
| 有序区域 (pLDDT>70) 占比 | 47.7% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM227A/FAM227A-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=64.6），有序残基占 47.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029417; Pfam: PF14922 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ARPC1B | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 1
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.6 + PDB: 无 | pLDDT=64.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 0 + 1 interactions | 数据有限 |

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
1. FAM227A — Protein FAM227A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小570 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/F5H4B4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184949-FAM227A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM227A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/F5H4B4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM227A/FAM227A-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000184949-FAM227A/subcellular

![](https://images.proteinatlas.org/3077/1276_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/3077/1276_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/3077/53_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/3077/53_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/3077/54_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/3077/54_G1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | F5H4B4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029417; |
| Pfam | PF14922; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000184949-FAM227A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARPC1B | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
