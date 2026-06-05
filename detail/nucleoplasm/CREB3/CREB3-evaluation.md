---
type: protein-evaluation
gene: "CREB3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CREB3 — REJECTED (研究热度过高 (PubMed strict=144，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CREB3 / LZIP |
| 蛋白名称 | Cyclic AMP-responsive element-binding protein 3 |
| 蛋白大小 | 371 aa / 41.4 kDa |
| UniProt ID | O43889 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Vesicles, Plasma membrane, Primary cilium, Prim; UniProt: Endoplasmic reticulum membrane; Golgi apparatus; Cytoplasm;  |
| 蛋白大小 | 10/10 | ×1 | 10 | 371 aa / 41.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=144 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004827, IPR046347, IPR051381; Pfam: PF00170 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Vesicles, Plasma membrane, Primary cilium, Primary cilium tip, Primary cilium transition zone, Centrosome, Basal body | Supported |
| UniProt | Endoplasmic reticulum membrane; Golgi apparatus; Cytoplasm; Nucleus; Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- membrane (GO:0016020)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 144 |
| PubMed broad count | 254 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LZIP |

**关键文献**:
1. Intrinsic heterogeneity of primary cilia revealed through spatial proteomics.. *Cell*. PMID: 41005307
2. CREB3 protein family: the promising therapeutic targets for cardiovascular and metabolic diseases.. *Cell biology and toxicology*. PMID: 39581923
3. Founder Homozygous Nonsense CREB3 Variant and Variable-Onset Retinal Degeneration.. *JAMA ophthalmology*. PMID: 40674075
4. Comparative Analysis of CREB3 and CREB3L2 Protein Expression in HEK293 Cells.. *International journal of molecular sciences*. PMID: 33803345
5. CREB3 suppresses hepatocellular carcinoma progression by depressing AKT signaling through competitively binding with insulin receptor and transcriptionally activating RNA-binding motif protein 38.. *MedComm*. PMID: 38952575

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.7 |
| 高置信度残基 (pLDDT>90) 占比 | 18.6% |
| 置信残基 (pLDDT 70-90) 占比 | 14.8% |
| 中等置信 (pLDDT 50-70) 占比 | 17.3% |
| 低置信 (pLDDT<50) 占比 | 49.3% |
| 有序区域 (pLDDT>70) 占比 | 33.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.7），有序残基占 33.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004827, IPR046347, IPR051381; Pfam: PF00170 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HCFC1 | 0.990 | 0.871 | — |
| NR0B2 | 0.988 | 0.000 | — |
| CREBRF | 0.981 | 0.292 | — |
| CREB3L2 | 0.964 | 0.541 | — |
| CREB3L4 | 0.960 | 0.551 | — |
| DCSTAMP | 0.959 | 0.292 | — |
| CREB3L3 | 0.958 | 0.513 | — |
| CREB1 | 0.955 | 0.101 | — |
| ATF2 | 0.950 | 0.000 | — |
| EP300 | 0.949 | 0.069 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000342136.2 | psi-mi:"MI:0018"(two hybrid) | pubmed:10675342|imex:IM-19116| |
| Ikbkb | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| HCFC1 | psi-mi:"MI:0013"(biophysical) | pubmed:10629049 |
| EMD | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| APPBP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MALL | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| BNIP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| STX8 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CCR1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15001559|imex:IM-18987 |
| CCR5 | psi-mi:"MI:0018"(two hybrid) | pubmed:15001559|imex:IM-18987 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.7 + PDB: 无 | pLDDT=60.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Golgi apparatus; C / Cytosol; 额外: Vesicles, Plasma membrane, Primary ci | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CREB3 — Cyclic AMP-responsive element-binding protein 3，研究基础较多，新颖性有限。
2. 蛋白大小371 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 144 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 144 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43889
- Protein Atlas: https://www.proteinatlas.org/ENSG00000107175-CREB3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CREB3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43889
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000107175-CREB3/subcellular

![](https://images.proteinatlas.org/30978/2266_D8_68_blue_red_green.jpg)
![](https://images.proteinatlas.org/30978/2266_D8_93_blue_red_green.jpg)
![](https://images.proteinatlas.org/77421/2166_F2_20_blue_red_green.jpg)
![](https://images.proteinatlas.org/77421/2166_F2_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/77421/2176_D2_46_blue_red_green.jpg)
![](https://images.proteinatlas.org/77421/2176_D2_63_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43889-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
