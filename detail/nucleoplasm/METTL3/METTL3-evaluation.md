---
type: protein-evaluation
gene: "METTL3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## METTL3 — REJECTED (研究热度过高 (PubMed strict=1994，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | METTL3 / MTA70 |
| 蛋白名称 | N(6)-adenosine-methyltransferase catalytic subunit METTL3 |
| 蛋白大小 | 580 aa / 64.5 kDa |
| UniProt ID | Q86U44 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Nuclear bodies, Golgi apparatus; UniProt: Nucleus; Nucleus speckle; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 580 aa / 64.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1994 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=75.4; PDB: 5IL0, 5IL1, 5IL2, 5K7M, 5K7U, 5K7W, 5L6D |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR025848, IPR007757, IPR029063; Pfam: PF05063 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Nuclear bodies, Golgi apparatus | Supported |
| UniProt | Nucleus; Nucleus speckle; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- nuclear body (GO:0016604)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA N6-methyladenosine methyltransferase complex (GO:0036396)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1994 |
| PubMed broad count | 3455 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MTA70 |

**关键文献**:
1. Lactylation-driven METTL3-mediated RNA m(6)A modification promotes immunosuppression of tumor-infiltrating myeloid cells.. *Molecular cell*. PMID: 35320754
2. Roles of METTL3 in cancer: mechanisms and therapeutic targeting.. *Journal of hematology & oncology*. PMID: 32854717
3. METTL3 drives NAFLD-related hepatocellular carcinoma and is a therapeutic target for boosting immunotherapy.. *Cell reports. Medicine*. PMID: 37586322
4. METTL3 regulates heterochromatin in mouse embryonic stem cells.. *Nature*. PMID: 33505026
5. Promoter-bound METTL3 maintains myeloid leukaemia by m(6)A-dependent translation control.. *Nature*. PMID: 29186125

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.4 |
| 高置信度残基 (pLDDT>90) 占比 | 33.4% |
| 置信残基 (pLDDT 70-90) 占比 | 37.9% |
| 中等置信 (pLDDT 50-70) 占比 | 5.3% |
| 低置信 (pLDDT<50) 占比 | 23.3% |
| 有序区域 (pLDDT>70) 占比 | 71.3% |
| 可用 PDB 条目 | 5IL0, 5IL1, 5IL2, 5K7M, 5K7U, 5K7W, 5L6D, 5L6E, 5TEY, 5YZ9 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（5IL0, 5IL1, 5IL2, 5K7M, 5K7U, 5K7W, 5L6D, 5L6E, 5TEY, 5YZ9）+ AlphaFold极高置信度预测（pLDDT=75.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR025848, IPR007757, IPR029063; Pfam: PF05063 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| METTL14 | 0.999 | 0.994 | — |
| RBM15B | 0.999 | 0.243 | — |
| VIRMA | 0.999 | 0.543 | — |
| METTL4 | 0.999 | 0.000 | — |
| ZC3H13 | 0.999 | 0.331 | — |
| RBM15 | 0.999 | 0.360 | — |
| CBLL1 | 0.999 | 0.292 | — |
| WTAP | 0.999 | 0.846 | — |
| EIF3H | 0.991 | 0.292 | — |
| METTL16 | 0.990 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FIP37 | psi-mi:"MI:0018"(two hybrid) | pubmed:18505803|imex:IM-19060 |
| "BEST:GH09876" | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dysb | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| strat | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Mettl14 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Pnn | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG9014 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Mst84Da | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG13022 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| EBI-180445 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.4 + PDB: 5IL0, 5IL1, 5IL2, 5K7M, 5K7U,  | pLDDT=75.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus speckle; Cytoplasm / Nucleoplasm, Cytosol; 额外: Nuclear bodies, Golgi ap | 一致 |
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
1. METTL3 — N(6)-adenosine-methyltransferase catalytic subunit METTL3，研究基础较多，新颖性有限。
2. 蛋白大小580 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1994 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1994 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86U44
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165819-METTL3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=METTL3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86U44
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000165819-METTL3/subcellular

![](https://images.proteinatlas.org/79662/2073_E6_1_red_green.jpg)
![](https://images.proteinatlas.org/79662/2073_E6_2_red_green.jpg)
![](https://images.proteinatlas.org/79662/2081_G1_3_red_green.jpg)
![](https://images.proteinatlas.org/79662/2081_G1_4_red_green.jpg)
![](https://images.proteinatlas.org/79662/2082_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/79662/2082_F2_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86U44-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
