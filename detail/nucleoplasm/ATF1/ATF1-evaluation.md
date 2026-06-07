---
type: protein-evaluation
gene: "ATF1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ATF1 — REJECTED (研究热度过高 (PubMed strict=876，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ATF1 |
| 蛋白名称 | Cyclic AMP-dependent transcription factor ATF-1 |
| 蛋白大小 | 271 aa / 29.2 kDa |
| UniProt ID | P18846 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 271 aa / 29.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=876 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004827, IPR046347, IPR003102, IPR001630; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **87.5/180** | |
| **归一化总分** | | | **48.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- ATF1-ATF4 transcription factor complex (GO:1990590)
- ATF4-CREB1 transcription factor complex (GO:1990589)
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 876 |
| PubMed broad count | 1207 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Intracranial mesenchymal tumor with FET-CREB fusion-A unifying diagnosis for the spectrum of intracranial myxoid mesenchymal tumors and angiomatoid fibrous histiocytoma-like neoplasms.. *Brain pathology (Zurich, Switzerland)*. PMID: 33141488
2. Cholesterol metabolism regulated by CAMKK2-CREB signaling promotes castration-resistant prostate cancer.. *Cell reports*. PMID: 40483692
3. MITF Pathway-Activated Cutaneous Neoplasms.. *Advances in anatomic pathology*. PMID: 40387110
4. Expanding the clinicopathologic spectrum and genomic landscape of tumors with SMARCA2/4::CREM fusions.. *The Journal of pathology*. PMID: 39344423
5. Update on gene fusions and the emerging clinicopathological landscape of peritoneal and pleural mesotheliomas and other neoplasms.. *ESMO open*. PMID: 39059063

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.8 |
| 高置信度残基 (pLDDT>90) 占比 | 20.3% |
| 置信残基 (pLDDT 70-90) 占比 | 21.0% |
| 中等置信 (pLDDT 50-70) 占比 | 23.2% |
| 低置信 (pLDDT<50) 占比 | 35.4% |
| 有序区域 (pLDDT>70) 占比 | 41.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.8），有序残基占 41.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004827, IPR046347, IPR003102, IPR001630; Pfam: PF00170, PF02173 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RPS6KA5 | 0.960 | 0.292 | — |
| CREB1 | 0.947 | 0.551 | — |
| ATF2 | 0.946 | 0.612 | — |
| CREB3L2 | 0.930 | 0.101 | — |
| CREB3 | 0.888 | 0.101 | — |
| EWSR1 | 0.874 | 0.000 | — |
| CREB3L4 | 0.861 | 0.101 | — |
| CREB3L1 | 0.855 | 0.101 | — |
| ATF4 | 0.847 | 0.095 | — |
| CREB5 | 0.841 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.8 + PDB: 无 | pLDDT=64.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ATF1 — Cyclic AMP-dependent transcription factor ATF-1，研究基础较多，新颖性有限。
2. 蛋白大小271 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 876 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=64.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 876 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P18846
- Protein Atlas: https://www.proteinatlas.org/ENSG00000123268-ATF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ATF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P18846
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000123268-ATF1/subcellular

![](https://images.proteinatlas.org/16222/944_A11_1_red_green.jpg)
![](https://images.proteinatlas.org/16222/944_A11_3_red_green.jpg)
![](https://images.proteinatlas.org/16222/947_A11_2_red_green.jpg)
![](https://images.proteinatlas.org/16222/947_A11_3_red_green.jpg)
![](https://images.proteinatlas.org/16222/952_A11_2_red_green.jpg)
![](https://images.proteinatlas.org/16222/952_A11_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P18846-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P18846 |
| SMART | SM00338; |
| UniProt Domain [FT] | DOMAIN 31..90; /note="KID"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00312"; DOMAIN 213..271; /note="bZIP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00978" |
| InterPro | IPR004827;IPR046347;IPR003102;IPR001630; |
| Pfam | PF00170;PF02173; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000123268-ATF1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATF2 | Biogrid | false |
| BRCA1 | Biogrid | false |
| CREB1 | Intact | false |
| CREBBP | Biogrid | false |
| CSNK2A1 | Biogrid | false |
| ESR1 | Intact | false |
| JUN | Intact | false |
| NFATC1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
