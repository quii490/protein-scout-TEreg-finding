---
type: protein-evaluation
gene: "NAA10"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NAA10 — REJECTED (研究热度过高 (PubMed strict=101，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NAA10 / ARD1, ARD1A, TE2 |
| 蛋白名称 | N-alpha-acetyltransferase 10 |
| 蛋白大小 | 235 aa / 26.5 kDa |
| UniProt ID | P41227 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoli; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 235 aa / 26.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=101 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=80.3; PDB: 6C95, 6C9M, 6PPL, 6PW9, 9F1B, 9F1C, 9F1D |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016181, IPR045047, IPR000182; Pfam: PF00583 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoli | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- NatA complex (GO:0031415)
- nucleolus (GO:0005730)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 101 |
| PubMed broad count | 217 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ARD1, ARD1A, TE2 |

**关键文献**:
1. Epilepsy With Eyelid Myoclonia (Jeavons Syndrome).. *Pediatric neurology*. PMID: 34167046
2. Expanding the phenotypic spectrum of NAA10-related neurodevelopmental syndrome and NAA15-related neurodevelopmental syndrome.. *European journal of human genetics : EJHG*. PMID: 37130971
3. NAA10-related syndrome.. *Experimental & molecular medicine*. PMID: 30054457
4. Truncating Variants in NAA15 Are Associated with Variable Levels of Intellectual Disability, Autism Spectrum Disorder, and Congenital Anomalies.. *American journal of human genetics*. PMID: 29656860
5. N-α-acetyltransferase 10 (NAA10) in development: the role of NAA10.. *Experimental & molecular medicine*. PMID: 30054454

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.3 |
| 高置信度残基 (pLDDT>90) 占比 | 68.1% |
| 置信残基 (pLDDT 70-90) 占比 | 3.8% |
| 中等置信 (pLDDT 50-70) 占比 | 6.0% |
| 低置信 (pLDDT<50) 占比 | 22.1% |
| 有序区域 (pLDDT>70) 占比 | 71.9% |
| 可用 PDB 条目 | 6C95, 6C9M, 6PPL, 6PW9, 9F1B, 9F1C, 9F1D, 9FPZ, 9FQ0, 9QQB |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6C95, 6C9M, 6PPL, 6PW9, 9F1B, 9F1C, 9F1D, 9FPZ, 9FQ0, 9QQB）+ AlphaFold极高置信度预测（pLDDT=80.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016181, IPR045047, IPR000182; Pfam: PF00583 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NAA50 | 0.999 | 0.994 | — |
| NAA16 | 0.999 | 0.953 | — |
| NAA15 | 0.999 | 0.995 | — |
| HYPK | 0.999 | 0.978 | — |
| NAA35 | 0.976 | 0.085 | — |
| NAA30 | 0.950 | 0.000 | — |
| NAA60 | 0.948 | 0.468 | — |
| NAA38 | 0.938 | 0.000 | — |
| NAA11 | 0.935 | 0.369 | — |
| NAA25 | 0.920 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000033763.9 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| EHMT2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CDC25A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ARRB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17620599 |
| ENSP00000417763.1 | psi-mi:"MI:0889"(acetylase assay) | pubmed:16638120|imex:IM-20427 |
| HIF1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16638120|imex:IM-20427 |
| ARHGEF6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21295525|imex:IM-16535 |
| Arhgef7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21295525|imex:IM-16535 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.3 + PDB: 6C95, 6C9M, 6PPL, 6PW9, 9F1B,  | pLDDT=80.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. NAA10 — N-alpha-acetyltransferase 10，研究基础较多，新颖性有限。
2. 蛋白大小235 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 101 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 101 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P41227
- Protein Atlas: https://www.proteinatlas.org/ENSG00000102030-NAA10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NAA10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P41227
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000102030-NAA10/subcellular

![](https://images.proteinatlas.org/30711/551_H9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30711/551_H9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/30711/554_H9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30711/554_H9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/30711/560_H9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30711/560_H9_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P41227-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
