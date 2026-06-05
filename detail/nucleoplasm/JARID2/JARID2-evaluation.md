---
type: protein-evaluation
gene: "JARID2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## JARID2 — REJECTED (研究热度过高 (PubMed strict=192，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | JARID2 / JMJ |
| 蛋白名称 | Protein Jumonji |
| 蛋白大小 | 1246 aa / 138.7 kDa |
| UniProt ID | Q92833 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Mitochondria; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1246 aa / 138.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=192 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.9; PDB: 4X3E, 5HYN, 5LS6, 5WAI, 6C23, 6C24, 6NQ3 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001606, IPR036431, IPR003347, IPR003349, IPR004 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.5/180** | |
| **归一化总分** | | | **42.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Mitochondria | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- ESC/E(Z) complex (GO:0035098)
- histone methyltransferase complex (GO:0035097)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 192 |
| PubMed broad count | 326 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: JMJ |

**关键文献**:
1. JARID2 coordinates with the NuRD complex to facilitate breast tumorigenesis through response to adipocyte-derived leptin.. *Cancer communications (London, England)*. PMID: 37658635
2. EPOP and MTF2 Activate PRC2 Activity through DNA-sequence specificity.. *bioRxiv : the preprint server for biology*. PMID: 41040190
3. Piezo1-Mediated Calcium Flux Transfers Mechanosignal to Yes-Associated Protein to Stimulate Matrix Production in Keloid.. *The Journal of investigative dermatology*. PMID: 40254148
4. PRC2.1- and PRC2.2-specific accessory proteins drive recruitment of different forms of canonical PRC1.. *Molecular cell*. PMID: 37030288
5. DNA Methylation Signature for JARID2-Neurodevelopmental Syndrome.. *International journal of molecular sciences*. PMID: 35887345

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.9 |
| 高置信度残基 (pLDDT>90) 占比 | 31.5% |
| 置信残基 (pLDDT 70-90) 占比 | 15.3% |
| 中等置信 (pLDDT 50-70) 占比 | 3.6% |
| 低置信 (pLDDT<50) 占比 | 49.6% |
| 有序区域 (pLDDT>70) 占比 | 46.8% |
| 可用 PDB 条目 | 4X3E, 5HYN, 5LS6, 5WAI, 6C23, 6C24, 6NQ3, 6WKR, 7KSO, 8TB9 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.9），有序残基占 46.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001606, IPR036431, IPR003347, IPR003349, IPR004198; Pfam: PF01388, PF02373, PF02375 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AEBP2 | 0.999 | 0.988 | — |
| SUZ12 | 0.999 | 0.986 | — |
| EED | 0.999 | 0.974 | — |
| RBBP4 | 0.999 | 0.927 | — |
| EZH2 | 0.999 | 0.890 | — |
| MTF2 | 0.998 | 0.539 | — |
| EZH1 | 0.998 | 0.959 | — |
| RBBP7 | 0.995 | 0.433 | — |
| PHF19 | 0.995 | 0.921 | — |
| PHF1 | 0.982 | 0.221 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG2926 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG17826 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Eed | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12117|pubmed:20064375 |
| Suz12 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12117|pubmed:20064375 |
| Ezh2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12117|pubmed:20064375 |
| Ezh1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12118|pubmed:20064376 |
| ALB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15174051|imex:IM-19123 |
| Es2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Setx | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12118|pubmed:20064376 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.9 + PDB: 4X3E, 5HYN, 5LS6, 5WAI, 6C23,  | pLDDT=61.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Mitochondria | 一致 |
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
1. JARID2 — Protein Jumonji，研究基础较多，新颖性有限。
2. 蛋白大小1246 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 192 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=61.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 192 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92833
- Protein Atlas: https://www.proteinatlas.org/ENSG00000008083-JARID2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=JARID2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92833
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000008083-JARID2/subcellular

![](https://images.proteinatlas.org/63889/1193_H4_2_red_green.jpg)
![](https://images.proteinatlas.org/63889/1193_H4_4_red_green.jpg)
![](https://images.proteinatlas.org/63889/1223_H4_2_red_green.jpg)
![](https://images.proteinatlas.org/63889/1223_H4_3_red_green.jpg)
![](https://images.proteinatlas.org/63889/1279_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/63889/1279_A1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92833-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
