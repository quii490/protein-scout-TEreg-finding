---
type: protein-evaluation
gene: "GID8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GID8 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GID8 / C20orf11, TWA1 |
| 蛋白名称 | Glucose-induced degradation protein 8 homolog |
| 蛋白大小 | 228 aa / 26.7 kDa |
| UniProt ID | Q9NWU2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cell Junctions; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 228 aa / 26.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.0; PDB: 7NSC |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR013144, IPR024964, IPR006595, IPR006594, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cell Junctions | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell junction (GO:0030054)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- ubiquitin ligase complex (GO:0000151)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf11, TWA1 |

**关键文献**:
1. The interactome of tau phosphorylated at T217 in Alzheimer's disease human brain tissue.. *Acta neuropathologica*. PMID: 40317322
2. PIPE: a protein-protein interaction prediction engine based on the re-occurring short polypeptide sequences between known interacting protein pairs.. *BMC bioinformatics*. PMID: 16872538
3. Gid8p (Dcr1p) and Dcr2p function in a common pathway to promote START completion in Saccharomyces cerevisiae.. *Eukaryotic cell*. PMID: 15590836
4. Studies of recombinant TWA1 reveal constitutive dimerization.. *Bioscience reports*. PMID: 27920276
5. Twa1/Gid8 is a β-catenin nuclear retention factor in Wnt signaling and colorectal tumorigenesis.. *Cell research*. PMID: 28829046

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.0 |
| 高置信度残基 (pLDDT>90) 占比 | 86.8% |
| 置信残基 (pLDDT 70-90) 占比 | 8.8% |
| 中等置信 (pLDDT 50-70) 占比 | 2.2% |
| 低置信 (pLDDT<50) 占比 | 2.2% |
| 有序区域 (pLDDT>70) 占比 | 95.6% |
| 可用 PDB 条目 | 7NSC |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.0，有序区 95.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013144, IPR024964, IPR006595, IPR006594, IPR050618; Pfam: PF10607, PF08513 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RMND5A | 0.999 | 0.934 | — |
| ARMC8 | 0.999 | 0.989 | — |
| WDR26 | 0.999 | 0.987 | — |
| GID4 | 0.996 | 0.955 | — |
| MKLN1 | 0.995 | 0.701 | — |
| RANBP9 | 0.995 | 0.979 | — |
| RANBP10 | 0.990 | 0.965 | — |
| MAEA | 0.960 | 0.784 | — |
| RMND5B | 0.959 | 0.811 | — |
| YPEL5 | 0.885 | 0.633 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VID30 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RNPS1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SLX4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| O22730 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| GID7 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |
| HSC82 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| PFD1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSE1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| P/V | psi-mi:"MI:0096"(pull down) | pubmed:21911578|imex:IM-17703 |
| EPB41L3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-20985|pubmed:24366813 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.0 + PDB: 7NSC | pLDDT=92.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cell Junctions | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GID8 — Glucose-induced degradation protein 8 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小228 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NWU2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101193-GID8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GID8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NWU2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000101193-GID8/subcellular

![](https://images.proteinatlas.org/55047/874_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/55047/874_G1_4_red_green.jpg)
![](https://images.proteinatlas.org/55047/881_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/55047/881_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/55047/927_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/55047/927_D9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NWU2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
