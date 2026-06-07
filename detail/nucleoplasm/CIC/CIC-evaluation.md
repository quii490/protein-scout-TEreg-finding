---
type: protein-evaluation
gene: "CIC"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CIC — REJECTED (研究热度过高 (PubMed strict=866，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CIC / KIAA0306 |
| 蛋白名称 | Protein capicua homolog |
| 蛋白大小 | 2517 aa / 258.0 kDa |
| UniProt ID | Q96RK0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Nucleus |
| 蛋白大小 | 2/10 | ×1 | 2 | 2517 aa / 258.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=866 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=40.4; PDB: 2M41, 4J2J, 4J2L, 6JRP, 6KZG, 6KZH, 7M5W |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052412, IPR032147, IPR058607, IPR009071, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 866 |
| PubMed broad count | 26137 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0306 |

**关键文献**:
1. CIC-Rearranged Sarcoma.. *Surgical pathology clinics*. PMID: 38278603
2. Capicua in Human Cancer.. *Trends in cancer*. PMID: 32978089
3. Gene fusions in superficial mesenchymal neoplasms: Emerging entities and useful diagnostic adjuncts.. *Seminars in diagnostic pathology*. PMID: 37156707
4. Small round cell sarcoma tumoroid biobank reveals CIC::DUX4 sarcoma vulnerability to MCL-1 inhibition.. *Nature communications*. PMID: 40841360
5. The signaling cascade of induction and maintenance of ES cell diapause.. *Research square*. PMID: 39281867

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 40.4 |
| 高置信度残基 (pLDDT>90) 占比 | 7.3% |
| 置信残基 (pLDDT 70-90) 占比 | 2.5% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 87.9% |
| 有序区域 (pLDDT>70) 占比 | 9.8% |
| 可用 PDB 条目 | 2M41, 4J2J, 4J2L, 6JRP, 6KZG, 6KZH, 7M5W |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=40.4），有序残基占 9.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052412, IPR032147, IPR058607, IPR009071, IPR036910; Pfam: PF16090, PF00505, PF25981 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ATXN1 | 0.996 | 0.982 | — |
| ATXN1L | 0.863 | 0.296 | — |
| RBM17 | 0.847 | 0.000 | — |
| NCOR2 | 0.671 | 0.000 | — |
| ATN1 | 0.621 | 0.000 | — |
| EGFR | 0.620 | 0.163 | — |
| ETV5 | 0.573 | 0.057 | — |
| UBQLN4 | 0.564 | 0.045 | — |
| PRRC2A | 0.555 | 0.000 | — |
| FUBP1 | 0.548 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ftz-f1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| TRIM22 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| POLR1H | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| GABPB1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| GTPBP3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| ATXN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| SETD2 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| SEC62 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| CPAP | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| PICK1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=40.4 + PDB: 2M41, 4J2J, 4J2L, 6JRP, 6KZG,  | pLDDT=40.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Vesicles | 一致 |
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
1. CIC — Protein capicua homolog，研究基础较多，新颖性有限。
2. 蛋白大小2517 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 866 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=40.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 866 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96RK0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000079432-CIC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CIC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96RK0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000079432-CIC/subcellular

![](https://images.proteinatlas.org/26388/625_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/26388/625_C4_4_red_green.jpg)
![](https://images.proteinatlas.org/26388/629_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/26388/629_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/26388/631_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/26388/631_C4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96RK0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96RK0 |
| SMART | SM00398; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR052412;IPR032147;IPR058607;IPR009071;IPR036910;IPR058606; |
| Pfam | PF16090;PF00505;PF25981; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000079432-CIC/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATXN1 | Intact, Biogrid | true |
| CENPJ | Intact, Biogrid | true |
| GOLGA2 | Intact, Biogrid | true |
| NFYC | Intact, Biogrid | true |
| YWHAZ | Intact, Biogrid | true |
| ATXN1L | Biogrid | false |
| CBX3 | Biogrid | false |
| CEBPA | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
