---
type: protein-evaluation
gene: "SERPINB9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SERPINB9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SERPINB9 / PI9 |
| 蛋白名称 | Serpin B9 |
| 蛋白大小 | 376 aa / 42.4 kDa |
| UniProt ID | P50453 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 376 aa / 42.4 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=52 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.2; PDB: 8ZCR |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000240, IPR023795, IPR023796, IPR000215, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.0/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- extracellular matrix (GO:0031012)
- extracellular space (GO:0005615)
- Golgi apparatus (GO:0005794)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 52 |
| PubMed broad count | 188 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PI9 |

**关键文献**:
1. Signatures of T cell dysfunction and exclusion predict cancer immunotherapy response.. *Nature medicine*. PMID: 30127393
2. Single-cell multiomics reveals persistence of HIV-1 in expanded cytotoxic T cell clones.. *Immunity*. PMID: 35320704
3. MUC1-C integrates type II interferon and chromatin remodeling pathways in immunosuppression of prostate cancer.. *Oncoimmunology*. PMID: 35127252
4. Microbiota-reprogrammed phosphatidylcholine inactivates cytotoxic CD8 T cells through UFMylation via exosomal SerpinB9 in multiple myeloma.. *Nature communications*. PMID: 40128181
5. Immune-privileged tissues formed from immunologically cloaked mouse embryonic stem cells survive long term in allogeneic hosts.. *Nature biomedical engineering*. PMID: 37996616

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.2 |
| 高置信度残基 (pLDDT>90) 占比 | 83.0% |
| 置信残基 (pLDDT 70-90) 占比 | 11.4% |
| 中等置信 (pLDDT 50-70) 占比 | 0.8% |
| 低置信 (pLDDT<50) 占比 | 4.8% |
| 有序区域 (pLDDT>70) 占比 | 94.4% |
| 可用 PDB 条目 | 8ZCR |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.2，有序区 94.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000240, IPR023795, IPR023796, IPR000215, IPR036186; Pfam: PF00079 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GZMB | 0.958 | 0.294 | — |
| CTSG | 0.920 | 0.045 | — |
| CASP1 | 0.792 | 0.292 | — |
| PRF1 | 0.682 | 0.051 | — |
| PIGM | 0.676 | 0.000 | — |
| CASP8 | 0.523 | 0.292 | — |
| TIMD4 | 0.499 | 0.472 | — |
| ST3GAL3 | 0.492 | 0.482 | — |
| ULBP3 | 0.455 | 0.000 | — |
| TRAF5 | 0.433 | 0.420 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BRD7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CRMP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EEF1A1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| MED31 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RBM48 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GAPDH | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RIF1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TLE1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TP53 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TUBB2A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.2 + PDB: 8ZCR | pLDDT=91.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SERPINB9 — Serpin B9，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小376 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 52 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P50453
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170542-SERPINB9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SERPINB9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P50453
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000170542-SERPINB9/subcellular

![](https://images.proteinatlas.org/30067/1611_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/30067/1611_C2_6_red_green.jpg)
![](https://images.proteinatlas.org/30067/1719_E1_13_cr58048c42963eb_red_green.jpg)
![](https://images.proteinatlas.org/30067/1719_E1_8_cr58048c3900e22_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P50453-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
