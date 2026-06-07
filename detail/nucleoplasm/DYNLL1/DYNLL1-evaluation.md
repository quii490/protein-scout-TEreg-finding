---
type: protein-evaluation
gene: "DYNLL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DYNLL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DYNLL1 / DLC1, DNCL1, DNCLC1, HDLC1 |
| 蛋白名称 | Dynein light chain 1, cytoplasmic |
| 蛋白大小 | 89 aa / 10.4 kDa |
| UniProt ID | P63167 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol, Mid piece, Principal piece; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 5/10 | ×1 | 5 | 89 aa / 10.4 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=80 篇 (≤80→4) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=95.3; PDB: 1CMI, 3ZKE, 3ZKF, 6GZJ, 6GZL, 6RLB, 6SC2 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR037177, IPR019763, IPR001372; Pfam: PF01221 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.0/180** | |
| **归一化总分** | | | **61.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol, Mid piece, Principal piece | Approved |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Chromosome; Cytoplasm, cytoskele... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axon cytoplasm (GO:1904115)
- centrosome (GO:0005813)
- ciliary tip (GO:0097542)
- cilium (GO:0005929)
- cytoplasm (GO:0005737)
- cytoplasmic dynein complex (GO:0005868)
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 80 |
| PubMed broad count | 189 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DLC1, DNCL1, DNCLC1, HDLC1 |

**关键文献**:
1. ATM loss disrupts the autophagy-lysosomal pathway.. *Autophagy*. PMID: 32757690
2. Dynamics of the DYNLL1-MRE11 complex regulate DNA end resection and recruitment of Shieldin to DSBs.. *Nature structural & molecular biology*. PMID: 37696958
3. KIF5A-dependent axonal transport deficiency disrupts autophagic flux in trimethyltin chloride-induced neurotoxicity.. *Autophagy*. PMID: 32160081
4. DYNLL1 is hypomethylated and upregulated in a tumor stage- and grade-dependent manner and associated with increased mortality in hepatocellular carcinoma.. *Experimental and molecular pathology*. PMID: 33171156
5. Dimerization of hub protein DYNLL1 and bZIP transcription factor CREB3L1 enhances transcriptional activation of CREB3L1 target genes like arginine vasopressin.. *Peptides*. PMID: 38960286

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.3 |
| 高置信度残基 (pLDDT>90) 占比 | 94.4% |
| 置信残基 (pLDDT 70-90) 占比 | 2.2% |
| 中等置信 (pLDDT 50-70) 占比 | 2.2% |
| 低置信 (pLDDT<50) 占比 | 1.1% |
| 有序区域 (pLDDT>70) 占比 | 96.6% |
| 可用 PDB 条目 | 1CMI, 3ZKE, 3ZKF, 6GZJ, 6GZL, 6RLB, 6SC2, 7D35, 8PR0, 8PR1 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1CMI, 3ZKE, 3ZKF, 6GZJ, 6GZL, 6RLB, 6SC2, 7D35, 8PR0, 8PR1）+ AlphaFold极高置信度预测（pLDDT=95.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037177, IPR019763, IPR001372; Pfam: PF01221 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BCL2L11 | 0.999 | 0.787 | — |
| DYNC2H1 | 0.999 | 0.877 | — |
| DYNC1I2 | 0.998 | 0.935 | — |
| WDR60 | 0.998 | 0.981 | — |
| DYNC1I1 | 0.997 | 0.890 | — |
| WDR34 | 0.997 | 0.947 | — |
| DYNLRB1 | 0.997 | 0.940 | — |
| DYNC1H1 | 0.995 | 0.578 | — |
| DYNC2LI1 | 0.995 | 0.832 | — |
| STRN4 | 0.994 | 0.994 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000447907.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ENSMUSP00000107720.2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Ca2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14760703 |
| Mdh2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14760703 |
| Tubb2b | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14760703 |
| Acta1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14760703 |
| Gapdh | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14760703 |
| Ldha | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14760703 |
| Aldoa | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14760703 |
| Mta1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14760703 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.3 + PDB: 1CMI, 3ZKE, 3ZKF, 6GZJ, 6GZL,  | pLDDT=95.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Nucleoplasm, Cytosol, Mid piece, Principal piece | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DYNLL1 — Dynein light chain 1, cytoplasmic，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小89 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 80 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P63167
- Protein Atlas: https://www.proteinatlas.org/ENSG00000088986-DYNLL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DYNLL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P63167
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000088986-DYNLL1/subcellular

![](https://images.proteinatlas.org/39954/2146_C10_36_blue_red_green.jpg)
![](https://images.proteinatlas.org/39954/2146_C10_58_blue_red_green.jpg)
![](https://images.proteinatlas.org/39954/2153_E9_41_blue_red_green.jpg)
![](https://images.proteinatlas.org/39954/2153_E9_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/39954/2199_A5_10_blue_red_green.jpg)
![](https://images.proteinatlas.org/39954/2199_A5_14_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P63167-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P63167 |
| SMART | SM01375; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR037177;IPR019763;IPR001372; |
| Pfam | PF01221; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000088986-DYNLL1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ADNP | Biogrid, Opencell | true |
| AGGF1 | Biogrid, Opencell | true |
| AMBRA1 | Intact, Biogrid, Opencell | true |
| AMOT | Intact, Biogrid, Opencell | true |
| AMOTL1 | Biogrid, Opencell | true |
| AMOTL2 | Biogrid, Opencell | true |
| ATMIN | Biogrid, Opencell | true |
| BACH1 | Intact, Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
