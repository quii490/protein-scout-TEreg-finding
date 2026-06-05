---
type: protein-evaluation
gene: "AADAT"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## AADAT — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AADAT / KAT2, KYAT2 |
| 蛋白名称 | Kynurenine/alpha-aminoadipate aminotransferase, mitochondrial |
| 蛋白大小 | 425 aa / 47.4 kDa |
| UniProt ID | Q8N5Z0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Plasma membrane; 额外: Vesicles; UniProt: Mitochondrion |
| 蛋白大小 | 10/10 | ×1 | 10 | 425 aa / 47.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=32 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=97.3; PDB: 2QLR, 2R2N, 2VGZ, 2XH1, 3DC1, 3UE8, 4GDY |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR004839, IPR050859, IPR015424, IPR015421; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Vesicles | Approved |
| UniProt | Mitochondrion | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- mitochondrial matrix (GO:0005759)
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 48 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KAT2, KYAT2 |

**关键文献**:
1. Characterization of the human gene encoding alpha-aminoadipate aminotransferase (AADAT).. *Molecular genetics and metabolism*. PMID: 12126930
2. Variation of genes encoding KAT1, AADAT and IDO1 as a potential risk of depression development.. *European psychiatry : the journal of the Association of European Psychiatrists*. PMID: 29777939
3. Purification and properties of 2-aminoadipate: 2-oxoglutarate aminotransferase from bovine kidney.. *The Biochemical journal*. PMID: 2803240
4. Association of kynurenine aminotransferase II gene C401T polymorphism with immune response in patients with meningitis.. *BMC medical genetics*. PMID: 21473761
5. Purification and properties of kynurenine aminotransferase from rat kidney.. *The Biochemical journal*. PMID: 1953654

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.3 |
| 高置信度残基 (pLDDT>90) 占比 | 94.6% |
| 置信残基 (pLDDT 70-90) 占比 | 5.4% |
| 中等置信 (pLDDT 50-70) 占比 | 0.0% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 100.0% |
| 可用 PDB 条目 | 2QLR, 2R2N, 2VGZ, 2XH1, 3DC1, 3UE8, 4GDY, 4GE4, 4GE7, 4GE9 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2QLR, 2R2N, 2VGZ, 2XH1, 3DC1, 3UE8, 4GDY, 4GE4, 4GE7, 4GE9）+ AlphaFold极高置信度预测（pLDDT=97.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004839, IPR050859, IPR015424, IPR015421; Pfam: PF00155 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KYAT1 | 0.999 | 0.071 | — |
| KMO | 0.983 | 0.000 | — |
| KYNU | 0.980 | 0.000 | — |
| KYAT3 | 0.960 | 0.188 | — |
| AFMID | 0.955 | 0.000 | — |
| DHTKD1 | 0.940 | 0.000 | — |
| ALDH7A1 | 0.929 | 0.000 | — |
| DLD | 0.909 | 0.000 | — |
| DLST | 0.908 | 0.000 | — |
| BCAT2 | 0.894 | 0.071 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SPACA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.3 + PDB: 2QLR, 2R2N, 2VGZ, 2XH1, 3DC1,  | pLDDT=97.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion / Plasma membrane; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

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
1. AADAT — Kynurenine/alpha-aminoadipate aminotransferase, mitochondrial，非常新颖，仅有少数基础研究。
2. 蛋白大小425 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 32 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N5Z0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000109576-AADAT/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AADAT
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N5Z0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000109576-AADAT/subcellular

![](https://images.proteinatlas.org/37502/436_B2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/37502/436_B2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/37502/442_B2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/37502/442_B2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/37502/521_B2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/37502/521_B2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N5Z0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
