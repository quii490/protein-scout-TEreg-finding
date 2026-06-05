---
type: protein-evaluation
gene: "TRIM55"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRIM55 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRIM55 / MURF2, RNF29 |
| 蛋白名称 | Tripartite motif-containing protein 55 |
| 蛋白大小 | 548 aa / 60.5 kDa |
| UniProt ID | Q9BYV6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; 额外: Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 548 aa / 60.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=24 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR017903, IPR050617, IPR027370, IPR000315, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Cytosol | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- microtubule (GO:0005874)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 24 |
| PubMed broad count | 37 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MURF2, RNF29 |

**关键文献**:
1. TRIM55 promotes noncanonical NF-κB signaling and B cell-mediated immune responses by coordinating p100 ubiquitination and processing.. *Science signaling*. PMID: 37816088
2. TRIM55 restricts the progression of hepatocellular carcinoma through ubiquitin-proteasome-mediated degradation of NF90.. *Cell death discovery*. PMID: 39420007
3. SUMO-3 promotes the ubiquitin-dependent turnover of TRIM55.. *Biochemistry and cell biology = Biochimie et biologie cellulaire*. PMID: 37703582
4. TRIM55 inhibits colorectal cancer development via enhancing protein degradation of c-Myc.. *Cancer medicine*. PMID: 37212463
5. Genetic and functional implications of an exonic TRIM55 variant in heart failure.. *Journal of molecular and cellular cardiology*. PMID: 31866377

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.4 |
| 高置信度残基 (pLDDT>90) 占比 | 39.8% |
| 置信残基 (pLDDT 70-90) 占比 | 12.6% |
| 中等置信 (pLDDT 50-70) 占比 | 5.1% |
| 低置信 (pLDDT<50) 占比 | 42.5% |
| 有序区域 (pLDDT>70) 占比 | 52.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.4），有序残基占 52.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017903, IPR050617, IPR027370, IPR000315, IPR001841; Pfam: PF00643, PF13445 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TTN | 0.960 | 0.625 | — |
| BBOX1 | 0.847 | 0.000 | — |
| SQSTM1 | 0.792 | 0.481 | — |
| NBR1 | 0.750 | 0.095 | — |
| TCAP | 0.665 | 0.454 | — |
| UBE2D3 | 0.654 | 0.647 | — |
| TRIM63 | 0.638 | 0.590 | — |
| TRIM23 | 0.615 | 0.488 | — |
| USP13 | 0.591 | 0.474 | — |
| USP39 | 0.581 | 0.511 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000323913.4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15696|pubmed:22493164 |
| PYGM | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| TRIM63 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| UBE2D1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2D2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2D3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| TRIM23 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15696|pubmed:22493164 |
| BRAP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| RNF114 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| TRIM27 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.4 + PDB: 无 | pLDDT=67.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Golgi apparatus; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TRIM55 — Tripartite motif-containing protein 55，非常新颖，仅有少数基础研究。
2. 蛋白大小548 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 24 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=67.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BYV6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000147573-TRIM55/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRIM55
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BYV6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000147573-TRIM55/subcellular

![](https://images.proteinatlas.org/53691/1138_C1_12_blue_red_green.jpg)
![](https://images.proteinatlas.org/53691/1138_C1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/53691/1149_C1_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/53691/1149_C1_9_blue_red_green.jpg)
![](https://images.proteinatlas.org/53691/1446_H11_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/53691/1446_H11_6_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BYV6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
