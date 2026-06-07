---
type: protein-evaluation
gene: "CIAPIN1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CIAPIN1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CIAPIN1 |
| 蛋白名称 | Anamorsin |
| 蛋白大小 | 312 aa / 33.6 kDa |
| UniProt ID | Q6FI81 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Mitochondria; 额外: Nucleoplasm; UniProt: Cytoplasm; Nucleus; Mitochondrion intermembrane space |
| 蛋白大小 | 10/10 | x1 | 10 | 312 aa / 33.6 kDa |
| 研究新颖性 | 4/10 | x5 | 20 | PubMed strict=63 篇 (≤80→4) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=80.2; PDB: 2LD4, 2YUI, 4M7R |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR007785, IPR049011, IPR046408, IPR029063; Pfam:  |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nucleoplasm | Supported |
| UniProt | Cytoplasm; Nucleus; Mitochondrion intermembrane space | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- mitochondrial intermembrane space (GO:0005758)
- mitochondrion (GO:0005739)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 63 |
| PubMed broad count | 102 |
| 别名(未计入scoring) |  |

**关键文献**:
1. CIAPIN1 attenuates ferroptosis via regulating PI3K/AKT pathway in LPS-induced podocytes.. *BMC nephrology*. PMID: 40259237
2. Subcellular localization of CIAPIN1.. *The journal of histochemistry and cytochemistry : official journal of the Histochemistry Society*. PMID: 16957168
3. CIAPIN1 promotes survival, proliferation, migration and glycolysis of endometrial cancer cells through PI3K/Akt pathway.. *Scientific reports*. PMID: 40730854
4. Tat-CIAPIN1 protein prevents against cytokine-induced cytotoxicity in pancreatic RINm5F β-cells.. *BMB reports*. PMID: 34120676
5. Tat-CIAPIN1 inhibits hippocampal neuronal cell damage through the MAPK and apoptotic signaling pathways.. *Free radical biology & medicine*. PMID: 30818058

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.2 |
| 高置信度残基 (pLDDT>90) 占比 | 40.7% |
| 置信残基 (pLDDT 70-90) 占比 | 34.3% |
| 中等置信 (pLDDT 50-70) 占比 | 22.4% |
| 低置信 (pLDDT<50) 占比 | 2.6% |
| 有序区域 (pLDDT>70) 占比 | 75.0% |
| 可用 PDB 条目 | 2LD4, 2YUI, 4M7R |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2LD4, 2YUI, 4M7R）+ AlphaFold高质量预测（pLDDT=80.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007785, IPR049011, IPR046408, IPR029063; Pfam: PF20922, PF05093 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NDOR1 | 0.999 | 0.969 | — |
| GLRX3 | 0.995 | 0.976 | — |
| NUBP1 | 0.967 | 0.281 | — |
| BOLA1 | 0.949 | 0.853 | — |
| CIAO3 | 0.903 | 0.094 | — |
| BOLA2B | 0.844 | 0.468 | — |
| NUBP2 | 0.824 | 0.226 | — |
| CIAO1 | 0.814 | 0.000 | — |
| MMS19 | 0.797 | 0.000 | — |
| BOLA2 | 0.797 | 0.280 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GLRX3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| spn-B | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| Dmel\CG4116 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ENSP00000377914.4 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A0G2RND5 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Tnf | psi-mi:"MI:0096"(pull down) | imex:IM-12051|pubmed:17623297 |
| Dmel\CG13667 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Kat5 | psi-mi:"MI:0096"(pull down) | pubmed:20946988|imex:IM-15160 |
| NDOR1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| CACNB3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.2 + PDB: 2LD4, 2YUI, 4M7R | pLDDT=80.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Mitochondrion intermembrane sp / Mitochondria; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CIAPIN1 -- Anamorsin，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小312 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 63 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6FI81
- Protein Atlas: https://www.proteinatlas.org/ENSG00000005194-CIAPIN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CIAPIN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6FI81
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6FI81-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6FI81 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR007785;IPR049011;IPR046408;IPR029063; |
| Pfam | PF20922;PF05093; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000005194-CIAPIN1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CACNB3 | Intact, Biogrid | true |
| GLRX3 | Intact, Biogrid | true |
| NDOR1 | Intact, Biogrid | true |
| AIMP2 | Biogrid | false |
| BOLA2 | Intact | false |
| BOLA2B | Intact | false |
| GARS1 | Biogrid | false |
| IPO13 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
