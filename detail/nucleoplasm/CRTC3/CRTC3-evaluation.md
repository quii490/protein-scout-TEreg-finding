---
type: protein-evaluation
gene: "CRTC3"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CRTC3 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRTC3 / CREB-regulated transcription coactivator 3 |
| 蛋白大小 | 619 aa / 67.0 kDa |
| UniProt ID | Q6UUV7 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | Nucleus; Cytoplasm |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 619 aa / 67.0 kDa |
| 🆕 研究新颖性 | 2/10 | ×5 | 30 | PubMed 100 篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=49.2，PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024786 - TORC; InterPro: IPR024785 - TORC_C; In |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 20 partners, IntAct 67 interactions |
| ➕ 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
|  | **原始总分** |  | **88/183** | **85.0/183** |  |  |  |
|  | **归一化总分** |  | **48.1/100** | **46.4/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |
| Protein Atlas (IF) | Nucleoplasm | Approved |

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CRTC3/IF_images/487_B7_1_blue_red_green.jpg|487_B7_1_blue_red]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CRTC3/IF_images/487_B7_2_blue_red_green.jpg|487_B7_2_blue_red]]

**结论**: 主要核定位，伴部分胞质信号，HPA Approved。

#### 3.2 蛋白大小评估

**评价**: 大小适中，适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 100 |
| 研究方向 | 待补充关键文献摘要 |

**评价**: 有一定研究基础，但仍存在未探索的niche空间。

**关键文献**:
1. Sabbah M et al. (2021). "Dasatinib Stimulates Its Own Mechanism of Resistance by Activating a CRTC3/MITF/Bcl-2 Pathway in Melanoma with Mutant or Amplified c-Kit". *Mol Cancer Res*. PMID: 33741716
2. Li L et al. (2023). "In vitro CRISPR screening uncovers CRTC3 as a regulator of IFN-γ-induced ferroptosis of hepatocellular carcinoma". *Cell Death Discov*. PMID: 37666810
3. Liu J et al. (2018). "Regulation role of CRTC3 in skeletal muscle and adipose tissue". *J Cell Physiol*. PMID: 28322447
4. Koromina M et al. (2024). "Fine-mapping genomic loci refines bipolar disorder risk genes". *medRxiv*. PMID: 38405768
5. Kim YH et al. (2018). "NEDD4L limits cAMP signaling through ubiquitination of CREB-regulated transcription coactivator 3". *FASEB J*. PMID: 29505301
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 49.2 |
| 高置信度残基 (pLDDT>90) 占比 | 6.0% |
| 置信残基 (pLDDT 70-90) 占比 | 5.2% |
| 有序区域 (pLDDT>70) 占比 | 11.2% |
| 可用 PDB 条目 | 无 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CRTC3/CRTC3-PAE.png]]

**评价**: AlphaFold 预测质量一般（pLDDT=49.2），有序区 11.2%。作为新颖蛋白，结构基线下不扣分。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024786 - TORC; InterPro: IPR024785 - TORC_C; InterPro: IPR024784 - TORC_M; InterPro: IPR024783 - TORC_N; Pf |

**染色质调控潜力分析**: 存在注释结构域：InterPro: IPR024786 - TORC; InterPro: IPR024785 - TORC_C; In...。新颖蛋白基线不扣分。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| CRTC2 | 0.952 | — | — |
| CRTC1 | 0.949 | — | — |
| CREB1 | 0.907 | — | — |
| SIK2 | 0.867 | — | — |
| PPARGC1A | 0.774 | — | — |
| SIK1 | 0.681 | — | — |
| SIK1B | 0.671 | — | — |
| SIK3 | 0.626 | — | — |
| RGS2 | 0.608 | — | — |
| FOXJ2 | 0.56 | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-359832|uniprotkb:O70457|uniprotkb:P35214|uniprotkb:Q6FH52|uniprotkb:Q9UDP2|uniprotkb:Q9UN99|ensembl:ENSP00000306330.3 | — | — | — | — |
| intact:EBI-306940|intact:EBI-11759595|ensembl:ENSP00000248975.5|intact:EBI-21351354 | — | — | — | — |
| intact:EBI-359854|uniprotkb:Q567U5|uniprotkb:Q5TZU8|uniprotkb:Q9UP48|uniprotkb:D6W4Z5|ensembl:ENSP00000238081.3|ensembl:ENSP00000371267.4 | — | — | — | — |
| intact:EBI-10770173 | — | — | — | — |
| intact:EBI-11982647|ensembl:ENSP00000318912.3 | — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 无 GO-CC 注释

**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 20
- 仅 IntAct 实验: 67
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 20 个预测互作，IntAct 67 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=49.2 + PDB: 无 | pLDDT=49.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm | 一致 |
| PPI | STRING + IntAct | 20 + 67 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CRTC3 — CREB-regulated transcription coactivator 3，有一定研究基础，但仍存在未探索的niche空间。
2. 蛋白大小619 aa，大小适中，适合常规生化实验和结构解析。

**风险/不确定性**:
1. 已有一定研究，需确认独特研究角度
2. AlphaFold 预测质量一般（pLDDT=49.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新 5 篇关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6UUV7
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRTC3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/CRTC3


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[CRTC3-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CRTC3/CRTC3-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6UUV7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR024786;IPR024785;IPR024784;IPR024783; |
| Pfam | PF12886;PF12885;PF12884; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000140577-CRTC3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| YWHAB | Biogrid, Opencell | true |
| YWHAE | Biogrid, Opencell | true |
| YWHAG | Intact, Biogrid, Opencell | true |
| YWHAH | Biogrid, Opencell | true |
| YWHAZ | Biogrid, Opencell | true |
| CA13 | Intact | false |
| CENPJ | Biogrid | false |
| DCAF7 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
