---
type: protein-evaluation
gene: "BRIP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BRIP1 — REJECTED (研究热度过高 (PubMed strict=456，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BRIP1 / BACH1, FANCJ |
| 蛋白名称 | Fanconi anemia group J protein |
| 蛋白大小 | 1249 aa / 140.9 kDa |
| UniProt ID | Q9BX63 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear membrane; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 5/10 | ×1 | 5 | 1249 aa / 140.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=456 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.9; PDB: 1T15, 1T29, 3AL3 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR006555, IPR045028, IPR014013, IPR006554, IPR014 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.5/180** | |
| **归一化总分** | | | **42.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear membrane | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- BRCA1-B complex (GO:0070532)
- cytoplasm (GO:0005737)
- nuclear membrane (GO:0031965)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- replication fork (GO:0005657)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 456 |
| PubMed broad count | 725 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BACH1, FANCJ |

**关键文献**:
1. Hereditary cancer variants and homologous recombination deficiency in biliary tract cancer.. *Journal of hepatology*. PMID: 36243179
2. Pathogenic and likely pathogenic variant prevalence among the first 10,000 patients referred for next-generation cancer panel testing.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 26681312
3. Germline Mutations in the BRIP1, BARD1, PALB2, and NBN Genes in Women With Ovarian Cancer.. *Journal of the National Cancer Institute*. PMID: 26315354
4. Understanding genetic variations associated with familial breast cancer.. *World journal of surgical oncology*. PMID: 39390525
5. Treatment patterns and outcomes in metastatic castration-resistant prostate cancer patients with and without somatic or germline alterations in homologous recombination repair genes.. *Annals of oncology : official journal of the European Society for Medical Oncology*. PMID: 38417742

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.9 |
| 高置信度残基 (pLDDT>90) 占比 | 34.3% |
| 置信残基 (pLDDT 70-90) 占比 | 19.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.5% |
| 低置信 (pLDDT<50) 占比 | 43.2% |
| 有序区域 (pLDDT>70) 占比 | 53.3% |
| 可用 PDB 条目 | 1T15, 1T29, 3AL3 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.9），有序残基占 53.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006555, IPR045028, IPR014013, IPR006554, IPR014001; Pfam: PF06733, PF13307 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BRCA1 | 0.999 | 0.999 | — |
| MLH1 | 0.999 | 0.994 | — |
| BARD1 | 0.999 | 0.994 | — |
| TOPBP1 | 0.999 | 0.994 | — |
| BRCA2 | 0.998 | 0.292 | — |
| PALB2 | 0.998 | 0.292 | — |
| MRE11 | 0.998 | 0.994 | — |
| NBN | 0.998 | 0.994 | — |
| FANCD2 | 0.997 | 0.515 | — |
| FANCI | 0.994 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RRAS | psi-mi:"MI:0018"(two hybrid) | pubmed:18624398|imex:IM-19021 |
| BRCA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:17525340|imex:IM-19729 |
| ABRAXAS1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17525340|imex:IM-19729 |
| MLH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25502805|imex:IM-26175| |
| CDK8 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| MRPL36 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| VWA5A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| POMK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GATD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DOCK5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.9 + PDB: 1T15, 1T29, 3AL3 | pLDDT=63.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm, Nuclear membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BRIP1 — Fanconi anemia group J protein，研究基础较多，新颖性有限。
2. 蛋白大小1249 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 456 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=63.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 456 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BX63
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136492-BRIP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BRIP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BX63
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/BRIP1/IF_images/BRIP1_IF_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000136492-BRIP1/subcellular

![](https://images.proteinatlas.org/5474/110_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/5474/110_D3_2_red_green.jpg)
![](https://images.proteinatlas.org/5474/111_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/5474/111_D3_2_red_green.jpg)
![](https://images.proteinatlas.org/5474/159_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/5474/159_D3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BX63-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
