---
type: protein-evaluation
gene: "CEBPB"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CEBPB — REJECTED (研究热度过高 (PubMed strict=742，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CEBPB / TCF5 |
| 蛋白名称 | CCAAT/enhancer-binding protein beta |
| 蛋白大小 | 345 aa / 36.1 kDa |
| UniProt ID | P17676 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 345 aa / 36.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=742 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.7; PDB: 1GTW, 1GU4, 1GU5, 1H88, 1H89, 1H8A, 1HJB |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004827, IPR046347, IPR031106, IPR016468; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- C/EBP complex (GO:1990647)
- CHOP-C/EBP complex (GO:0036488)
- chromatin (GO:0000785)
- condensed chromosome, centromeric region (GO:0000779)
- cytoplasm (GO:0005737)
- nuclear matrix (GO:0016363)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 742 |
| PubMed broad count | 1365 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TCF5 |

**关键文献**:
1. Dynamics of Cardiac Neutrophil Diversity in Murine Myocardial Infarction.. *Circulation research*. PMID: 32811295
2. Advances in tooth agenesis and tooth regeneration.. *Regenerative therapy*. PMID: 36819612
3. COL1A1-positive endothelial cells promote gastric cancer progression via the ANGPTL4-SDC4 axis driven by endothelial-to-mesenchymal transition.. *Cancer letters*. PMID: 40254092
4. Ubiquitin Ligase COP1 Suppresses Neuroinflammation by Degrading c/EBPβ in Microglia.. *Cell*. PMID: 32795415
5. Sepsis-induced endothelial dysfunction drives acute-on-chronic liver failure through Angiopoietin-2-HGF-C/EBPβ pathway.. *Hepatology (Baltimore, Md.)*. PMID: 36943063

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.7 |
| 高置信度残基 (pLDDT>90) 占比 | 19.1% |
| 置信残基 (pLDDT 70-90) 占比 | 7.5% |
| 中等置信 (pLDDT 50-70) 占比 | 26.4% |
| 低置信 (pLDDT<50) 占比 | 47.0% |
| 有序区域 (pLDDT>70) 占比 | 26.6% |
| 可用 PDB 条目 | 1GTW, 1GU4, 1GU5, 1H88, 1H89, 1H8A, 1HJB, 1IO4, 2E42, 2E43 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.7），有序残基占 26.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004827, IPR046347, IPR031106, IPR016468; Pfam: PF07716 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ATF4 | 0.997 | 0.926 | — |
| EP300 | 0.996 | 0.748 | — |
| PRDM16 | 0.995 | 0.154 | — |
| CEBPD | 0.994 | 0.459 | — |
| DDIT3 | 0.994 | 0.783 | — |
| HDAC1 | 0.991 | 0.547 | — |
| CEBPA | 0.990 | 0.623 | — |
| PPARG | 0.989 | 0.512 | — |
| STAT3 | 0.984 | 0.300 | — |
| MYB | 0.980 | 0.893 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| A2VD03 | psi-mi:"MI:0047"(far western blotting) | pubmed:8657121|imex:IM-23839 |
| TP53 | psi-mi:"MI:0096"(pull down) | imex:IM-14469|pubmed:16227626 |
| SMAD4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12042|pubmed:16959612 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| CCL3 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:20702408|imex:IM-23250 |
| ENSP00000520773.1 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:20702408|imex:IM-23250 |
| - | psi-mi:"MI:0412"(electrophoretic mobility supershi | pubmed:20702408|imex:IM-23250 |
| EBI-1566585 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-23786|pubmed:19064995 |
| RELA | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-23786|pubmed:19064995 |
| IL12B | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:25202013|imex:IM-23695 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.7 + PDB: 1GTW, 1GU4, 1GU5, 1H88, 1H89,  | pLDDT=59.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm | 一致 |
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
1. CEBPB — CCAAT/enhancer-binding protein beta，研究基础较多，新颖性有限。
2. 蛋白大小345 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 742 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=59.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 742 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P17676
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172216-CEBPB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CEBPB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P17676
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000172216-CEBPB/subcellular

![](https://images.proteinatlas.org/4213/653_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/4213/653_A5_2_red_green.jpg)
![](https://images.proteinatlas.org/4213/658_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/4213/658_A5_2_red_green.jpg)
![](https://images.proteinatlas.org/4213/659_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/4213/659_A5_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P17676-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
