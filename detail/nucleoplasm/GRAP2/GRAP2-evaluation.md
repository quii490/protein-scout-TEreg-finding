---
type: protein-evaluation
gene: "GRAP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GRAP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GRAP2 / GADS, GRB2L, GRID |
| 蛋白名称 | GRB2-related adapter protein 2 |
| 蛋白大小 | 330 aa / 37.9 kDa |
| UniProt ID | O75791 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Plasma membrane; UniProt: Nucleus; Cytoplasm; Endosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 330 aa / 37.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=37 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=70.2; PDB: 5GJH |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR035646, IPR043539, IPR000980, IPR036860, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.0/180** | |
| **归一化总分** | | | **70.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Plasma membrane | Supported |
| UniProt | Nucleus; Cytoplasm; Endosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endosome (GO:0005768)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 37 |
| PubMed broad count | 123 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GADS, GRB2L, GRID |

**关键文献**:
1. GCIP, a novel human grap2 and cyclin D interacting protein, regulates E2F-mediated transcriptional activity.. *The Journal of biological chemistry*. PMID: 10801854
2. GRAP2 is a prognostic biomarker and correlated with immune infiltration in lung adenocarcinoma.. *Journal of clinical laboratory analysis*. PMID: 36181310
3. Grap2 cyclin D interacting protein negatively regulates CREB‑binding protein, inhibiting fibroblast‑like synoviocyte growth.. *Molecular medicine reports*. PMID: 33576455
4. Spi-1 and Spi-B control the expression of the Grap2 gene in B cells.. *Gene*. PMID: 15936902
5. Leukocyte-specific adaptor protein Grap2 interacts with hematopoietic progenitor kinase 1 (HPK1) to activate JNK signaling pathway in T lymphocytes.. *Oncogene*. PMID: 11313918

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.2 |
| 高置信度残基 (pLDDT>90) 占比 | 29.7% |
| 置信残基 (pLDDT 70-90) 占比 | 31.2% |
| 中等置信 (pLDDT 50-70) 占比 | 4.2% |
| 低置信 (pLDDT<50) 占比 | 34.8% |
| 有序区域 (pLDDT>70) 占比 | 60.9% |
| 可用 PDB 条目 | 5GJH |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=70.2，有序区 60.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR035646, IPR043539, IPR000980, IPR036860, IPR036028; Pfam: PF00017, PF00018 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LCP2 | 0.999 | 0.945 | — |
| LAT | 0.999 | 0.535 | — |
| PLCG1 | 0.998 | 0.135 | — |
| GRB2 | 0.993 | 0.292 | — |
| SHC1 | 0.992 | 0.099 | — |
| VAV1 | 0.992 | 0.093 | — |
| CD28 | 0.983 | 0.729 | — |
| FYB1 | 0.980 | 0.341 | — |
| ITK | 0.979 | 0.100 | — |
| ZAP70 | 0.974 | 0.100 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Blnk | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| KRTAP4-12 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| HNRNPK | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RBPMS | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CCNDBP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| YWHAE | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| GFAP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| STAMBP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| LCP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ZBTB7B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.2 + PDB: 5GJH | pLDDT=70.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Endosome / Nucleoplasm, Cytosol; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GRAP2 — GRB2-related adapter protein 2，非常新颖，仅有少数基础研究。
2. 蛋白大小330 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 37 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75791
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100351-GRAP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GRAP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75791
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000100351-GRAP2/subcellular

![](https://images.proteinatlas.org/5788/1825_F1_12_cr5abb7f3b92f0b_red_green.jpg)
![](https://images.proteinatlas.org/5788/1825_F1_5_cr5abb7f3b92161_red_green.jpg)
![](https://images.proteinatlas.org/5788/21_G11_1_red_green.jpg)
![](https://images.proteinatlas.org/5788/21_G11_2_red_green.jpg)
![](https://images.proteinatlas.org/5788/22_G11_1_red_green.jpg)
![](https://images.proteinatlas.org/5788/22_G11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75791-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
