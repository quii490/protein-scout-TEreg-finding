---
type: protein-evaluation
gene: "TENT4A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TENT4A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TENT4A / PAPD7, POLS, TRF4 |
| 蛋白名称 | Terminal nucleotidyltransferase 4A |
| 蛋白大小 | 792 aa / 84.7 kDa |
| UniProt ID | Q5XG87 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus, nucleoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 792 aa / 84.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR054708, IPR043519, IPR002058, IPR045862; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)
- nuclear membrane (GO:0031965)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- TRAMP complex (GO:0031499)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PAPD7, POLS, TRF4 |

**关键文献**:
1. The ZCCHC14/TENT4 complex is required for hepatitis A virus RNA synthesis.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 35867748
2. Mixed tailing by TENT4A and TENT4B shields mRNA from rapid deadenylation.. *Science (New York, N.Y.)*. PMID: 30026317
3. 3' RNA Uridylation in Epitranscriptomics, Gene Regulation, and Disease.. *Frontiers in molecular biosciences*. PMID: 30057901
4. TENT4A Non-Canonical Poly(A) Polymerase Regulates DNA-Damage Tolerance via Multiple Pathways That Are Mutated in Endometrial Cancer.. *International journal of molecular sciences*. PMID: 34203408
5. A Genome-wide CRISPR Screen Identifies ZCCHC14 as a Host Factor Required for Hepatitis B Surface Antigen Production.. *Cell reports*. PMID: 31801065

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.7 |
| 高置信度残基 (pLDDT>90) 占比 | 34.1% |
| 置信残基 (pLDDT 70-90) 占比 | 8.5% |
| 中等置信 (pLDDT 50-70) 占比 | 5.2% |
| 低置信 (pLDDT<50) 占比 | 52.3% |
| 有序区域 (pLDDT>70) 占比 | 42.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.7），有序残基占 42.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR054708, IPR043519, IPR002058, IPR045862; Pfam: PF22600, PF03828 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZCCHC7 | 0.999 | 0.661 | — |
| MTREX | 0.999 | 0.522 | — |
| POLL | 0.959 | 0.000 | — |
| POLM | 0.948 | 0.000 | — |
| EXOSC10 | 0.875 | 0.431 | — |
| PAPOLB | 0.828 | 0.100 | — |
| PAPOLA | 0.827 | 0.100 | — |
| URI1 | 0.826 | 0.000 | — |
| PAPOLG | 0.826 | 0.100 | — |
| ZCCHC8 | 0.820 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RMND5A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LRP6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ENST00000230859 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |
| SQSTM1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:34524948|imex:IM-30012 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.7 + PDB: 无 | pLDDT=60.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus, nucleoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TENT4A — Terminal nucleotidyltransferase 4A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小792 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=60.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5XG87
- Protein Atlas: https://www.proteinatlas.org/search/TENT4A
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TENT4A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5XG87
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000112941-TENT4A/subcellular

![](https://images.proteinatlas.org/45487/697_A6_4_red_green.jpg)
![](https://images.proteinatlas.org/45487/697_A6_5_red_green.jpg)
![](https://images.proteinatlas.org/45487/776_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/45487/776_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/45487/789_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/45487/789_D4_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5XG87-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5XG87 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 428..486; /note="PAP-associated"; /evidence="ECO:0000255" |
| InterPro | IPR054708;IPR043519;IPR002058;IPR045862; |
| Pfam | PF22600;PF03828; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000112941-TENT4A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| LRP6 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
