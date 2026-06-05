---
type: protein-evaluation
gene: "THAP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## THAP1 — REJECTED (研究热度过高 (PubMed strict=149，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | THAP1 |
| 蛋白名称 | THAP domain-containing protein 1 |
| 蛋白大小 | 213 aa / 24.9 kDa |
| UniProt ID | Q9NVV9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus, nucleoplasm; Nucleus, PML body |
| 蛋白大小 | 10/10 | ×1 | 10 | 213 aa / 24.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=149 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=70.9; PDB: 2JTG, 2KO0, 2L1G |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026516, IPR006612, IPR038441; Pfam: PF05485 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.0/180** | |
| **归一化总分** | | | **55.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus, nucleoplasm; Nucleus, PML body | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- fibrillar center (GO:0001650)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PML body (GO:0016605)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 149 |
| PubMed broad count | 241 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genetics and Pathogenesis of Dystonia.. *Annual review of pathology*. PMID: 37738511
2. Genetics in dystonia.. *Parkinsonism & related disorders*. PMID: 24262166
3. Tremor in Primary Monogenic Dystonia.. *Current neurology and neuroscience reports*. PMID: 34264428
4. DYT-THAP1: exploring gene expression in fibroblasts for potential biomarker discovery.. *Neurogenetics*. PMID: 38498291
5. Isolated dystonia: clinical and genetic updates.. *Journal of neural transmission (Vienna, Austria : 1996)*. PMID: 33247415

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.9 |
| 高置信度残基 (pLDDT>90) 占比 | 16.9% |
| 置信残基 (pLDDT 70-90) 占比 | 38.0% |
| 中等置信 (pLDDT 50-70) 占比 | 27.7% |
| 低置信 (pLDDT<50) 占比 | 17.4% |
| 有序区域 (pLDDT>70) 占比 | 54.9% |
| 可用 PDB 条目 | 2JTG, 2KO0, 2L1G |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2JTG, 2KO0, 2L1G）+ AlphaFold高质量预测（pLDDT=70.9），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026516, IPR006612, IPR038441; Pfam: PF05485 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TOR1A | 0.969 | 0.292 | — |
| PAWR | 0.916 | 0.292 | — |
| THAP11 | 0.906 | 0.000 | — |
| THAP12 | 0.895 | 0.045 | — |
| THAP7 | 0.875 | 0.094 | — |
| ZCCHC10 | 0.856 | 0.617 | — |
| SGCE | 0.852 | 0.000 | — |
| RRM1 | 0.811 | 0.292 | — |
| GNAL | 0.806 | 0.000 | — |
| ANO3 | 0.777 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000254250.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NUP62 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ZCCHC10 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PHF1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MMTAG2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NKAP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ZNF408 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| FXR2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| AP2B1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| POLR2M | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.9 + PDB: 2JTG, 2KO0, 2L1G | pLDDT=70.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleoplasm; Nucleus, PML body / Nucleoplasm | 一致 |
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
1. THAP1 — THAP domain-containing protein 1，研究基础较多，新颖性有限。
2. 蛋白大小213 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 149 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 149 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NVV9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000131931-THAP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=THAP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NVV9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000131931-THAP1/subcellular

![](https://images.proteinatlas.org/71310/1360_G8_3_red_green.jpg)
![](https://images.proteinatlas.org/71310/1360_G8_5_red_green.jpg)
![](https://images.proteinatlas.org/71310/1367_G8_4_red_green.jpg)
![](https://images.proteinatlas.org/71310/1367_G8_5_red_green.jpg)
![](https://images.proteinatlas.org/71310/1417_H4_2_red_green.jpg)
![](https://images.proteinatlas.org/71310/1417_H4_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NVV9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
