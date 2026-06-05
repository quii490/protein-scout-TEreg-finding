---
type: protein-evaluation
gene: "GPAM"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPAM — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=146，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPAM / GPAT1, KIAA1560 |
| 蛋白名称 | Glycerol-3-phosphate acyltransferase 1, mitochondrial |
| 蛋白大小 | 828 aa / 93.8 kDa |
| UniProt ID | Q9HCL2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Mitochondria; UniProt: Mitochondrion outer membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 828 aa / 93.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=146 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=80.1; PDB: 8E4Y, 8E50 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR022284, IPR045520, IPR041728, IPR028354, IPR002 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **70.0/180** | |
| **归一化总分** | | | **38.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Approved |
| UniProt | Mitochondrion outer membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- mitochondrial outer membrane (GO:0005741)
- mitochondrion (GO:0005739)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 146 |
| PubMed broad count | 238 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GPAT1, KIAA1560 |

**关键文献**:
1. TXNIP/VDUP1 attenuates steatohepatitis via autophagy and fatty acid oxidation.. *Autophagy*. PMID: 33190588
2. Genome-wide association meta-analysis identifies 17 loci associated with nonalcoholic fatty liver disease.. *Nature genetics*. PMID: 37709864
3. Convergent somatic mutations in metabolism genes in chronic liver disease.. *Nature*. PMID: 34646017
4. Indole-3-Acetic Acid Alleviates Nonalcoholic Fatty Liver Disease in Mice via Attenuation of Hepatic Lipogenesis, and Oxidative and Inflammatory Stress.. *Nutrients*. PMID: 31484323
5. GPAM upregulation enhances hepatic fat deposition and reduces visceral adipose tissue in response to trans-fatty acids.. *Journal of gastroenterology*. PMID: 41046275

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.1 |
| 高置信度残基 (pLDDT>90) 占比 | 48.3% |
| 置信残基 (pLDDT 70-90) 占比 | 31.2% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 13.9% |
| 有序区域 (pLDDT>70) 占比 | 79.5% |
| 可用 PDB 条目 | 8E4Y, 8E50 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8E4Y, 8E50）+ AlphaFold高质量预测（pLDDT=80.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR022284, IPR045520, IPR041728, IPR028354, IPR002123; Pfam: PF01553, PF19277 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GPAT3 | 0.995 | 0.000 | — |
| GPAT4 | 0.992 | 0.000 | — |
| GPD1 | 0.972 | 0.000 | — |
| GPD1L | 0.957 | 0.000 | — |
| GPD2 | 0.955 | 0.000 | — |
| AGPAT1 | 0.932 | 0.000 | — |
| GK | 0.931 | 0.000 | — |
| GK2 | 0.930 | 0.000 | — |
| AGPAT2 | 0.926 | 0.000 | — |
| ADPRM | 0.921 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IDE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| ALDH1L1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| SLC25A6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| HNRNPC | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CIDEB | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PSMC4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDH5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ATP2B2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SIRT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Bub1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.1 + PDB: 8E4Y, 8E50 | pLDDT=80.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion outer membrane / Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GPAM — Glycerol-3-phosphate acyltransferase 1, mitochondrial，研究基础较多，新颖性有限。
2. 蛋白大小828 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 146 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HCL2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119927-GPAM/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPAM
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HCL2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (approved)。来源: https://www.proteinatlas.org/ENSG00000119927-GPAM/subcellular

![](https://images.proteinatlas.org/60090/1089_F11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/60090/1089_F11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/60090/1663_H3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/60090/1663_H3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/60090/1666_A4_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/60090/1666_A4_33_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HCL2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
