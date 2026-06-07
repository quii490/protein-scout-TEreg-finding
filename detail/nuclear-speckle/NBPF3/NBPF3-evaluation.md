---
type: protein-evaluation
gene: "NBPF3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NBPF3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NBPF3 |
| 蛋白名称 | NBPF family member NBPF3 |
| 蛋白大小 | 633 aa / 73.0 kDa |
| UniProt ID | Q9H094 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; 额外: Nuclear speckles; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 633 aa / 73.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=47.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR055306, IPR010630; Pfam: PF06758 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Nuclear speckles | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Vitamin B-related Gene Polymorphisms and Cardiovascular Disease.. *Endocrine, metabolic & immune disorders drug targets*. PMID: 35346016
2. Landscape of sex differences in obesity and type 2 diabetes in subcutaneous adipose tissue: a systematic review and meta-analysis of transcriptomics studies.. *Metabolism: clinical and experimental*. PMID: 40157598
3. Insertion of an HERV(K) LTR in the intron of NBPF3 is not required for its transcriptional activity.. *Virology*. PMID: 17391723
4. Different transcription activity of HERV-K LTR-containing and LTR-lacking genes of the KIAA1245/NBPF gene subfamily.. *Genetica*. PMID: 21544646
5. Novel Insights From In Silico Analysis of Biallelic ALPL (c.1001G/A and c.571G/A) in Two Mennonite Families Leading to Hypophosphatasia.. *Cureus*. PMID: 41158885

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 47.1 |
| 高置信度残基 (pLDDT>90) 占比 | 0.3% |
| 置信残基 (pLDDT 70-90) 占比 | 18.5% |
| 中等置信 (pLDDT 50-70) 占比 | 7.9% |
| 低置信 (pLDDT<50) 占比 | 73.3% |
| 有序区域 (pLDDT>70) 占比 | 18.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=47.1），有序残基占 18.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR055306, IPR010630; Pfam: PF06758 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ALPL | 0.886 | 0.045 | — |
| NBPF1 | 0.726 | 0.672 | — |
| ZNF490 | 0.589 | 0.095 | — |
| FAM47A | 0.484 | 0.091 | — |
| CPHXL | 0.472 | 0.057 | — |
| ENSP00000491197 | 0.465 | 0.057 | — |
| TBC1D7 | 0.447 | 0.000 | — |
| ERVW-1 | 0.445 | 0.071 | — |
| MSH3 | 0.410 | 0.042 | — |
| ZNF232 | 0.409 | 0.095 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TSEN15 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EWSR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NBPF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 4
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=47.1 + PDB: 无 | pLDDT=47.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm, Cytosol; 额外: Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 13 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. NBPF3 — NBPF family member NBPF3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小633 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=47.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H094
- Protein Atlas: https://www.proteinatlas.org/ENSG00000142794-NBPF3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NBPF3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H094
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000142794-NBPF3/subcellular

![](https://images.proteinatlas.org/73664/1951_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/73664/1951_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/73664/2162_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/73664/2162_D1_5_red_green.jpg)
![](https://images.proteinatlas.org/73664/2207_A8_1_red_green.jpg)
![](https://images.proteinatlas.org/73664/2207_A8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H094-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H094 |
| SMART | SM01148; |
| UniProt Domain [FT] | DOMAIN 221..313; /note="Olduvai 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00647"; DOMAIN 314..402; /note="Olduvai 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00647"; DOMAIN 405..460; /note="Olduvai 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00647"; DOMAIN 461..552; /note="Olduvai 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00647"; DOMAIN 555..633; /note="Olduvai 5"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00647" |
| InterPro | IPR055306;IPR010630; |
| Pfam | PF06758; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000142794-NBPF3/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
