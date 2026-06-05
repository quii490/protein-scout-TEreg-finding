---
type: protein-evaluation
gene: "CPSF1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CPSF1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CPSF1 / CPSF160 |
| 蛋白名称 | Cleavage and polyadenylation specificity factor subunit 1 |
| 蛋白大小 | 1443 aa / 160.9 kDa |
| UniProt ID | Q10570 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | x4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus, nucleoplasm |
| 蛋白大小 | 5/10 | x1 | 5 | 1443 aa / 160.9 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=37 篇 (≤40→8) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=82.4; PDB: 6BLY, 6BM0, 6DNH, 6F9N, 6FUW, 6URG, 6URO |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR018846, IPR058543, IPR050358, IPR004871, IPR015 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.5/180** | |
| **归一化总分** | | | **75.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- mRNA cleavage and polyadenylation specificity factor complex (GO:0005847)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 37 |
| PubMed broad count | 54 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CPSF160 |

**关键文献**:
1. HSF1 and CPSF1 affect milk fat and protein synthesis by regulating the AKT/mTOR signaling pathway.. *Journal of animal science*. PMID: 39932399
2. Familial Whole Exome Sequencing Study of 30 Families With Early-Onset High Myopia.. *Investigative ophthalmology & visual science*. PMID: 37191617
3. Development and Validation of the FIP Score for the Screening of FIP1L1::PDGFRA-Associated Hypereosinophilic Syndrome.. *The journal of allergy and clinical immunology. In practice*. PMID: 40992688
4. ABL kinases regulate the stabilization of HIF-1α and MYC through CPSF1.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 37040401
5. Aberrant expression of CPSF1 promotes head and neck squamous cell carcinoma via regulating alternative splicing.. *PloS one*. PMID: 32437477

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.4 |
| 高置信度残基 (pLDDT>90) 占比 | 60.5% |
| 置信残基 (pLDDT 70-90) 占比 | 21.0% |
| 中等置信 (pLDDT 50-70) 占比 | 4.4% |
| 低置信 (pLDDT<50) 占比 | 14.1% |
| 有序区域 (pLDDT>70) 占比 | 81.5% |
| 可用 PDB 条目 | 6BLY, 6BM0, 6DNH, 6F9N, 6FUW, 6URG, 6URO, 8E3I, 8E3Q, 8R8R |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构 + AlphaFold极高置信度（pLDDT=82.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018846, IPR058543, IPR050358, IPR004871, IPR015943; Pfam: PF10433, PF23726, PF03178 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 无PPI数据
- STRING partners: 0，IntAct interactions: 0
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.4 + PDB: 6BLY, 6BM0, 6DNH, 6F9N, 6FUW,  | pLDDT=82.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CPSF1 -- Cleavage and polyadenylation specificity factor subunit 1，非常新颖，仅有少数基础研究。
2. 蛋白大小1443 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 37 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q10570
- Protein Atlas: https://www.proteinatlas.org/ENSG00000071894-CPSF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CPSF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q10570
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000071894-CPSF1/subcellular

![](https://images.proteinatlas.org/65167/1186_F3_2_red_green.jpg)
![](https://images.proteinatlas.org/65167/1186_F3_3_red_green.jpg)
![](https://images.proteinatlas.org/65167/1200_F3_1_red_green.jpg)
![](https://images.proteinatlas.org/65167/1200_F3_2_red_green.jpg)
![](https://images.proteinatlas.org/65167/1230_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/65167/1230_G2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q10570-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
