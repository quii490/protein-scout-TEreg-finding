---
type: protein-evaluation
gene: "IBTK"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## IBTK 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | IBTK / BTKI, KIAA1417 |
| 蛋白名称 | Inhibitor of Bruton tyrosine kinase |
| 蛋白大小 | 1353 aa / 150.5 kDa |
| UniProt ID | Q9P2D0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Membrane; Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1353 aa / 150.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770, IPR000210, IPR009091, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/180** | |
| **归一化总分** | | | **71.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Membrane; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BTKI, KIAA1417 |

**关键文献**:
1. IBTK Differently Modulates Gene Expression and RNA Splicing in HeLa and K562 Cells.. *International journal of molecular sciences*. PMID: 27827994
2. Rare longevity-associated variants, including a reduced-function mutation in cGAS, identified in multigenerational long-lived families.. *bioRxiv : the preprint server for biology*. PMID: 41427385
3. CRL3IBTK Regulates the Tumor Suppressor Pdcd4 through Ubiquitylation Coupled to Proteasomal Degradation.. *The Journal of biological chemistry*. PMID: 25882842
4. IBTK contributes to B-cell lymphomagenesis in Eμ-myc transgenic mice conferring resistance to apoptosis.. *Cell death & disease*. PMID: 30975981
5. mTORC1/S6K1 signaling promotes sustained oncogenic translation through modulating CRL3(IBTK)-mediated ubiquitination of eIF4A1 in cancer cells.. *eLife*. PMID: 38738857

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.7 |
| 高置信度残基 (pLDDT>90) 占比 | 41.5% |
| 置信残基 (pLDDT 70-90) 占比 | 22.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 30.5% |
| 有序区域 (pLDDT>70) 占比 | 63.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.7，有序区 63.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR000210, IPR009091, IPR000408; Pfam: PF12796, PF00651, PF00415 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BTK | 0.950 | 0.639 | — |
| CUL3 | 0.906 | 0.831 | — |
| EIF4A1 | 0.792 | 0.778 | — |
| POP7 | 0.680 | 0.680 | — |
| RPP25L | 0.677 | 0.677 | — |
| AKT1 | 0.613 | 0.319 | — |
| IRAK1BP1 | 0.534 | 0.000 | — |
| ITK | 0.529 | 0.319 | — |
| TMEM248 | 0.507 | 0.000 | — |
| PLEK2 | 0.479 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EIF4A2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SNRPN | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| RGS2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CD2BP2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| hemC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| PPP1CA | psi-mi:"MI:0018"(two hybrid) | imex:IM-16965|pubmed:22321011 |
| BTK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:11577348|imex:IM-20016| |
| LAMTOR3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| EIF4A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.7 + PDB: 无 | pLDDT=70.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Membrane; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. IBTK — Inhibitor of Bruton tyrosine kinase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1353 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P2D0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000005700-IBTK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=IBTK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P2D0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000005700-IBTK/subcellular

![](https://images.proteinatlas.org/23826/224_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/23826/224_H4_2_red_green.jpg)
![](https://images.proteinatlas.org/23826/2269_H5_40_red_green.jpg)
![](https://images.proteinatlas.org/23826/2269_H5_88_red_green.jpg)
![](https://images.proteinatlas.org/23826/226_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/23826/226_H4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9P2D0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
