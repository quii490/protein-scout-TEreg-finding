---
type: protein-evaluation
gene: "REXO2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## REXO2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | REXO2 / SFN, SMFN |
| 蛋白名称 | Oligoribonuclease, mitochondrial |
| 蛋白大小 | 237 aa / 26.8 kDa |
| UniProt ID | Q9Y3B8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Mitochondria; 额外: Nucleoli, Focal adhesion sites; UniProt: Mitochondrion intermembrane space; Mitochondrion matrix; Mit |
| 蛋白大小 | 10/10 | ×1 | 10 | 237 aa / 26.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=88.2; PDB: 6J7Y, 6J7Z, 6J80, 6N6I, 6N6J, 6N6K, 6RCI |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR022894, IPR013520, IPR012337, IPR036397; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **146.0/180** | |
| **归一化总分** | | | **81.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nucleoli, Focal adhesion sites | Supported |
| UniProt | Mitochondrion intermembrane space; Mitochondrion matrix; Mitochondrion; Cytoplasm; Nucleus; Cytoplas... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- focal adhesion (GO:0005925)
- mitochondrial intermembrane space (GO:0005758)
- mitochondrial matrix (GO:0005759)
- mitochondrion (GO:0005739)
- nucleolus (GO:0005730)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 24 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SFN, SMFN |

**关键文献**:
1. Pathway-based cancer transcriptome deciphers a high-resolution intrinsic heterogeneity within bladder cancer classification.. *Journal of translational medicine*. PMID: 40528211
2. Heterozygous de novo dominant negative mutation of REXO2 results in interferonopathy.. *Nature communications*. PMID: 39107301
3. Update on new autoinflammatory disorders from the 2024 Pediatric Rheumatology European Society Congress.. *Pediatric rheumatology online journal*. PMID: 41152899
4. RUNX1 and REXO2 are associated with the heterogeneity and prognosis of IDH wild type lower grade glioma.. *Scientific reports*. PMID: 34088969
5. Structural insights into nanoRNA degradation by human Rexo2.. *RNA (New York, N.Y.)*. PMID: 30926754

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.2 |
| 高置信度残基 (pLDDT>90) 占比 | 72.6% |
| 置信残基 (pLDDT 70-90) 占比 | 10.1% |
| 中等置信 (pLDDT 50-70) 占比 | 10.5% |
| 低置信 (pLDDT<50) 占比 | 6.8% |
| 有序区域 (pLDDT>70) 占比 | 82.7% |
| 可用 PDB 条目 | 6J7Y, 6J7Z, 6J80, 6N6I, 6N6J, 6N6K, 6RCI, 6RCL, 6RCN, 6STY |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6J7Y, 6J7Z, 6J80, 6N6I, 6N6J, 6N6K, 6RCI, 6RCL, 6RCN, 6STY）+ AlphaFold极高置信度预测（pLDDT=88.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR022894, IPR013520, IPR012337, IPR036397; Pfam: PF00929 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| REXO5 | 0.953 | 0.106 | — |
| REXO1 | 0.946 | 0.106 | — |
| REXO4 | 0.845 | 0.095 | — |
| EXO1 | 0.835 | 0.000 | — |
| PGM5 | 0.794 | 0.000 | — |
| PNPT1 | 0.747 | 0.000 | — |
| EXOSC10 | 0.622 | 0.088 | — |
| SUPV3L1 | 0.606 | 0.000 | — |
| ELAC2 | 0.578 | 0.000 | — |
| PGM1 | 0.567 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EIF1B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ATG5 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MPG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TRAF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ENST00000265881 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.2 + PDB: 6J7Y, 6J7Z, 6J80, 6N6I, 6N6J,  | pLDDT=88.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion intermembrane space; Mitochondrion m / Mitochondria; 额外: Nucleoli, Focal adhesion sites | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. REXO2 — Oligoribonuclease, mitochondrial，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小237 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y3B8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000076043-REXO2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=REXO2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y3B8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (supported)。来源: https://www.proteinatlas.org/ENSG00000076043-REXO2/subcellular

![](https://images.proteinatlas.org/38450/449_E3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38450/449_E3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/38450/452_E3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/38450/452_E3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/38450/455_E3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38450/455_E3_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y3B8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
